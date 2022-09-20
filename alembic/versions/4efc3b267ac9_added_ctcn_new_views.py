"""added ctcn new_views

Revision ID: 4efc3b267ac9
Revises: 1982aabfb5e9
Create Date: 2022-09-14 14:46:15.211124

"""
from alembic import op

from app.utils.alembic import ReplaceableObject

# revision identifiers, used by Alembic.
revision = '4efc3b267ac9'
down_revision = '1982aabfb5e9'
branch_labels = None
depends_on = None

ter_view = ReplaceableObject(
    "ctcn.new_v_ter",
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
    t.numero AS numero_f,
    t.flag_redd,
    t.flag_porz,
    t.flag_deduz,
    t.dominic_l,
    t.dominic_e,
    t.agrario_l,
    t.agrario_e,
    to_date(t.gen_regist::text, 'DDMMYYYY'::text)::text as gen_regist,
    t.gen_tipo,
    t.gen_numero,
    t.gen_progre,
    t.gen_anno,
    to_date(t.con_regist::text, 'DDMMYYYY'::text)::text as con_regist,
    t.con_tipo,
    t.con_numero,
    t.con_progre,
    t.con_anno,
    t.annotazion,
    t.mutaz_iniz,
    t.mutaz_fine,
    t.gen_causa,
    t.gen_descr,
    t.con_causa,
    t.con_descr
   FROM ctcn.ctpartic t
     JOIN ctcn.comuni c ON c.codice::text = t.codice::text
     LEFT JOIN ctcn.ctqualit q ON q.codice = t.qualita;
    """
)

fab_view = ReplaceableObject(
    "ctcn.new_v_fab",
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
            WHEN COALESCE(f.categoria, ''::character varying)::text <> ''::text THEN (substr(f.categoria::text, 1, 1) || '/'::text) || ltrim(substr(f.categoria::text, 2, 2), '0'::text)
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
    ii.subalterno AS subalterno_f,
    f.superficie,
    f.rendita_l,
    f.lotto,
    f.edificio,
    f.scala,
    f.interno_1,
    f.interno_2,
    f.piano_1,
    f.piano_2,
    f.piano_3,
    f.piano_4,
    to_date(f.gen_regist::text, 'DDMMYYYY'::text)::text as gen_regist,
    f.gen_tipo,
    f.gen_numero,
    f.gen_progre,
    f.gen_anno,
    to_date(f.con_regist::text, 'DDMMYYYY'::text)::text as con_regist,
    f.con_tipo,
    f.con_numero,
    f.con_progre,
    f.con_anno,
    f.annotazion,
    f.mutaz_iniz,
    f.mutaz_fine,
    f.prot_notif,
    f.data_notif,
    f.gen_causa,
    f.gen_descr,
    f.con_causa,
    f.con_descr,
    f.flag_class
   FROM ctcn.cuarcuiu f
     JOIN ctcn.cuidenti ii ON ii.codice::text = f.codice::text AND ii.sezione::text = f.sezione::text AND ii.immobile = f.immobile AND ii.tipo_imm::text = f.tipo_imm::text AND ii.progressiv = f.progressiv
     JOIN ctcn.comuni c ON c.codice::text = f.codice::text;
    """
)

def upgrade() -> None:
    op.create_view(fab_view)
    op.create_view(ter_view)


def downgrade() -> None:
    op.drop_view(fab_view)
    op.drop_view(ter_view)
