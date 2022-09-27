"""Added catasto db views

Revision ID: cfd6fafbf3bc
Revises: 8375b5e3a6f1
Create Date: 2022-06-27 10:43:58.617879

"""
from alembic import op

# revision identifiers, used by Alembic.
from app.utils.alembic import ReplaceableObject

revision = "cfd6fafbf3bc"
down_revision = "8375b5e3a6f1"
branch_labels = None
depends_on = None


building_view = ReplaceableObject(
    "ctcn.v_fabbricati",
    """
    SELECT f.codice,
    f.sezione,
    f.immobile,
    f.tipo_imm,
    f.progressiv,
    ltrim(ii.foglio::text, '0'::text) AS foglio,
    ltrim(ii.numero::text, '0'::text) AS particella,
    ltrim(ii.subalterno::text, '0'::text) AS subalterno,
    c.comune::text ||
        CASE
            WHEN c.provincia::text <> ''::text THEN (' ('::text || c.provincia::text) || ')'::text
            ELSE ''::text
        END AS comune,
    ltrim(f.zona::text, '0'::text) AS zona_censuaria,
        CASE
            WHEN COALESCE(f.categoria, ''::character varying)::text <> ''::text THEN (substr(f.categoria::text, 1, 1) || 
            '/'::text) || ltrim(substr(f.categoria::text, 2, 2), '0'::text)
            ELSE ''::text
        END AS categoria,
    ltrim(f.classe::text, '0'::text) AS classe,
        CASE
            WHEN COALESCE(f.consistenz, ''::character varying)::text <> ''::text THEN
            CASE
                WHEN f.categoria::text ~~ 'A%'::text THEN (f.consistenz::text || ' van'::text) ||
                CASE
                    WHEN f.consistenz::text = '1'::text THEN 'o'::text
                    ELSE 'i'::text
                END
                WHEN f.categoria::text ~~ 'B%'::text THEN f.consistenz::text || ' mc'::text
                WHEN f.categoria::text ~~ 'C%'::text THEN f.consistenz::text || ' mq'::text
                ELSE ''::text
            END
            ELSE ''::text
        END AS consistenza,
    f.rendita_e AS rendita,
        CASE f.partita
            WHEN 'C'::text THEN 'Soppressa'::text
            ELSE ltrim(f.partita::text, '0'::text)
        END AS partita,
    to_date(f.gen_eff::text, 'DDMMYYYY'::text) AS data_inizio,
    to_date(f.con_eff::text, 'DDMMYYYY'::text) AS data_fine,
    COALESCE(to_date(f.con_eff::text, 'DDMMYYYY'::text), 'now'::text::date + 1) AS data_fine_f,
    ii.foglio AS foglio_f,
    ii.numero AS numero_f,
    ii.subalterno AS subalterno_f
   FROM ctcn.cuarcuiu f
     JOIN ctcn.cuidenti ii ON ii.codice::text = f.codice::text AND ii.sezione::text = f.sezione::text AND ii.immobile = 
     f.immobile AND ii.tipo_imm::text = f.tipo_imm::text AND ii.progressiv = f.progressiv
     JOIN ctcn.comuni c ON c.codice::text = f.codice::text;
    """
)


land_view = ReplaceableObject(
    "ctcn.v_terreni",
    """
    SELECT t.codice,
    t.sezione,
    t.immobile,
    t.tipo_imm,
    t.progressiv,
    c.comune::text ||
        CASE
            WHEN c.provincia::text <> ''::text THEN (' ('::text || c.provincia::text) || ')'::text
            ELSE ''::text
        END AS comune,
    t.foglio,
    ltrim(t.numero::text, '0'::text) AS particella,
    t.subalterno,
    upper(q.qualita::text) AS qualita,
    ltrim(t.classe::text, '0'::text) AS classe,
    t.ettari,
    t.are,
    t.centiare,
    t.dominic_e AS reddito_dominicale,
    t.agrario_e AS reddito_agrario,
        CASE t.partita
            WHEN 'C'::text THEN 'Soppressa'::text
            ELSE ltrim(t.partita::text, '0'::text)
        END AS partita,
    to_date(t.gen_eff::text, 'DDMMYYYY'::text) AS data_inizio,
    to_date(t.con_eff::text, 'DDMMYYYY'::text) AS data_fine,
    COALESCE(to_date(t.con_eff::text, 'DDMMYYYY'::text), 'now'::text::date + 1) AS data_fine_f,
    t.numero AS numero_f
   FROM ctcn.ctpartic t
     JOIN ctcn.comuni c ON c.codice::text = t.codice::text
     LEFT JOIN ctcn.ctqualit q ON q.codice = t.qualita;
    """
)


v_properties_ls_view = ReplaceableObject(
    "ctcn.v_immobili_pf",
    """
    SELECT t.codice,
    t.sezione,
    t.immobile,
    t.tipo_imm,
    btrim((f.cognome::text || ' '::text) || f.nome::text) AS nominativo,
    c.comune AS comune_nascita,
    to_date(NULLIF(btrim(f.data::text), ''::text), 'DDMMYYYY'::text) AS data_nascita,
    f.codfiscale AS codice_fiscale,
    COALESCE(tt.titolo, t.titolo) AS titolo,
        CASE
            WHEN COALESCE(t.numeratore, 0) > 0 THEN (t.numeratore || '/'::text) || t.denominato
            ELSE ''::text
        END AS quota,
    to_date(t.gen_valida::text, 'DDMMYYYY'::text) AS data_inizio,
    to_date(t.con_valida::text, 'DDMMYYYY'::text) AS data_fine,
    COALESCE(to_date(t.con_valida::text, 'DDMMYYYY'::text), 'now'::text::date + 1) AS data_fine_f,
    t.identifica
   FROM ctcn.cttitola t
     JOIN ctcn.ctfisica f ON f.codice::text = t.codice::text AND f.sezione::text = t.sezione::text 
     AND f.soggetto = t.soggetto AND f.tipo_sog::text = t.tipo_sog::text
     JOIN ctcn.comuni c ON f.luogo::text = c.codice::text
     LEFT JOIN ctcn.cttitoli tt ON tt.codice::text = t.diritto::text AND 
     (t.diritto::text <> ALL (ARRAY['99 '::character varying::text, '990'::character varying::text]));
    """
)

v_properties_ns_view = ReplaceableObject(
    "ctcn.v_immobili_pg",
    """
    SELECT t.codice,
    t.sezione,
    t.immobile,
    t.tipo_imm,
    g.denominaz AS nominativo,
    c.comune AS comune_sede,
    g.codfiscale AS codice_fiscale,
    COALESCE(tt.titolo, t.titolo) AS titolo,
        CASE
            WHEN COALESCE(t.numeratore, 0) > 0 THEN (t.numeratore || '/'::text) || t.denominato
            ELSE ''::text
        END AS quota,
    to_date(t.gen_valida::text, 'DDMMYYYY'::text) AS data_inizio,
    to_date(t.con_valida::text, 'DDMMYYYY'::text) AS data_fine,
    COALESCE(to_date(t.con_valida::text, 'DDMMYYYY'::text), 'now'::text::date + 1) AS data_fine_f,
    t.identifica
   FROM ctcn.cttitola t
     JOIN ctcn.ctnonfis g ON g.codice::text = t.codice::text AND g.sezione::text = t.sezione::text 
     AND g.soggetto = t.soggetto AND g.tipo_sog::text = t.tipo_sog::text
     JOIN ctcn.comuni c ON g.sede::text = c.codice::text
     LEFT JOIN ctcn.cttitoli tt ON tt.codice::text = t.diritto::text AND (t.diritto::text <> 
     ALL (ARRAY['99 '::character varying::text, '990'::character varying::text]));
    """
)


v_subject_building_view = ReplaceableObject(
    "ctcn.v_soggetti_fabbricati",
    """
    SELECT t.codice,
    t.sezione,
    t.soggetto,
    t.tipo_sog,
    'Fabbricati'::character varying AS tipo_immobile,
    COALESCE(tt.titolo, t.titolo) AS titolo,
        CASE
            WHEN COALESCE(t.numeratore, 0) > 0 THEN (t.numeratore || '/'::text) || t.denominato
            ELSE ''::text
        END AS quota,
    (((c.comune::text ||
        CASE
            WHEN c.provincia::text <> ''::text THEN (' ('::text || c.provincia::text) || ')'::text
            ELSE ''::text
        END) || ' ('::text) || t.codice::text) || ')'::text AS ubicazione,
    ltrim(ii.foglio::text, '0'::text) AS foglio,
    ltrim(ii.numero::text, '0'::text) AS particella,
    ltrim(ii.subalterno::text, '0'::text) AS subalterno,
    btrim(
        CASE
            WHEN COALESCE(ltrim(f.zona::text, '0'::text), ''::text) <> ''::text THEN 
            ('zona '::text || ltrim(f.zona::text, '0'::text)) || ', '::text
            ELSE ''::text
        END ||
        CASE
            WHEN COALESCE(f.categoria, ''::character varying)::text <> ''::text THEN 
            (('cat. '::text || substr(f.categoria::text, 1, 1)) || '/'::text) 
            || ltrim(substr(f.categoria::text, 2, 2), '0'::text)
            ELSE ''::text
        END, ', '::text) AS classamento,
    ltrim(f.classe::text, '0'::text) AS classe,
        CASE
            WHEN COALESCE(f.consistenz, ''::character varying)::text <> ''::text THEN
            CASE
                WHEN f.categoria::text ~~ 'A%'::text THEN (f.consistenz::text || ' van'::text) ||
                CASE
                    WHEN f.consistenz::text = '1'::text THEN 'o'::text
                    ELSE 'i'::text
                END
                WHEN f.categoria::text ~~ 'B%'::text THEN f.consistenz::text || ' mc'::text
                WHEN f.categoria::text ~~ 'C%'::text THEN f.consistenz::text || ' mq'::text
                ELSE ''::text
            END
            ELSE ''::text
        END AS consistenza,
    f.rendita_e AS rendita,
        CASE f.partita
            WHEN 'C'::text THEN 'Soppressa'::text
            ELSE ltrim(f.partita::text, '0'::text)
        END AS partita,
    to_date(t.gen_valida::text, 'DDMMYYYY'::text) AS data_inizio,
    to_date(t.con_valida::text, 'DDMMYYYY'::text) AS data_fine,
    COALESCE(to_date(t.con_valida::text, 'DDMMYYYY'::text), 'now'::text::date + 1) AS data_fine_f,
    to_date(f.gen_eff::text, 'DDMMYYYY'::text) AS data_inizio_imm,
    COALESCE(to_date(f.con_eff::text, 'DDMMYYYY'::text), 'now'::text::date + 1) AS data_fine_imm,
    t.identifica,
    t.immobile
   FROM ctcn.cttitola t
     JOIN ctcn.comuni c ON c.codice::text = t.codice::text
     JOIN ctcn.cuarcuiu f ON f.codice::text = t.codice::text AND f.sezione::text = t.sezione::text 
     AND f.immobile = t.immobile AND f.tipo_imm::text = t.tipo_imm::text
     JOIN ctcn.cuidenti ii ON ii.codice::text = f.codice::text AND ii.sezione::text = f.sezione::text 
     AND ii.immobile = f.immobile AND ii.tipo_imm::text = f.tipo_imm::text AND ii.progressiv = f.progressiv
     LEFT JOIN ctcn.cttitoli tt ON tt.codice::text = t.diritto::text 
     AND (t.diritto::text <> ALL (ARRAY['99 '::character varying::text, '990'::character varying::text]))
  WHERE to_date(f.gen_eff::text, 'DDMMYYYY'::text) < COALESCE(to_date(t.con_valida::text, 'DDMMYYYY'::text), 
  'now'::text::date) AND COALESCE(to_date(f.con_eff::text, 'DDMMYYYY'::text), 
  'now'::text::date) > to_date(t.gen_valida::text, 'DDMMYYYY'::text);
    """
)

v_subject_land_view = ReplaceableObject(
    "ctcn.v_soggetti_terreni",
    """
    SELECT t.codice,
    t.sezione,
    t.soggetto,
    t.tipo_sog,
    'Terreni'::character varying AS tipo_immobile,
    COALESCE(tt.titolo, t.titolo) AS titolo,
        CASE
            WHEN COALESCE(t.numeratore, 0) > 0 THEN (t.numeratore || '/'::text) || t.denominato
            ELSE ''::text
        END AS quota,
    (((c.comune::text ||
        CASE
            WHEN c.provincia::text <> ''::text THEN (' ('::text || c.provincia::text) || ')'::text
            ELSE ''::text
        END) || ' ('::text) || t.codice::text) || ')'::text AS ubicazione,
    p.foglio::character varying AS foglio,
    ltrim(p.numero::text, '0'::text) AS particella,
    p.subalterno,
    upper(q.qualita::text) AS classamento,
    ltrim(p.classe::text, '0'::text) AS classe,
    btrim((
        CASE
            WHEN COALESCE(p.ettari, 0) > 0 THEN p.ettari || ' ha, '::text
            ELSE ''::text
        END ||
        CASE
            WHEN COALESCE(p.are, 0) > 0 THEN p.are || ' are, '::text
            ELSE ''::text
        END) ||
        CASE
            WHEN COALESCE(p.centiare, 0) > 0 THEN p.centiare || ' ca'::text
            ELSE ''::text
        END, ', '::text) AS consistenza,
    btrim(
        CASE
            WHEN COALESCE(p.dominic_e, ''::character varying)::text <> ''::text THEN 'Dom. '::text || p.dominic_e::text
            ELSE ''::text
        END ||
        CASE
            WHEN COALESCE(p.agrario_e, ''::character varying)::text <> ''::text THEN 
            ' - Agr. '::text || p.agrario_e::text
            ELSE ''::text
        END, ' - '::text) AS rendita,
        CASE p.partita
            WHEN 'C'::text THEN 'Soppressa'::text
            ELSE ltrim(p.partita::text, '0'::text)
        END AS partita,
    to_date(t.gen_valida::text, 'DDMMYYYY'::text) AS data_inizio,
    to_date(t.con_valida::text, 'DDMMYYYY'::text) AS data_fine,
    COALESCE(to_date(t.con_valida::text, 'DDMMYYYY'::text), 'now'::text::date + 1) AS data_fine_f,
    to_date(p.gen_eff::text, 'DDMMYYYY'::text) AS data_inizio_imm,
    COALESCE(to_date(p.con_eff::text, 'DDMMYYYY'::text), 'now'::text::date + 1) AS data_fine_imm,
    t.identifica,
    t.immobile
   FROM ctcn.cttitola t
     JOIN ctcn.ctpartic p ON p.codice::text = t.codice::text 
     AND p.sezione::text = t.sezione::text AND p.immobile = t.immobile AND p.tipo_imm::text = t.tipo_imm::text
     JOIN ctcn.comuni c ON c.codice::text = t.codice::text
     LEFT JOIN ctcn.cttitoli tt ON tt.codice::text = t.diritto::text 
     AND (t.diritto::text <> ALL (ARRAY['99 '::character varying::text, '990'::character varying::text]))
     LEFT JOIN ctcn.ctqualit q ON q.codice = p.qualita
  WHERE to_date(p.gen_eff::text, 'DDMMYYYY'::text) < COALESCE(to_date(t.con_valida::text, 'DDMMYYYY'::text), 
  'now'::text::date) AND COALESCE(to_date(p.con_eff::text, 'DDMMYYYY'::text), 'now'::text::date) > 
  to_date(t.gen_valida::text, 'DDMMYYYY'::text);
    """
)


def upgrade():
    op.create_view(land_view)
    op.create_view(building_view)
    op.create_view(v_properties_ns_view)
    op.create_view(v_properties_ls_view)
    op.create_view(v_subject_building_view)
    op.create_view(v_subject_land_view)


def downgrade():
    op.drop_view(land_view)
    op.drop_view(building_view)
    op.drop_view(v_properties_ns_view)
    op.drop_view(v_properties_ls_view)
    op.drop_view(v_subject_building_view)
    op.drop_view(v_subject_land_view)
