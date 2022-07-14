from datetime import date

from sqlalchemy import text

from app.utils.db import dal


def get_city_by_name(name: str = ""):
    statement = text(
        f"""select distinct c.comune as name, c.codice as code
    from ctcn.comuni c inner join ctmp.fogli f on (c.codice = f.comune)
    where c.comune ilike '{name}' || '%' group by c.codice order by 1 """
    )

    return dal.connection.execute(statement).fetchall()


def get_section_by_city_code(city_code: str):
    statement = text(
        f"""select f.sezione as name
        from ctcn.comuni c
        inner join ctmp.fogli f on (c.codice = f.comune)
        where c.codice = '{city_code}'group by f.sezione order by 1"""
    )

    return dal.connection.execute(statement).fetchall()


def get_sheet_by_city_code(city_code: str):
    statement = text(
        f"""
        select cityCode, section, sheet, number, geom,
        st_envelope(geom) as extent
        from
        (select f.foglio::integer as number,
        f.comune  as cityCode,
        f.sezione  as section,
        f.foglio  as sheet,
        st_transform(st_setsrid(st_extent(f.geom),3004),3857) as geom
        from ctmp.fogli f
        where f.comune = '{city_code}'
        group by 1,2,3,4) as sheets order by 1"""
    )
    return dal.connection.execute(statement).fetchall()


def get_building_by_city_code_and_sheet_code(city_code: str, sheet_code: str):
    today = date.today().strftime("%Y-%m-%d")
    statement = text(
        f"""
        select vf.codice as cityCode,
        f.sezione as section,
        vf.foglio as sheet,
        vf.numero_f as number,
        st_transform(st_setsrid(st_extent(f.geom),3004),3857) as geom,
        st_envelope(st_transform(st_setsrid(st_extent(f.geom),3004),3857))
        as extent
        from ctcn.v_fabbricati vf
        right join ctmp.fabbricati f on f.comune = vf.codice
        and f.foglio = vf.foglio and f.numero = vf.particella
        where vf.codice = '{city_code}' and vf.foglio = '{sheet_code}'
        and vf.data_inizio<='{today}' and vf.data_fine_f>='{today}'
        group by 1,2,3,4 order by 1,2,3,4"""
    )
    return dal.connection.execute(statement).fetchall()


def get_land_by_city_code_and_sheet_code(city_code: str, sheet_code: str):
    today = date.today().strftime("%Y-%m-%d")
    statement = text(
        f"""
        select vt.codice as cityCode,
        p.sezione as section,
        vt.foglio as sheet,
        vt.numero_f as number,
        st_transform(st_setsrid(st_extent(p.geom),3004),3857) as geom,
        st_envelope(st_transform(st_setsrid(st_extent(p.geom),3004),3857))
        as extent
        from ctcn.v_terreni vt
        right join ctmp.particelle p on p.comune = vt.codice
        and p.foglio = vt.foglio::text and p.numero = vt.particella
        where vt.codice = '{city_code}' and vt.foglio::text = '{sheet_code}'
        and vt.data_inizio<='{today}' and vt.data_fine_f>='{today}'
        group by 1,2,3,4
        order by 1,2,3,4"""
    )
    return dal.connection.execute(statement).fetchall()


def get_land_details(city_code: str, sheet_code: str, number: str):
    today = date.today().strftime("%Y-%m-%d")
    statement = text(
        f"""
        select
        vt.immobile as property,
        vt.tipo_imm as propertyType,
        vt.subalterno as subordinate,
        vt.qualita  as quality,
        vt.classe as class,
        vt.ettari as hectares,
        vt.are,
        vt.centiare,
        vt.partita as lot,
        vt.reddito_dominicale as cadastralRent,
        vt.reddito_agrario as agriculturalRent
        from ctcn.v_terreni vt where
        vt.codice = '{city_code}' and
        vt.foglio = '{sheet_code}' and
        vt.numero_f = '{number}' and
        vt.data_inizio::text<='{today}' and
        vt.data_fine_f::text>='{today}'
    """
    )
    return dal.connection.execute(statement).fetchall()


def get_building_details(city_code: str, sheet_code: str, number: str):
    today = date.today().strftime("%Y-%m-%d")
    statement = text(
        f"""
        select vf.subalterno as subordinate,
        vf.immobile as property,
        vf.tipo_imm as propertyType,
        vf.zona_censuaria as censusZone,
        vf.categoria as category,
        vf.classe as _class,
        vf.consistenza as consistency,
        vf.rendita as rent,
        vf.partita as lot
        from ctcn.v_fabbricati vf
        where vf.codice = '{city_code}'
        and vf.foglio = '{sheet_code}'
        and vf.numero_f = '{number}'
        and vf.data_inizio::text<='{today}'
        and vf.data_fine_f::text>='{today}'
        """
    )
    return dal.connection.execute(statement).fetchall()


def get_property_by_subject(subjects, subject_type):
    statement = text(
        f"""
        select buildings.cityCode,
        buildings.section,
        buildings.sheet,
        buildings.number,
        st_transform(st_setsrid(ST_Envelope(buildings.geom),3004),3857)
        as geom,
        st_envelope(st_transform(st_setsrid(ST_Envelope(buildings.geom),3004),3857))
        as extent,
        vsf.ubicazione as city,
        vsf.subalterno as subordinate,
        vsf.titolo as right,
        vsf.quota as part,
        vsf.classamento as classification,
        vsf.classe as class,
        vsf.consistenza as consistency,
        vsf.rendita as income,
        vsf.partita as lot,
        vsf.tipo_immobile as propertyType
        from
        (select f.comune  as cityCode, f.sezione as section,
        f.foglio  as sheet, f.numero as number , f.geom
        from ctmp.fabbricati f) as buildings
        right join ctcn.v_soggetti_fabbricati vsf
        on  buildings.number = vsf.particella
        and buildings.cityCode = vsf.codice
        and buildings.sheet = vsf.foglio
        where vsf.soggetto in ({subjects}) and vsf.tipo_sog='{subject_type}'
        union
        select
        lands.cityCode,
        lands.section,
        lands.sheet,
        lands.number,
        st_transform(st_setsrid(ST_Envelope(lands.geom),3004),3857)
        as geom,
        st_envelope(st_transform(st_setsrid(ST_Envelope(lands.geom),3004),3857))
        as extent,
        vst.ubicazione as city,
        vst.subalterno as subordinate,
        vst.titolo as right,
        vst.quota as part,
        vst.classamento as classification,
        vst.classe as class,
        vst.consistenza as consistency,
        vst.rendita as income,
        vst.partita as lot,
        vst.tipo_immobile as propertyType
        from
        (select p.comune  as cityCode, p.sezione  as section,
        p.foglio as sheet, p.numero as number, p.geom
        from ctmp.particelle p) as lands
        inner join ctcn.v_soggetti_terreni vst
        on lands.number = vst.particella
        and lands.cityCode = vst.codice
        and lands.sheet = vst.foglio
        where vst.soggetto in ({subjects}) and vst.tipo_sog='{subject_type}'
        order by 1,2,3,4
    """
    )
    return dal.connection.execute(statement).fetchall()


def get_subject_by_property(city_code, property_num, property_type):
    today = date.today().strftime("%Y-%m-%d")
    statement = text(
        f"""
        select vipg.nominativo as nominative,
        vipg.codice_fiscale as fiscalCode,
        vipg.comune_sede as city,
        vipg.titolo as right,
        vipg.quota as part
        from ctcn.v_immobili_pg vipg
        where vipg.immobile={property_num}
        and vipg.tipo_imm='{property_type}'
        and vipg.codice='{city_code}'
        and vipg.data_inizio::text<='{today}'
        and vipg.data_fine_f::text>='{today}'
        union
        select vipf.nominativo as nominative,
        vipf.codice_fiscale as fiscalCode,
        vipf.comune_nascita as city,
        vipf.titolo as right,
        vipf.quota as part
        from ctcn.v_immobili_pf vipf
        where vipf.immobile={property_num}
        and vipf.codice='{city_code}'
        and vipf.tipo_imm='{property_type}'
        and vipf.data_inizio::text<='{today}'
        and vipf.data_fine_f::text>='{today}'
        """
    )
    return dal.connection.execute(statement).fetchall()


def get_natural_subject(
    fiscal_code: str = None, first_name: str = None, last_name: str = None
):
    statement = text(
        f"""
        select distinct
        string_agg(f.soggetto::text, ',') as subjects,
        f.tipo_sog as subjectType,
        f.nome as firstName,
        f.cognome as lastName,
        f.codfiscale AS fiscalCode,
        case
            when length(f.data) = 8 then to_date(f.data, 'DDMMYYYY')
        end as dateOfBirth,
        c.comune ||
        case
            when c.provincia <> '' then (' (' || c.provincia) || ')'
            else ''
        end as cityOfBirth,
        case f.sesso
            when '2' then 'Femmina'
            else 'Maschio'
            end as gender
    from ctcn.ctfisica f
    left join ctcn.comuni c ON c.codice = f.luogo
    where (f.codfiscale ilike '{fiscal_code or ''}')
    or (f.cognome ilike '{last_name or ''}'
    and f.nome ilike '{first_name or ''}')
    group by f.tipo_sog,
        f.nome,
        f.cognome,
        f.codfiscale,
        dateOfBirth,
        cityOfBirth,
        gender
    """
    )
    return dal.connection.execute(statement).fetchall()


def get_legal_subject(vat_number: str = "null", business_name: str = "null"):
    statement = text(
        f"""
        select distinct
            f.soggetto::text as subjects,
            f.tipo_sog as subjectType,
            f.denominaz as businessName,
        f.codfiscale as vatNumber,
        (select c.comune from ctcn.comuni c where c.codice = f.sede ) as branch
        from ctcn.ctnonfis f
        where (f.codfiscale like {vat_number}) or
        (f.denominaz  ilike {business_name} || '%')
        """
    )
    return dal.connection.execute(statement).fetchall()


def get_cttitola():
    statement = text("select * from ctcn.cuindiri")
    return dal.connection.execute(statement).fetchall()


def get_cuidenti():
    statement = text("select * from ctcn.cuidenti")
    return dal.connection.execute(statement).fetchall()


def get_cuindiri():
    statement = text("select * from ctcn.cuindiri")
    return dal.connection.execute(statement).fetchall()


def get_cuutilit():
    statement = text("select * from ctcn.cuutilit")
    return dal.connection.execute(statement).fetchall()


def get_cuarcuiu():
    statement = text("select * from ctcn.cuarcuiu")
    return dal.connection.execute(statement).fetchall()


def get_curiserv():
    statement = text("select * from ctcn.curiserv")
    return dal.connection.execute(statement).fetchall()


def get_ctpartic():
    statement = text("select * from ctcn.ctpartic")
    return dal.connection.execute(statement).fetchall()


def get_ctdeduzi():
    statement = text("select * from ctcn.ctdeduzi")
    return dal.connection.execute(statement).fetchall()


def get_ctporzio():
    statement = text("select * from ctcn.ctporzio")
    return dal.connection.execute(statement).fetchall()


def get_metadata(schema):
    statement = text(f"select * from {schema}.metadati")
    return dal.connection.execute(statement).fetchall()


def get_waters(schema):
    statement = text(f"select * from {schema}.acque")
    return dal.connection.execute(statement).fetchall()


def get_trusts(schema):
    statement = text(f"select * from {schema}.fiduciali")
    return dal.connection.execute(statement).fetchall()


def get_dress_lines(schema):
    statement = text(f"select * from {schema}.linee_vest")
    return dal.connection.execute(statement).fetchall()


def get_texts(schema):
    statement = text(f"select * from {schema}.testi")
    return dal.connection.execute(statement).fetchall()


def get_symbols(schema):
    statement = text(f"select * from {schema}.simboli")
    return dal.connection.execute(statement).fetchall()


def get_streets(schema):
    statement = text(f"select * from {schema}.strade")
    return dal.connection.execute(statement).fetchall()
