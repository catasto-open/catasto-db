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
    fiscalecode: str = "null",
    lastname: str = "null",
    firstname: str = "null",
    subject: str = "null",
):
    statement = text(
        cnf.APP_CONFIG.VIEW_QUERY_PERSONE_FISICA.format(
            fiscalecode, lastname, firstname, subject
        )
    )
    return dal.connection.execute(statement).fetchall()


def get_persone_fisica_with_bday(
    fiscalecode: str = "null",
    lastname: str = "null",
    firstname: str = "null",
    birthdate: str = "null",
    birthplace: str = "null",
):
    statement = text(
        cnf.APP_CONFIG.VIEW_QUERY_PERSONE_FISICA_WITH_BOTH.format(
            fiscalecode, lastname, firstname, birthdate, birthplace
        )
    )
    if birthdate == "null":
        statement = text(
            cnf.APP_CONFIG.VIEW_QUERY_PERSONE_FISICA_WITH_BPLACE.format(
                fiscalecode, lastname, firstname, birthplace
            )
        )
    if birthplace == "null":
        statement = text(
            cnf.APP_CONFIG.VIEW_QUERY_PERSONE_FISICA_WITH_BDAY.format(
                fiscalecode, lastname, firstname, birthdate
            )
        )
    return dal.connection.execute(statement).fetchall()


def get_non_fisica(
    vatNumber: str = "null", businessName: str = "null", subject: str = "null"
):
    statement = text(
        cnf.APP_CONFIG.VIEW_QUERY_NON_FISICA.format(
            vatNumber, businessName, subject
        )
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


def get_toponym(toponym: str):
    statement = text(cnf.APP_CONFIG.VIEW_QUERY_TOPONIMO.format(toponym))
    return dal.connection.execute(statement).fetchall()


def get_immobile_by_address(
    toponymCode: int,
    addressName: str,
    houseNumber: str,
    cityCode: str,
    startDate: str = None,
    endDate: str = None,
):
    if startDate and endDate:
        statement = text(
            cnf.APP_CONFIG.VIEW_QUERY_IMMOBILI_BY_IND_TEMP.format(
                toponymCode,
                addressName,
                houseNumber,
                cityCode,
                startDate,
                endDate,
            )
        )
    else:
        statement = text(
            cnf.APP_CONFIG.VIEW_QUERY_IMMOBILI_BY_IND.format(
                toponymCode, addressName, houseNumber, cityCode
            )
        )
    return dal.connection.execute(statement).fetchall()


def get_fabbricati_by_codice(
    cityCode: str,
    immobileCodice: int,
    startDate: str = None,
    endDate: str = None,
):
    if startDate and endDate:
        statement = text(
            cnf.APP_CONFIG.VIEW_QUERY_FABBRICATI_BY_CODICE_TEMP.format(
                immobileCodice, cityCode, startDate, endDate
            )
        )
    else:
        statement = text(
            cnf.APP_CONFIG.VIEW_QUERY_FABBRICATI_BY_CODICE.format(
                immobileCodice, cityCode
            )
        )
    return dal.connection.execute(statement).fetchall()


def get_terreni_by_codice(
    cityCode: str,
    immobileCodice: int,
    startDate: str = None,
    endDate: str = None,
):
    if startDate and endDate:
        statement = text(
            cnf.APP_CONFIG.VIEW_QUERY_TERRENI_BY_CODICE_TEMP.format(
                immobileCodice, cityCode, startDate, endDate
            )
        )
    else:
        statement = text(
            cnf.APP_CONFIG.VIEW_QUERY_TERRENI_BY_CODICE.format(
                immobileCodice, cityCode
            )
        )
    return dal.connection.execute(statement).fetchall()
