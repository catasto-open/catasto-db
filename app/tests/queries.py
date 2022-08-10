from sqlalchemy import text

from app.utils.db import dal
from app.configs import cnf


def get_comuni_by_name(cityName: str = "", endDate: str = None):
    if not endDate:
        statement = text(cnf.APP_CONFIG.VIEW_QUERY_COMUNI_.format(cityName))
    else:
        statement = text(
            cnf.APP_CONFIG.VIEW_QUERY_COMUNI_TEMP.format(cityName, endDate)
        )
    return dal.connection.execute(statement).fetchall()


def get_sezioni_by_city_code(cityCode: str, endDate: str = None):
    if not endDate:
        statement = text(cnf.APP_CONFIG.VIEW_QUERY_SEZIONI_.format(cityCode))
    else:
        statement = text(
            cnf.APP_CONFIG.VIEW_QUERY_SEZIONI_TEMP.format(cityCode, endDate)
        )
    return dal.connection.execute(statement).fetchall()


def get_fogli_by_city_info(
    cityCode: str, sectionCode: str, startDate: str = None, endDate: str = None
):
    if startDate and endDate:
        statement = text(
            cnf.APP_CONFIG.VIEW_QUERY_FOGLI_TEMP.format(
                cityCode, sectionCode, startDate, endDate
            )
        )
    else:
        statement = text(
            cnf.APP_CONFIG.VIEW_QUERY_FOGLI.format(cityCode, sectionCode)
        )
    return dal.connection.execute(statement).fetchall()


def get_fabbricati(
    cityCode: str,
    sectionCode: str,
    sheetCode: str,
    startDate: str = None,
    endDate: str = None,
):
    if startDate and endDate:
        statement = text(
            cnf.APP_CONFIG.VIEW_QUERY_FABBRICATI_TEMP.format(
                cityCode, sectionCode, sheetCode, startDate, endDate
            )
        )
    else:
        statement = text(
            cnf.APP_CONFIG.VIEW_QUERY_FABBRICATI.format(
                cityCode, sectionCode, sheetCode
            )
        )
    return dal.connection.execute(statement).fetchall()


def get_fabbricati_detail(
    cityCode: str,
    sheetCode: str,
    number: str,
    startDate: str = None,
    endDate: str = None,
):
    if startDate and endDate:
        statement = text(
            cnf.APP_CONFIG.VIEW_QUERY_FABBRICATI_DETAIL_TEMP.format(
                cityCode, sheetCode, number, startDate, endDate
            )
        )
    else:
        statement = text(
            cnf.APP_CONFIG.VIEW_QUERY_FABBRICATI_DETAIL.format(
                cityCode, sheetCode, number
            )
        )
    return dal.connection.execute(statement).fetchall()


def get_terreni(
    cityCode: str,
    sectionCode: str,
    sheetCode: str,
    startDate: str = None,
    endDate: str = None,
):
    if startDate and endDate:
        statement = text(
            cnf.APP_CONFIG.VIEW_QUERY_TERRENI_TEMP.format(
                cityCode, sectionCode, sheetCode, startDate, endDate
            )
        )
    else:
        statement = text(
            cnf.APP_CONFIG.VIEW_QUERY_TERRENI.format(
                cityCode, sectionCode, sheetCode
            )
        )
    return dal.connection.execute(statement).fetchall()


def get_terreno_detail(
    cityCode: str,
    sheetCode: str,
    number: str,
    startDate: str = None,
    endDate: str = None,
):
    if startDate and endDate:
        statement = text(
            cnf.APP_CONFIG.VIEW_QUERY_TERRENO_DETAIL_TEMP.format(
                cityCode, sheetCode, number, startDate, endDate
            )
        )
    else:
        statement = text(
            cnf.APP_CONFIG.VIEW_QUERY_TERRENO_DETAIL.format(
                cityCode, sheetCode, number
            )
        )
    return dal.connection.execute(statement).fetchall()


def get_titolari_immobile(
    cityCode: str,
    property: int,
    propertyType: str,
    startDate: str = None,
    endDate: str = None,
):
    if startDate and endDate:
        statement = text(
            cnf.APP_CONFIG.VIEW_QUERY_TITOLARI_IMMOBILE_TEMP.format(
                cityCode, property, propertyType, startDate, endDate
            )
        )
    else:
        statement = text(
            cnf.APP_CONFIG.VIEW_QUERY_TITOLARI_IMMOBILE.format(
                cityCode, property, propertyType
            )
        )
    return dal.connection.execute(statement).fetchall()


def get_persone_fisica(
    fiscalecode: str = "null", lastname: str = "null", firstname: str = "null"
):
    statement = text(
        cnf.APP_CONFIG.VIEW_QUERY_PERSONE_FISICA.format(
            fiscalecode, lastname, firstname
        )
    )
    return dal.connection.execute(statement).fetchall()


def get_non_fisica(vatNumber: str = "null", businessName: str = "null"):
    statement = text(
        cnf.APP_CONFIG.VIEW_QUERY_NON_FISICA.format(vatNumber, businessName)
    )
    return dal.connection.execute(statement).fetchall()


def get_soggetti(
    subjects: list,
    subjectType: str,
    startDate: str = None,
    endDate: str = None,
):
    if startDate and endDate:
        statement = text(
            cnf.APP_CONFIG.VIEW_QUERY_SOGGETTI_TEMP.format(
                ",".join(subjects), subjectType, startDate, endDate
            )
        )
    else:
        statement = text(
            cnf.APP_CONFIG.VIEW_QUERY_SOGGETTI.format(
                ",".join(subjects), subjectType
            )
        )
    return dal.connection.execute(statement).fetchall()
