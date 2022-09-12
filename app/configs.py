from pathlib import Path
from typing import Optional

from pydantic import BaseSettings, Field, BaseModel
from dotenv import load_dotenv

base_path = Path(__file__).resolve().parent.parent
env_file_path = base_path / "scripts" / "docker" / ".env"

load_dotenv(dotenv_path=env_file_path)


class AppConfig(BaseModel):
    """Application configurations."""

    COMPOSE_PROJECT_NAME: str = "catasto-open"

    POSTGIS_VERSION_TAG: str = "14-3.1"
    GS_VERSION: str = "2.20.4"
    GS_WFS_VERSION: str = "1.0.0"

    CATASTO_OPEN_CITY_LAYER = "catasto_comuni"
    CATASTO_OPEN_SECTION_LAYER = "catasto_sezioni"
    CATASTO_OPEN_SHEET_LAYER = "catasto_fogli"
    CATASTO_OPEN_LAND_LAYER = "catasto_terreni"
    CATASTO_OPEN_BUILDING_LAYER = "catasto_fabbricati"
    CATASTO_OPEN_TOWN_LAYER = "catasto_comuni_anag"
    CATASTO_OPEN_NATURAL_SUBJECT_LAYER = "catasto_persone_fisiche"
    CATASTO_OPEN_NATURAL_SUBJECT_LAYER_WBDAY = (
        "catasto_persone_fisiche_with_bday"
    )
    CATASTO_OPEN_NATURAL_SUBJECT_LAYER_WBPLACE = (
        "catasto_persone_fisiche_with_bplace"
    )
    CATASTO_OPEN_NATURAL_SUBJECT_LAYER_WBOTH = (
        "catasto_persone_fisiche_with_both"
    )
    CATASTO_OPEN_LEGAL_SUBJECT_LAYER = "catasto_persone_giuridiche"
    CATASTO_OPEN_SUBJECT_PROPERTY_LAYER = "catasto_particelle_soggetto"
    CATASTO_OPEN_LAND_DETAIL_LAYER = "catasto_dettagli_terreno"
    CATASTO_OPEN_BUILDING_DETAIL_LAYER = "catasto_dettagli_fabbricato"
    CATASTO_OPEN_PROPERTY_OWNER_LAYER = "catasto_titolari_immobile"
    CATASTO_OPEN_CITY_LAYER_TEMP = "catasto_comuni_temp"
    CATASTO_OPEN_SECTION_LAYER_TEMP = "catasto_sezioni_temp"
    CATASTO_OPEN_SHEET_LAYER_TEMP = "catasto_fogli_temp"
    CATASTO_OPEN_LAND_LAYER_TEMP = "catasto_terreni_temp"
    CATASTO_OPEN_BUILDING_LAYER_TEMP = "catasto_fabbricati_temp"
    CATASTO_OPEN_SUBJECT_PROPERTY_LAYER_TEMP = (
        "catasto_particelle_soggetto_temp"
    )
    CATASTO_OPEN_LAND_DETAIL_LAYER_TEMP = "catasto_dettagli_terreno_temp"
    CATASTO_OPEN_BUILDING_DETAIL_LAYER_TEMP = (
        "catasto_dettagli_fabbricato_temp"
    )
    CATASTO_OPEN_PROPERTY_OWNER_LAYER_TEMP = "catasto_titolari_immobile_temp"
    CATASTO_OPEN_TOPONIMO_LAYER = "catasto_toponimo"
    CATASTO_OPEN_INDIRIZZO_IMMOBILE_LAYER = "catasto_indrizzo_immobile"
    CATASTO_OPEN_INDIRIZZO_IMMOBILE_LAYER_TEMP = (
        "catasto_indrizzo_immobile_temp"
    )
    CATASTO_OPEN_BUILDING_BY_CODE_LAYER = "catasto_fabbricati_bcodice"
    CATASTO_OPEN_BUILDING_BY_CODE_LAYER_TEMP = (
        "catasto_fabbricati_bcodice_temp"
    )
    CATASTO_OPEN_LAND_BY_CODE_LAYER = "catasto_terreni_bcodice"
    CATASTO_OPEN_LAND_BY_CODE_LAYER_TEMP = "catasto_terreni_bcodice_temp"

    CTCN_COMUNI: str = "ctcn:comuni"
    CTCN_COMUNI_: str = "ctcn:comuni_"
    CTCN_SEZIONI_: str = "ctcn:sezioni_"
    CTMP_FOGLI: str = "ctmp:fogli"
    CTMP_METADATI: str = "ctmp:metadati"
    CTCN_CUIDENTI: str = "ctcn:cuidenti"
    CTCN_CUARCUIU: str = "ctcn:cuarcuiu"
    CTCN_CTPARTIC: str = "ctcn:ctpartic"
    CTCN_CTQUALIT: str = "ctcn:ctqualit"
    CTCN_CTTITOLA: str = "ctcn:cttitola"
    CTCN_CTTITOLI: str = "ctcn:cttitoli"
    CTCN_CTFISICA: str = "ctcn:ctfisica"
    CTCN_CTNONFIS: str = "ctcn:ctnonfis"
    CTCN_CUCODTOP: str = "ctcn:cucodtop"
    CTCN_CUINDIRI: str = "ctcn:cuindiri"

    CTMP_FABRICATI: str = "ctmp:fabbricati"
    CTMP_PARTICELLE: str = "ctmp:particelle"
    CTMP_ACQUE: str = "ctmp:acque"
    CTMP_FIDUCIALI: str = "ctmp:fiduciali"
    CTMP_LINEE_VEST: str = "ctmp:linee_vest"
    CTMP_TESTI: str = "ctmp:testi"
    CTMP_SIMBOLI: str = "ctmp:simboli"
    CTMP_STRADE: str = "ctmp:strade"

    VIEW_QUERY_COMUNI_ = """
    select codice as code,
        comune as name
    from ctcn.comuni_ t
        where t.tipo = 'A'
        and t.comune ilike '{0}%'||'%' order by 1
    """

    VIEW_QUERY_COMUNI = """
    select codice as code,
        comune as name
    from ctcn.comuni t
        where t.comune ilike '{0}%'||'%' order by 1
    """

    VIEW_QUERY_SEZIONI_ = """
    select s.sezione as name
    from ctcn.sezioni_ s
        inner join ctcn.comuni_ c
        on (c.codice = s.codice)
        where c.codice = '{0}'
        and
        c.tipo = 'A'
        group by s.sezione order by 1
    """

    VIEW_QUERY_FOGLI = """
    select tab.codice as citycode,
        tab.sezione as section,
        tab.foglio as sheet,
        tab.foglio::integer as number,
        st_transform(
            st_setsrid(
                st_union(tab.geom),3004),3857)
                as geom,
        st_transform(
            st_setsrid(
                st_union(tab.extent),3004),3857)
                as extent
        from (
            select distinct t.codice,
                t.sezione,
                t.gen_eff,
                t.con_eff,
                t.foglio,
                f.geom,
                st_envelope(f.geom) as extent
                from ctcn.ctpartic t
                left outer join ctmp.fogli f
                on (f.comune=t.codice
                and
                f.sezione = case
                    when t.sezione =' '
                    then '_'
                    else
                    t.sezione
                    end
                and
                t.foglio = f.foglio::integer
                )
            where t.codice = '{0}'
                and
                    coalesce(
                        to_date(t.con_eff::text,'DDMMYYYY'),
                        (('now'::text)::date + 1)) >= ('now'::text)::date
                and case '{1}' when '_'
                    then t.sezione like '%'
                    else t.sezione = '{1}'
                    end
            )
            tab
        group by tab.codice,tab.sezione,tab.foglio
    """

    VIEW_QUERY_FABBRICATI = """
    select vf.codice as cityCode,
        f.sezione as section,
        vf.foglio as sheet,
        vf.numero_f as number,
        st_transform(st_setsrid(st_extent(f.geom),3004),3857)
        as geom,
        st_envelope(st_transform(
        st_setsrid(st_extent(f.geom),3004),3857))
        as extent
    from ctcn.v_fabbricati vf
        right join ctmp.fabbricati f
        on
            f.comune = vf.codice
            and f.foglio = vf.foglio
            and f.numero = vf.particella
        where
            vf.codice = '{0}'
            and f.sezione = '{1}'
            and vf.foglio = '{2}'
            and vf.data_inizio <= ('now'::text)::date
            and vf.data_fine_f >= ('now'::text)::date
        group by 1,2,3,4
        order by 1,2,3,4
    """

    VIEW_QUERY_FABBRICATI_DETAIL = """
    select vf.subalterno as subordinate,
        vf.immobile as property,
        vf.tipo_imm as propertyType,
        vf.zona_censuaria as censusZone,
        vf.categoria as category,
        vf.classe as _class,
        vf.consistenza as consistency,
        vf.rendita as rent,
        vf.partita as lot,
        vf.data_inizio as startDate,
        vf.data_fine_f as endDate
    from ctcn.v_fabbricati vf
        where
            vf.codice = '{0}'
            and vf.foglio = '{1}'
            and vf.numero_f = '{2}'
            and vf.data_inizio <= ('now'::text)::date
            and vf.data_fine_f >= ('now'::text)::date
    order by 1
    """

    VIEW_QUERY_TERRENI = """
    select vt.codice as cityCode,
        vt.foglio as sheet,
        vt.numero_f as number,
        p.sezione as section,
        st_transform(st_setsrid(
            st_extent(p.geom),3004),3857)
            as geom,
        st_envelope(
            st_transform(
                st_setsrid(
                    st_extent(p.geom),3004),3857))
                    as extent
    from ctcn.v_terreni vt
        right join ctmp.particelle p
        on
            p.comune = vt.codice
            and p.foglio = vt.foglio::text
            and p.numero = vt.particella
        where
            vt.codice = '{0}'
            and p.sezione = '{1}'
            and vt.foglio::text = '{2}'
            and vt.data_inizio <= ('now'::text)::date
            and vt.data_fine_f >= ('now'::text)::date
        group by 1,2,3,4
        order by 1,2,3,4
    """

    VIEW_QUERY_TERRENO_DETAIL = """
    select vt.immobile as property,
        vt.tipo_imm as propertyType,
        vt.subalterno as subordinate,
        vt.qualita  as quality,
        vt.classe as class,
        vt.ettari as hectares,
        vt.are, vt.centiare,
        vt.partita as lot,
        vt.reddito_dominicale as cadastralRent,
        vt.reddito_agrario as agriculturalRent,
        vt.data_inizio as startDate,
        vt.data_fine_f as endDate
    from ctcn.v_terreni vt
        where
            vt.codice = '{0}'
            and vt.foglio = '{1}'
            and vt.numero_f = '{2}'
            and vt.data_inizio <= ('now'::text)::date
            and vt.data_fine_f >= ('now'::text)::date
    order by 1
    """

    VIEW_QUERY_TITOLARI_IMMOBILE = """
    select vipg.nominativo as nominative,
        vipg.codice_fiscale as fiscalCode,
        vipg.comune_sede as city,
        vipg.titolo as right,
        vipg.quota as part,
        vipg.data_inizio as startDate,
        vipg.data_fine_f as endDate
    from ctcn.v_immobili_pg vipg
        where
            vipg.immobile={1}
            and vipg.tipo_imm='{2}'
            and vipg.codice='{0}'
            and vipg.data_inizio <= ('now'::text)::date
            and vipg.data_fine_f >= ('now'::text)::date
    union
    select vipf.nominativo as nominative,
        vipf.codice_fiscale as fiscalCode,
        vipf.comune_nascita as city,
        vipf.titolo as right,
        vipf.quota as part,
        vipf.data_inizio as startDate,
        vipf.data_fine_f as endDate
    from ctcn.v_immobili_pf vipf
        where vipf.immobile={1}
            and vipf.codice='{0}'
            and vipf.tipo_imm='{2}'
            and vipf.data_inizio <= ('now'::text)::date
            and vipf.data_fine_f >= ('now'::text)::date
    """

    VIEW_QUERY_SOGGETTI = """
    (select buildings.cityCode,
        buildings.section,
        buildings.sheet,
        buildings.number,
        st_transform(
            st_setsrid(
                ST_Envelope(buildings.geom),3004),3857)
                as geom,
        st_envelope(
            st_transform(
                st_setsrid(
                    ST_Envelope(buildings.geom),3004),3857))
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
        vsf.tipo_immobile as propertyType,
        vsf.data_inizio as startDate,
        vsf.data_fine_f as endDate
    from (
        select f.comune as cityCode,
            f.sezione  as section,
            f.foglio  as sheet,
            f.numero as number,
            f.geom
            from ctmp.fabbricati f
        ) as buildings
        right join ctcn.v_soggetti_fabbricati vsf
        on
            buildings.number = vsf.particella
            and buildings.cityCode = vsf.codice
            and buildings.sheet = vsf.foglio
            where vsf.soggetto in ({0})
                and vsf.tipo_sog='{1}'
                and vsf.data_inizio <= ('now'::text)::date
                and vsf.data_fine_f >= ('now'::text)::date
    )
    union
    (select lands.cityCode,
        lands.section,
        lands.sheet,
        lands.number,
        st_transform(
            st_setsrid(
                ST_Envelope(lands.geom),3004),3857)
                as geom,
        st_envelope(st_transform(
            st_setsrid(
                ST_Envelope(lands.geom),3004),3857))
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
        vst.tipo_immobile as propertyType,
        vst.data_inizio as startDate,
        vst.data_fine_f as endDate
        from (
            select p.comune as cityCode,
                p.sezione as section,
                p.foglio as sheet,
                p.numero as number,
                p.geom
                from ctmp.particelle p
            )
            as lands
            inner join ctcn.v_soggetti_terreni vst
            on
                lands.number = vst.particella
                and lands.cityCode = vst.codice
                and lands.sheet = vst.foglio
                where vst.soggetto in ({0})
                    and vst.tipo_sog='{1}'
                    and vst.data_inizio <= ('now'::text)::date
                    and vst.data_fine_f >= ('now'::text)::date
    )
    order by 1,2,3,4
    """

    VIEW_QUERY_COMUNI_TEMP = """
    select codice as code,
        comune as name
    from ctcn.comuni_ t
        where t.tipo='A'
        and t.data_inizio <= '{1}'
        and t.comune ilike '{0}%'||'%' order by 1
    """

    VIEW_QUERY_SEZIONI_TEMP = """
    select s.sezione as name
    from ctcn.sezioni_ s
    inner join ctcn.comuni_ c
        on (c.codice = s.codice)
        where c.codice = '{0}'
        and
        c.data_inizio <= '{1}'
    group by s.sezione order by 1
    """

    VIEW_QUERY_FOGLI_TEMP = """
    select tab.codice as citycode,
        tab.sezione as section,
        tab.foglio as sheet,
        tab.foglio::integer as number,
        st_transform(
            st_setsrid(
                st_union(tab.geom),3004),3857)
                as geom,
        st_transform(
            st_setsrid(
                st_union(tab.extent),3004),3857)
                as extent
        from (
            select distinct t.codice,
                t.sezione,
                t.gen_eff,
                t.con_eff,
                t.foglio,
                f.geom,
                st_envelope(f.geom) as extent
                from ctcn.ctpartic t
                left outer join ctmp.fogli f
                on (f.comune=t.codice
                and
                f.sezione = case
                    when t.sezione =' '
                    then '_'
                    else
                    t.sezione
                    end
                and
                t.foglio = f.foglio::integer
                )
            where t.codice = '{0}'
                and case '{1}' when '_'
                    then t.sezione like '%'
                    else t.sezione = '{1}'
                    end
                and (
                    '{2}' between
                        to_date(t.gen_eff::text,'DDMMYYYY')
                        and
                        coalesce(
                            to_date(t.con_eff::text,'DDMMYYYY'),
                            (('now'::text)::date + 1)
                            )
                    or
                    '{3}' between
                        to_date(t.gen_eff::text,'DDMMYYYY')
                        and
                        coalesce(
                            to_date(t.con_eff::text,'DDMMYYYY'),
                            (('now'::text)::date + 1)
                            )
                    or
                    to_date(t.gen_eff::text,'DDMMYYYY') between
                    '{2}' and '{3}'
                    or
                    coalesce(
                        to_date(t.con_eff::text,'DDMMYYYY'),
                        (('now'::text)::date + 1)) between
                     '{2}' and '{3}'
                    )
            )
            tab
        group by tab.codice,tab.sezione,tab.foglio
    """

    VIEW_QUERY_FABBRICATI_TEMP = """
    select vf.codice as cityCode,
        f.sezione as section,
        vf.foglio as sheet,
        vf.numero_f as number,
        st_transform(st_setsrid(st_extent(f.geom),3004),3857)
        as geom,
        st_envelope(st_transform(
        st_setsrid(st_extent(f.geom),3004),3857))
        as extent
    from ctcn.v_fabbricati vf
        right join ctmp.fabbricati f
        on
            f.comune = vf.codice
            and f.foglio = vf.foglio
            and f.numero = vf.particella
        where
            vf.codice = '{0}'
            and f.sezione = '{1}'
            and vf.foglio = '{2}'
            and
            (
                '{3}' between vf.data_inizio and vf.data_fine_f
                or
                '{4}' between vf.data_inizio and vf.data_fine_f
                or
                vf.data_inizio between '{3}' and '{4}'
                or
                vf.data_fine_f between '{3}' and '{4}'
            )
        group by 1,2,3,4
        order by 1,2,3,4
    """

    VIEW_QUERY_FABBRICATI_DETAIL_TEMP = """
    select vf.subalterno as subordinate,
        vf.immobile as property,
        vf.tipo_imm as propertyType,
        vf.zona_censuaria as censusZone,
        vf.categoria as category,
        vf.classe as _class,
        vf.consistenza as consistency,
        vf.rendita as rent,
        vf.partita as lot,
        vf.data_inizio as startDate,
        vf.data_fine_f as endDate
    from ctcn.v_fabbricati vf
        where
            vf.codice = '{0}'
            and vf.foglio = '{1}'
            and vf.numero_f = '{2}'
            and (
                '{3}' between vf.data_inizio and vf.data_fine_f
                or
                '{4}' between vf.data_inizio and vf.data_fine_f
                or
                vf.data_inizio between '{3}' and '{4}'
                or
                vf.data_fine_f between '{3}' and '{4}'
                )
    order by 1
    """

    VIEW_QUERY_TERRENI_TEMP = """
    select vt.codice as cityCode,
        vt.foglio as sheet,
        vt.numero_f as number,
        p.sezione as section,
        st_transform(st_setsrid(
            st_extent(p.geom),3004),3857)
            as geom,
        st_envelope(
            st_transform(
                st_setsrid(
                    st_extent(p.geom),3004),3857))
                    as extent
    from ctcn.v_terreni vt
        right join ctmp.particelle p
        on
            p.comune = vt.codice
            and p.foglio = vt.foglio::text
            and p.numero = vt.particella
        where
            vt.codice = '{0}'
            and p.sezione = '{1}'
            and vt.foglio::text = '{2}'
            and
            (
                '{3}' between vt.data_inizio and vt.data_fine_f
                or
                '{4}' between vt.data_inizio and vt.data_fine_f
                or
                vt.data_inizio between '{3}' and '{4}'
                or
                vt.data_fine_f between '{3}' and '{4}'
            )
        group by 1,2,3,4
        order by 1,2,3,4
    """

    VIEW_QUERY_TERRENO_DETAIL_TEMP = """
    select vt.immobile as property,
        vt.tipo_imm as propertyType,
        vt.subalterno as subordinate,
        vt.qualita  as quality,
        vt.classe as class,
        vt.ettari as hectares,
        vt.are, vt.centiare,
        vt.partita as lot,
        vt.reddito_dominicale as cadastralRent,
        vt.reddito_agrario as agriculturalRent,
        vt.data_inizio as startDate,
        vt.data_fine_f as endDate
    from ctcn.v_terreni vt
        where
            vt.codice = '{0}'
            and vt.foglio = '{1}'
            and vt.numero_f = '{2}'
            and (
                '{3}' between vt.data_inizio and vt.data_fine_f
                or
                '{4}' between vt.data_inizio and vt.data_fine_f
                or
                vt.data_inizio between '{3}' and '{4}'
                or
                vt.data_fine_f between '{3}' and '{4}'
                )
    order by 1
    """

    VIEW_QUERY_TITOLARI_IMMOBILE_TEMP = """
    select vipg.nominativo as nominative,
        vipg.codice_fiscale as fiscalCode,
        vipg.comune_sede as city,
        vipg.titolo as right,
        vipg.quota as part,
        vipg.data_inizio as startDate,
        vipg.data_fine_f as endDate
    from ctcn.v_immobili_pg vipg
        where
            vipg.immobile={1}
            and vipg.tipo_imm='{2}'
            and vipg.codice='{0}'
            and (
                '{3}' between vipg.data_inizio and vipg.data_fine_f
                or
                '{4}' between vipg.data_inizio and vipg.data_fine_f
                or
                vipg.data_inizio between '{3}' and '{4}'
                or
                vipg.data_fine_f between '{3}' and '{4}'
                )
    union
    select vipf.nominativo as nominative,
        vipf.codice_fiscale as fiscalCode,
        vipf.comune_nascita as city,
        vipf.titolo as right,
        vipf.quota as part,
        vipf.data_inizio as startDate,
        vipf.data_fine_f as endDate
    from ctcn.v_immobili_pf vipf
        where vipf.immobile={1}
            and vipf.codice='{0}'
            and vipf.tipo_imm='{2}'
            and (
                '{3}' between vipf.data_inizio and vipf.data_fine_f
                or
                '{4}' between vipf.data_inizio and vipf.data_fine_f
                or
                vipf.data_inizio between '{3}' and '{4}'
                or
                vipf.data_fine_f between '{3}' and '{4}'
                )
    """

    VIEW_QUERY_PERSONE_FISICA = """
    select distinct
        string_agg(f.soggetto::text, ',') as subjects,
        f.tipo_sog as subjectType,
        f.nome as firstName,
        f.cognome as lastName,
        f.codfiscale AS fiscalCode,
        case
            when length(f.data) = 8
                then to_date(f.data, 'DDMMYYYY')
                end
                as dateOfBirth,
        c.comune || case
            when c.provincia <> ''
                then (' (' || c.provincia) || ')'
                else ''
                end
                as cityOfBirth,
        case f.sesso
            when '2'
                then 'Femmina'
                else 'Maschio'
                end
                as gender,
        c.provincia as province
    from ctcn.ctfisica f
    left join ctcn.comuni c
        on
            c.codice = f.luogo
        where (f.codfiscale ilike {0})
        or (
            f.cognome ilike {1}
            and
            f.nome ilike {2}
            )
        or f.soggetto = {3}
    group by
        f.tipo_sog,
        f.nome,
        f.cognome,
        f.codfiscale,
        dateOfBirth,
        cityOfBirth,
        gender,
        province
    """

    VIEW_QUERY_PERSONE_FISICA_WITH_BDAY = """
    select distinct
        string_agg(f.soggetto::text, ',') as subjects,
        f.tipo_sog as subjectType,
        f.nome as firstName,
        f.cognome as lastName,
        f.codfiscale AS fiscalCode,
        case
            when length(f.data) = 8
                then to_date(f.data, 'DDMMYYYY')
                end
                as dateOfBirth,
        c.comune || case
            when c.provincia <> ''
                then (' (' || c.provincia) || ')'
                else ''
                end
                as cityOfBirth,
        case f.sesso
            when '2'
                then 'Femmina'
                else 'Maschio'
                end
                as gender,
        c.provincia as province
    from ctcn.ctfisica f
    left join ctcn.comuni c
        on
            c.codice = f.luogo
        where (f.codfiscale ilike {0})
        or (
            f.cognome ilike {1}
            and
            f.nome ilike {2}
            and
            to_date(f.data::text, 'DDMMYYYY'::text) = {3}
            )
    group by
        f.tipo_sog,
        f.nome,
        f.cognome,
        f.codfiscale,
        dateOfBirth,
        cityOfBirth,
        gender,
        province
    """

    VIEW_QUERY_PERSONE_FISICA_WITH_BPLACE = """
    select distinct
        string_agg(f.soggetto::text, ',') as subjects,
        f.tipo_sog as subjectType,
        f.nome as firstName,
        f.cognome as lastName,
        f.codfiscale AS fiscalCode,
        case
            when length(f.data) = 8
                then to_date(f.data, 'DDMMYYYY')
                end
                as dateOfBirth,
        c.comune || case
            when c.provincia <> ''
                then (' (' || c.provincia) || ')'
                else ''
                end
                as cityOfBirth,
        case f.sesso
            when '2'
                then 'Femmina'
                else 'Maschio'
                end
                as gender,
        c.provincia as province
    from ctcn.ctfisica f
    left join ctcn.comuni c
        on
            c.codice = f.luogo
        where (f.codfiscale ilike {0})
        or (
            f.cognome ilike {1}
            and
            f.nome ilike {2}
            and f.luogo = '{3}'
            )
    group by
        f.tipo_sog,
        f.nome,
        f.cognome,
        f.codfiscale,
        dateOfBirth,
        cityOfBirth,
        gender,
        province
    """

    VIEW_QUERY_PERSONE_FISICA_WITH_BOTH = """
    select distinct
        string_agg(f.soggetto::text, ',') as subjects,
        f.tipo_sog as subjectType,
        f.nome as firstName,
        f.cognome as lastName,
        f.codfiscale AS fiscalCode,
        case
            when length(f.data) = 8
                then to_date(f.data, 'DDMMYYYY')
                end
                as dateOfBirth,
        c.comune || case
            when c.provincia <> ''
                then (' (' || c.provincia) || ')'
                else ''
                end
                as cityOfBirth,
        case f.sesso
            when '2'
                then 'Femmina'
                else 'Maschio'
                end
                as gender,
        c.provincia as province
    from ctcn.ctfisica f
    left join ctcn.comuni c
        on
            c.codice = f.luogo
        where (f.codfiscale ilike {0})
        or (
            f.cognome ilike {1}
            and
            f.nome ilike {2}
            and
            to_date(f.data::text, 'DDMMYYYY'::text) = {3}
            and f.luogo = '{4}'
            )
    group by
        f.tipo_sog,
        f.nome,
        f.cognome,
        f.codfiscale,
        dateOfBirth,
        cityOfBirth,
        gender,
        province
    """

    VIEW_QUERY_NON_FISICA = """
    select distinct
        f.soggetto::text as subjects,
        f.tipo_sog as subjectType,
        f.denominaz as businessName,
        f.codfiscale as vatNumber,
        c.comune as branch,
        c.provincia as province
    from ctcn.ctnonfis f
    left join ctcn.comuni c
        on
        c.codice = f.sede
    where
        (f.codfiscale like {0})
        or
        (f.denominaz ilike {1})
        or
        (f.soggetto = {2})
    """

    VIEW_QUERY_SOGGETTI_TEMP = """
    (select buildings.cityCode,
        buildings.section,
        buildings.sheet,
        buildings.number,
        st_transform(
            st_setsrid(
                ST_Envelope(buildings.geom),3004),3857)
                as geom,
        st_envelope(
            st_transform(
                st_setsrid(
                    ST_Envelope(buildings.geom),3004),3857))
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
        vsf.tipo_immobile as propertyType,
        vsf.data_inizio as startDate,
        vsf.data_fine_f as endDate
    from (
        select f.comune as cityCode,
            f.sezione  as section,
            f.foglio  as sheet,
            f.numero as number,
            f.geom
            from ctmp.fabbricati f
        ) as buildings
        right join ctcn.v_soggetti_fabbricati vsf
        on
            buildings.number = vsf.particella
            and buildings.cityCode = vsf.codice
            and buildings.sheet = vsf.foglio
            where vsf.soggetto in ({0})
                and vsf.tipo_sog='{1}'
                and (
                    '{2}' between vsf.data_inizio and vsf.data_fine_f
                    or
                    '{3}' between vsf.data_inizio and vsf.data_fine_f
                    or
                    vsf.data_inizio between '{2}' and '{3}'
                    or
                    vsf.data_fine_f between '{2}' and '{3}'
                    )
    )
    union
    (select lands.cityCode,
        lands.section,
        lands.sheet,
        lands.number,
        st_transform(
            st_setsrid(
                ST_Envelope(lands.geom),3004),3857)
                as geom,
        st_envelope(st_transform(
            st_setsrid(
                ST_Envelope(lands.geom),3004),3857))
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
        vst.tipo_immobile as propertyType,
        vst.data_inizio as startDate,
        vst.data_fine_f as endDate
        from (
            select p.comune as cityCode,
                p.sezione as section,
                p.foglio as sheet,
                p.numero as number,
                p.geom
                from ctmp.particelle p
            )
            as lands
            inner join ctcn.v_soggetti_terreni vst
            on
                lands.number = vst.particella
                and lands.cityCode = vst.codice
                and lands.sheet = vst.foglio
                where vst.soggetto in ({0})
                    and vst.tipo_sog='{1}'
                    and (
                        '{2}' between vst.data_inizio and vst.data_fine_f
                        or
                        '{3}' between vst.data_inizio and vst.data_fine_f
                        or
                        vst.data_inizio between '{2}' and '{3}'
                        or
                        vst.data_fine_f between '{2}' and '{3}'
                        )
    )
    order by 1,2,3,4
    """

    VIEW_QUERY_TOPONIMO = """
    select
        c.codice as code,
        c.toponimo as toponym
    from ctcn.cucodtop c
        where
        c.toponimo ilike '{0}%' || '%'
    """

    VIEW_QUERY_IMMOBILI_BY_IND = """
    select vf.codice as cityCode,
        f.sezione as section,
        vf.foglio as sheet,
        vf.numero_f as number,
        st_transform(st_setsrid(st_extent(f.geom),3004),3857)
        as geom,
        st_envelope(st_transform(
        st_setsrid(st_extent(f.geom),3004),3857))
        as extent
    from ctcn.v_fabbricati vf
        right join ctmp.fabbricati f
        on
            f.comune = vf.codice
            and f.foglio = vf.foglio
            and f.numero = vf.particella
        inner join ctcn.cuindiri c
        on
            c.codice = vf.codice
            and c.immobile = vf.immobile
        where
            c.toponimo = {0}
            and c.indirizzo ilike '{1}%'
            and ltrim(coalesce(c.civico1,''),'0') like '{2}'
            and c.codice = '{3}'
            and vf.data_inizio <= ('now'::text)::date
            and vf.data_fine_f >= ('now'::text)::date
        group by 1,2,3,4
        order by 1,2,3,4
    """

    VIEW_QUERY_IMMOBILI_BY_IND_TEMP = """
    select vf.codice as cityCode,
        f.sezione as section,
        vf.foglio as sheet,
        vf.numero_f as number,
        st_transform(st_setsrid(st_extent(f.geom),3004),3857)
        as geom,
        st_envelope(st_transform(
        st_setsrid(st_extent(f.geom),3004),3857))
        as extent
    from ctcn.v_fabbricati vf
        right join ctmp.fabbricati f
        on
            f.comune = vf.codice
            and f.foglio = vf.foglio
            and f.numero = vf.particella
        inner join ctcn.cuindiri c
        on
            c.codice = vf.codice
            and c.immobile = vf.immobile
        where
            c.toponimo = {0}
            and c.indirizzo ilike '{1}%'
            and ltrim(coalesce(c.civico1,''),'0') like '{2}'
            and c.codice = '{3}'
            and
            (
                '{4}' between vf.data_inizio and vf.data_fine_f
                or
                '{5}' between vf.data_inizio and vf.data_fine_f
                or
                vf.data_inizio between '{4}' and '{5}'
                or
                vf.data_fine_f between '{4}' and '{5}'
            )
        group by 1,2,3,4
        order by 1,2,3,4
    """

    VIEW_QUERY_FABBRICATI_BY_CODICE = """
    select vf.codice as cityCode,
        f.sezione as section,
        vf.foglio as sheet,
        vf.numero_f as number,
        st_transform(st_setsrid(st_extent(f.geom),3004),3857)
        as geom,
        st_envelope(st_transform(
        st_setsrid(st_extent(f.geom),3004),3857))
        as extent
    from ctcn.v_fabbricati vf
        right join ctmp.fabbricati f
        on
            f.comune = vf.codice
            and f.foglio = vf.foglio
            and f.numero = vf.particella
        where
            vf.immobile = {0}
            and vf.codice = '{1}'
            and vf.data_inizio <= ('now'::text)::date
            and vf.data_fine_f >= ('now'::text)::date
        group by 1,2,3,4
        order by 1,2,3,4
    """

    VIEW_QUERY_FABBRICATI_BY_CODICE_TEMP = """
    select vf.codice as cityCode,
        f.sezione as section,
        vf.foglio as sheet,
        vf.numero_f as number,
        st_transform(st_setsrid(st_extent(f.geom),3004),3857)
        as geom,
        st_envelope(st_transform(
        st_setsrid(st_extent(f.geom),3004),3857))
        as extent
    from ctcn.v_fabbricati vf
        right join ctmp.fabbricati f
        on
            f.comune = vf.codice
            and f.foglio = vf.foglio
            and f.numero = vf.particella
        where
            vf.immobile = {0}
            and vf.codice = '{1}'
            and
            (
                '{2}' between vf.data_inizio and vf.data_fine_f
                or
                '{3}' between vf.data_inizio and vf.data_fine_f
                or
                vf.data_inizio between '{2}' and '{3}'
                or
                vf.data_fine_f between '{2}' and '{3}'
            )
        group by 1,2,3,4
        order by 1,2,3,4
    """

    VIEW_QUERY_TERRENI_BY_CODICE = """
    select vt.codice as cityCode,
        vt.foglio as sheet,
        vt.numero_f as number,
        p.sezione as section,
        st_transform(st_setsrid(
            st_extent(p.geom),3004),3857)
                as geom,
        st_envelope(
            st_transform(
                st_setsrid(
                    st_extent(p.geom),3004),3857))
                        as extent
    from ctcn.v_terreni vt
        right join ctmp.particelle p
        on
            p.comune = vt.codice
            and p.foglio = vt.foglio::text
            and p.numero = vt.particella
        where
            vt.codice = '{1}'
            and vt.immobile = {0}
            and vt.data_inizio <= ('now'::text)::date
            and vt.data_fine_f >= ('now'::text)::date
    group by 1,2,3,4
    order by 1,2,3,4
    """

    VIEW_QUERY_TERRENI_BY_CODICE_TEMP = """
    select vt.codice as cityCode,
        vt.foglio as sheet,
        vt.numero_f as number,
        p.sezione as section,
        st_transform(st_setsrid(
            st_extent(p.geom),3004),3857)
                as geom,
        st_envelope(
            st_transform(
                st_setsrid(
                    st_extent(p.geom),3004),3857))
                        as extent
    from ctcn.v_terreni vt
        right join ctmp.particelle p
        on
            p.comune = vt.codice
            and p.foglio = vt.foglio::text
            and p.numero = vt.particella
        where
            vt.codice = '{1}'
            and vt.immobile = {0}
            and
            (
                '{2}' between vt.data_inizio and vt.data_fine_f
                or
                '{3}' between vt.data_inizio and vt.data_fine_f
                or
                vt.data_inizio between '{2}' and '{3}'
                or
                vt.data_fine_f between '{2}' and '{3}'
            )
    group by 1,2,3,4
    order by 1,2,3,4
    """


class GlobalConfig(BaseSettings):
    """Global configurations."""

    # These variables will be loaded from the .env file. However, if
    # there is a shell environment variable having the same name,
    # that will take precedence.

    APP_CONFIG: AppConfig = AppConfig()

    # define global variables with the Field class
    ENV_STATE: Optional[str] = Field(None, env="ENV_STATE")

    # environment specific variables do not need the Field class
    POSTGRES_HOST: Optional[str] = None
    POSTGRES_HOST_PORT: Optional[int] = None
    POSTGRES_CONTAINER_PORT: Optional[int] = None
    POSTGRES_USER: Optional[str] = None
    POSTGRES_PASS: Optional[str] = None
    POSTGRES_DB: Optional[str] = None

    CATASTO_OPEN_GS_WORKSPACE: Optional[str] = None
    CATASTO_OPEN_GS_WORKSPACE_NAMESPACE: Optional[str] = None
    CATASTO_OPEN_GS_DATASTORE: Optional[str] = None

    GEOSERVER_HOST: Optional[str] = None
    GEOSERVER_HOST_PORT: Optional[str] = None
    GEOSERVER_CONTAINER_PORT: Optional[str] = None
    GEOSERVER_DATA_DIR: Optional[str] = None
    GEOWEBCACHE_CACHE_DIR: Optional[str] = None
    GEOSERVER_ADMIN_PASSWORD: Optional[str] = None
    GEOSERVER_ADMIN_USER: Optional[str] = None
    INITIAL_MEMORY: Optional[str] = None
    MAXIMUM_MEMORY: Optional[str] = None


class DevConfig(GlobalConfig):
    """Development configurations."""

    class Config:
        env_prefix: str = "DEV_"


class ProdConfig(GlobalConfig):
    """Production configurations."""

    class Config:
        env_prefix: str = "PROD_"


class FactoryConfig:
    """Returns a config instance depending on the ENV_STATE variable."""

    def __init__(self, env_state: Optional[str]):
        self.env_state = env_state

    def __call__(self):
        if self.env_state == "dev":
            return DevConfig()

        elif self.env_state == "prod":
            return ProdConfig()


cnf = FactoryConfig(GlobalConfig().ENV_STATE)()
