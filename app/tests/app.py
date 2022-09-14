# flake8: noqa

import datetime
import json
import unittest
import requests

from app.configs import cnf
from app.utils.db import dal
from app.tests.fixtures import populate_db_with_sample_data, get_json_from_file
import geoalchemy2  # noqa

from app.tests.queries import (
    get_comuni_by_name,
    get_persone_fisica_with_bday,
    get_sezioni_by_city_code,
    get_fogli_by_city_info,
    get_fabbricati,
    get_fabbricati_detail,
    get_terreni,
    get_terreno_detail,
    get_titolari_immobile,
    get_persone_fisica,
    get_non_fisica,
    get_soggetti,
    get_toponym,
    get_immobile_by_address,
    get_fabbricati_by_codice,
    get_terreni_by_codice,
)


class TestApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        conn_string = (
            f"postgresql://"
            f"{cnf.POSTGRES_USER}:{cnf.POSTGRES_PASS}"
            f"@{cnf.POSTGRES_HOST}:{cnf.POSTGRES_HOST_PORT}/"
            f"{cnf.POSTGRES_DB}"
        )
        dal.db_init(conn_string)
        populate_db_with_sample_data()

    @classmethod
    def tearDownClass(cls):
        for schema in dal.get_schema_names():
            if schema == "public":
                continue
            for table in dal.get_table_names(schema):
                d = dal.get_table(table_name=table, schema=schema).delete()
                d.execute()

    @classmethod
    def clean_database(cls):
        conn_string = (
            f"postgresql://"
            f"{cnf.POSTGRES_USER}:{cnf.POSTGRES_PASS}"
            f"@{cnf.POSTGRES_HOST}:{cnf.POSTGRES_HOST_PORT}/"
            f"{cnf.POSTGRES_DB}"
        )
        dal.db_init(conn_string)
        for schema in dal.get_schema_names():
            if schema == "public":
                continue
            for table in dal.get_table_names(schema):
                d = dal.get_table(table_name=table, schema=schema).delete()
                d.execute()

    def test_query_city(self):
        result = get_comuni_by_name(cityName="")
        expectedResult = [("H224", "REGGIO DI CALABRIA"), ("H501", "ROMA")]
        self.assertEqual(result, expectedResult)

        result = get_comuni_by_name(cityName="RE")
        expectedResult = [("H224", "REGGIO DI CALABRIA")]
        self.assertEqual(result, expectedResult)

        result = get_comuni_by_name(cityName="RO")
        expectedResult = [("H501", "ROMA")]
        self.assertEqual(result, expectedResult)

        result = get_comuni_by_name(cityName="RE", endDate="1864-12-12")
        expectedResult = []
        self.assertEqual(result, expectedResult)

    def test_query_sezioni(self):
        result = get_sezioni_by_city_code(cityCode="H224")
        expectedResult = [("A",), ("B",), ("C",), ("D",)]
        self.assertEqual(result, expectedResult)

        result = get_sezioni_by_city_code(
            cityCode="H224", endDate="1864-12-12"
        )
        expectedResult = []
        self.assertEqual(result, expectedResult)

    def test_query_foglio(self):
        expectedJson = get_json_from_file("expected_fogli")

        result = get_fogli_by_city_info(cityCode="H224", sectionCode="A")
        expectedResult = []
        for each in expectedJson["general"]:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)

        result = get_fogli_by_city_info(
            cityCode="H224",
            sectionCode="A",
            startDate="0001-01-01",
            endDate=datetime.datetime.today().strftime("%Y-%m-%d"),
        )
        expectedResult = []
        for each in expectedJson["temp"]:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)

    def test_query_fabbricati(self):
        expectedJson = get_json_from_file("expected_fabbricati")

        result = get_fabbricati(
            cityCode="H224", sectionCode="A", sheetCode="2"
        )
        expectedResult = []
        for each in expectedJson["2"]:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)

        result = get_fabbricati(
            cityCode="H224", sectionCode="A", sheetCode="3"
        )
        expectedResult = []
        for each in expectedJson["3"]:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)

        result = get_fabbricati_by_codice(immobileCodice=558, cityCode="H224")
        expectedResult = []
        for each in expectedJson["3"]:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)
        # [TODO] add temporal fab, this requires new data as the data now are all new

    def test_query_fabbricati_detail(self):
        expectedJson = get_json_from_file("expected_fab_detail")

        result = get_fabbricati_detail(
            cityCode="H224", sheetCode="2", number="00001"
        )
        expectedResult = []
        for each in expectedJson["general"]["00001-2"]:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)

        result = get_fabbricati_detail(
            cityCode="H224", sheetCode="3", number="00006"
        )
        expectedResult = []
        for each in expectedJson["general"]["00006-3"]:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)

        result = get_fabbricati_detail(
            cityCode="H224",
            sheetCode="2",
            number="00001",
            startDate="0001-01-01",
            endDate=datetime.datetime.today().strftime("%Y-%m-%d"),
        )
        expectedResult = []
        for each in expectedJson["temp"]["00001-2"]:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)

        result = get_fabbricati_detail(
            cityCode="H224",
            sheetCode="3",
            number="00006",
            startDate="0001-01-01",
            endDate=datetime.datetime.today().strftime("%Y-%m-%d"),
        )
        expectedResult = []
        for each in expectedJson["temp"]["00006-3"]:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)

    def test_query_terreni(self):
        expectedJson = get_json_from_file("expected_terreni")

        result = get_terreni(cityCode="H224", sectionCode="A", sheetCode="2")
        expectedResult = []
        for each in expectedJson["general"]["2"]:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)

        result = get_terreni(cityCode="H224", sectionCode="A", sheetCode="3")
        expectedResult = []
        for each in expectedJson["general"]["3"]:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)

        result = get_terreni_by_codice(cityCode="H224", immobileCodice=735)
        expectedResult = []
        for each in expectedJson["general"]["3"]:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)

        result = get_terreni(
            cityCode="H224",
            sectionCode="A",
            sheetCode="2",
            startDate="0001-01-01",
            endDate=datetime.datetime.today().strftime("%Y-%m-%d"),
        )
        expectedResult = []
        for each in expectedJson["temp"]["2"]:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)

        result = get_terreni(
            cityCode="H224",
            sectionCode="A",
            sheetCode="3",
            startDate="0001-01-01",
            endDate=datetime.datetime.today().strftime("%Y-%m-%d"),
        )
        expectedResult = []
        for each in expectedJson["temp"]["3"]:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)

    def test_query_terreno_detail(self):
        expectedJson = get_json_from_file("expected_ter_detail")

        result = get_terreno_detail(
            cityCode="H224", sheetCode="2", number="00001"
        )
        expectedResult = []
        for each in expectedJson["general"]["00001-2"]:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)

        result = get_terreno_detail(
            cityCode="H224", sheetCode="2", number="00006"
        )
        expectedResult = []
        for each in expectedJson["general"]["00006-2"]:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)

        result = get_terreno_detail(
            cityCode="H224", sheetCode="2", number="00007"
        )
        expectedResult = []
        for each in expectedJson["general"]["00007-2"]:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)

        result = get_terreno_detail(
            cityCode="H224",
            sheetCode="2",
            number="00001",
            startDate="0001-01-01",
            endDate=datetime.datetime.today().strftime("%Y-%m-%d"),
        )
        expectedResult = []
        for each in expectedJson["temp"]["00001-2"]:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)

        result = get_terreno_detail(
            cityCode="H224",
            sheetCode="2",
            number="00004",
            startDate="0001-01-01",
            endDate=datetime.datetime.today().strftime("%Y-%m-%d"),
        )
        expectedResult = []
        for each in expectedJson["temp"]["00004-2"]:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)

        result = get_terreno_detail(
            cityCode="H224",
            sheetCode="2",
            number="00005",
            startDate="0001-01-01",
            endDate=datetime.datetime.today().strftime("%Y-%m-%d"),
        )
        expectedResult = []
        for each in expectedJson["temp"]["00005-2"]:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)

        result = get_terreno_detail(
            cityCode="H224",
            sheetCode="2",
            number="00006",
            startDate="0001-01-01",
            endDate=datetime.datetime.today().strftime("%Y-%m-%d"),
        )
        expectedResult = []
        for each in expectedJson["temp"]["00006-2"]:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)

        result = get_terreno_detail(
            cityCode="H224",
            sheetCode="2",
            number="00007",
            startDate="0001-01-01",
            endDate=datetime.datetime.today().strftime("%Y-%m-%d"),
        )
        expectedResult = []
        for each in expectedJson["temp"]["00007-2"]:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)

        result = get_terreno_detail(
            cityCode="H224",
            sheetCode="3",
            number="00007",
            startDate="0001-01-01",
            endDate=datetime.datetime.today().strftime("%Y-%m-%d"),
        )
        expectedResult = []
        for each in expectedJson["temp"]["00007-3"]:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)

    def test_query_titolare_immobile(self):
        # [NOTE] query temporal for all the immobile (some are empty in general)
        expectedJson = get_json_from_file("expected_titolare_immobile")
        for cityCode, property, propertyType in [
            ("H224", 315, "T"),
            ("H224", 318, "T"),
            ("H224", 318, "T"),
            ("H224", 319, "T"),
            ("H224", 320, "T"),
            ("H224", 321, "T"),
            ("H224", 734, "T"),
            ("H224", 335, "F"),
            ("H224", 334, "F"),
            ("H224", 558, "F"),
            ("H224", 559, "F"),
        ]:
            result = get_titolari_immobile(
                cityCode=cityCode,
                property=property,
                propertyType=propertyType,
                startDate="0001-01-01",
                endDate=datetime.datetime.today().strftime("%Y-%m-%d"),
            )
            expectedResult = []
            for each in expectedJson[f"{cityCode}-{property}-{propertyType}"]:
                expectedResult.append(tuple(list(each.values())))
            self.assertEqual(result, expectedResult)

    def test_query_persone_fisica(self):
        expectedJson = get_json_from_file("expected_persone_fisica")
        result = get_persone_fisica(fiscalecode="'AAAAAAAAAAAAAAAA'")
        expectedResult = []
        for each in expectedJson["AAAAAAAAAAAAAAAA"]:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)

        result = get_persone_fisica(lastname="'ALICE'", firstname="'ALICE'")
        expectedResult = []
        for each in expectedJson["AAAAAAAAAAAAAAAA"]:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)

        result = get_persone_fisica(subject="2")
        expectedResult = []
        for each in expectedJson["AAAAAAAAAAAAAAAA"]:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)

        result = get_persone_fisica_with_bday(
            lastname="'ALICE'",
            firstname="'ALICE'",
            birthdate="'1940-08-15'",
            birthplace="H224",
        )
        expectedResult = []
        for each in expectedJson["AAAAAAAAAAAAAAAA"]:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)

        result = get_persone_fisica(fiscalecode="'BBBBBBBBBBBBBBBB'")
        expectedResult = []
        for each in expectedJson["BBBBBBBBBBBBBBBB"]:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)

        result = get_persone_fisica(firstname="'BOB'", lastname="'BOB'")
        expectedResult = []
        for each in expectedJson["BBBBBBBBBBBBBBBB"]:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)

        result = get_persone_fisica(subject="1")
        expectedResult = []
        for each in expectedJson["BBBBBBBBBBBBBBBB"]:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)

    def test_query_non_fisica(self):
        expectedJson = get_json_from_file("expected_non_fisica")
        result = get_non_fisica(vatNumber="'00101010101'")
        expectedResult = []
        for each in expectedJson:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)

        result = get_non_fisica(subject="3")
        expectedResult = []
        for each in expectedJson:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)

        result = get_non_fisica(businessName="'FOO S.R.L'")
        expectedResult = []
        for each in expectedJson:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)

    def test_query_soggetti(self):
        expectedJson = get_json_from_file("expected_soggetti")

        result = get_soggetti(subjects=["1"], subjectType="P")
        expectedResult = []
        for each in expectedJson["general"]["1-P"]:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)

        result = get_soggetti(subjects=["2"], subjectType="P")
        expectedResult = []
        for each in expectedJson["general"]["2-P"]:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)

        result = get_soggetti(subjects=["1", "2"], subjectType="P")
        expectedResult = []
        for each in expectedJson["general"]["1-2-P"]:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)

        result = get_soggetti(subjects=["3"], subjectType="G")
        expectedResult = []
        for each in expectedJson["general"]["3-G"]:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)

        result = get_soggetti(
            subjects=["1"],
            subjectType="P",
            startDate="0001-01-01",
            endDate=datetime.datetime.today().strftime("%Y-%m-%d"),
        )
        expectedResult = []
        for each in expectedJson["temp"]["1-P"]:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)

        result = get_soggetti(
            subjects=["2"],
            subjectType="P",
            startDate="0001-01-01",
            endDate=datetime.datetime.today().strftime("%Y-%m-%d"),
        )
        expectedResult = []
        for each in expectedJson["temp"]["2-P"]:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)

        result = get_soggetti(
            subjects=["1", "2"],
            subjectType="P",
            startDate="0001-01-01",
            endDate=datetime.datetime.today().strftime("%Y-%m-%d"),
        )
        expectedResult = []
        for each in expectedJson["temp"]["1-2-P"]:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)

        result = get_soggetti(
            subjects=["3"],
            subjectType="G",
            startDate="0001-01-01",
            endDate=datetime.datetime.today().strftime("%Y-%m-%d"),
        )
        expectedResult = []
        for each in expectedJson["temp"]["3-G"]:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)

    def test_query_toponym(self):
        expectedJson = get_json_from_file("expected_toponimo")

        result = get_toponym("")
        expectedResult = []
        for each in expectedJson["all"]:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)

        result = get_toponym("VI")
        expectedResult = []
        for each in expectedJson["VI"]:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)

    def test_query_immobile_by_address(self):
        expectedJson = get_json_from_file("expected_immobile_by_address")

        result = get_immobile_by_address(
            toponymCode=236,
            addressName="CRISTOFORO SABBADINO",
            houseNumber="68",
            cityCode="H501",
        )
        expectedResult = []
        for each in expectedJson["general"]:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)

        result = get_immobile_by_address(
            toponymCode=236,
            addressName="CRISTOFORO SABBADINO",
            houseNumber="68",
            cityCode="H501",
            startDate="0001-01-01",
            endDate=datetime.datetime.today().strftime("%Y-%m-%d"),
        )
        expectedResult = []
        for each in expectedJson["general"]:
            expectedResult.append(tuple(list(each.values())))
        self.assertEqual(result, expectedResult)


class GeoServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        conn_string = (
            f"postgresql://"
            f"{cnf.POSTGRES_USER}:{cnf.POSTGRES_PASS}"
            f"@{cnf.POSTGRES_HOST}:{cnf.POSTGRES_HOST_PORT}/"
            f"{cnf.POSTGRES_DB}"
        )
        dal.db_init(conn_string)
        populate_db_with_sample_data()

    @classmethod
    def tearDownClass(cls):
        for schema in dal.get_schema_names():
            if schema == "public":
                continue
            for table in dal.get_table_names(schema):
                d = dal.get_table(table_name=table, schema=schema).delete()
                d.execute()

    def test_geoserver_get_city(self):
        expectedResponses = [
            {"name": "REGGIO DI CALABRIA", "code": "H224"},
            {"name": "ROMA", "code": "H501"},
        ]
        params = {
            "service": "WFS",
            "version": cnf.APP_CONFIG.GS_WFS_VERSION,
            "request": "GetFeature",
            "outputFormat": "application/json",
            "typename": cnf.APP_CONFIG.CATASTO_OPEN_CITY_LAYER,
            "viewparams": "city:R",
        }
        response = requests.get(
            f"{cnf.GEOSERVER_HOST}:"
            f"{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/ows",
            params,
        )
        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.text)
        self.assertEqual(payload["totalFeatures"], len(expectedResponses))
        feature_properties = [
            feature["properties"] for feature in payload["features"]
        ]
        self.assertEqual(feature_properties, expectedResponses)

        expectedResponses = [{"name": "ROMA", "code": "H501"}]
        params = {
            "service": "WFS",
            "version": cnf.APP_CONFIG.GS_WFS_VERSION,
            "request": "GetFeature",
            "outputFormat": "application/json",
            "typename": cnf.APP_CONFIG.CATASTO_OPEN_CITY_LAYER,
            "viewparams": "city:RO",
        }
        response = requests.get(
            f"{cnf.GEOSERVER_HOST}:"
            f"{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/ows",
            params,
        )
        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.text)
        self.assertEqual(payload["totalFeatures"], len(expectedResponses))
        feature_properties = [
            feature["properties"] for feature in payload["features"]
        ]
        self.assertEqual(feature_properties, expectedResponses)

        expectedResponses = [{"name": "REGGIO DI CALABRIA", "code": "H224"}]
        params = {
            "service": "WFS",
            "version": cnf.APP_CONFIG.GS_WFS_VERSION,
            "request": "GetFeature",
            "outputFormat": "application/json",
            "typename": cnf.APP_CONFIG.CATASTO_OPEN_CITY_LAYER_TEMP,
            "viewparams": "city:RE;endDate:{}".format(
                datetime.datetime.today().strftime("%Y-%m-%d")
            ),
        }
        response = requests.get(
            f"{cnf.GEOSERVER_HOST}:"
            f"{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/ows",
            params,
        )
        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.text)
        self.assertEqual(payload["totalFeatures"], len(expectedResponses))
        feature_properties = [
            feature["properties"] for feature in payload["features"]
        ]
        self.assertEqual(feature_properties, expectedResponses)

        expectedResponses = [
            {"name": "REGGIO DI CALABRIA", "code": "H224"},
            {"name": "ROMA", "code": "H501"},
        ]
        params = {
            "service": "WFS",
            "version": cnf.APP_CONFIG.GS_WFS_VERSION,
            "request": "GetFeature",
            "outputFormat": "application/json",
            "typename": cnf.APP_CONFIG.CATASTO_OPEN_CITY_LAYER_TEMP,
            "viewparams": "city:R;endDate:{}".format(
                datetime.datetime.today().strftime("%Y-%m-%d")
            ),
        }
        response = requests.get(
            f"{cnf.GEOSERVER_HOST}:"
            f"{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/ows",
            params,
        )
        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.text)
        self.assertEqual(payload["totalFeatures"], len(expectedResponses))
        feature_properties = [
            feature["properties"] for feature in payload["features"]
        ]
        self.assertEqual(feature_properties, expectedResponses)

    def test_geoserver_get_sezioni(self):
        expectedResponses = [
            {"name": "A"},
            {"name": "B"},
            {"name": "C"},
            {"name": "D"},
        ]
        params = {
            "service": "WFS",
            "version": cnf.APP_CONFIG.GS_WFS_VERSION,
            "request": "GetFeature",
            "outputFormat": "application/json",
            "typename": cnf.APP_CONFIG.CATASTO_OPEN_SECTION_LAYER,
            "viewparams": "cityCode:H224",
        }
        response = requests.get(
            f"{cnf.GEOSERVER_HOST}:"
            f"{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/ows",
            params,
        )
        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.text)
        self.assertEqual(payload["totalFeatures"], len(expectedResponses))
        feature_properties = [
            feature["properties"] for feature in payload["features"]
        ]
        self.assertEqual(feature_properties, expectedResponses)

        expectedResponses = [
            {"name": "A"},
            {"name": "B"},
            {"name": "C"},
            {"name": "D"},
        ]
        params = {
            "service": "WFS",
            "version": cnf.APP_CONFIG.GS_WFS_VERSION,
            "request": "GetFeature",
            "outputFormat": "application/json",
            "typename": cnf.APP_CONFIG.CATASTO_OPEN_SECTION_LAYER_TEMP,
            "viewparams": "cityCode:H224;endDate:{}".format(
                datetime.datetime.today().strftime("%Y-%m-%d")
            ),
        }
        response = requests.get(
            f"{cnf.GEOSERVER_HOST}:"
            f"{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/ows",
            params,
        )
        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.text)
        self.assertEqual(payload["totalFeatures"], len(expectedResponses))
        feature_properties = [
            feature["properties"] for feature in payload["features"]
        ]
        self.assertEqual(feature_properties, expectedResponses)

    def test_geoserver_get_foglio(self):
        expectedResponses = get_json_from_file("expected_fogli_geoserver")
        params = {
            "service": "WFS",
            "version": cnf.APP_CONFIG.GS_WFS_VERSION,
            "request": "GetFeature",
            "outputFormat": "application/json",
            "typename": cnf.APP_CONFIG.CATASTO_OPEN_SHEET_LAYER,
            "viewparams": "cityCode:H224;sectionCode:A",
        }
        response = requests.get(
            f"{cnf.GEOSERVER_HOST}:"
            f"{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/ows",
            params,
        )
        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.text)
        self.assertEqual(
            payload["totalFeatures"],
            len(expectedResponses["general"]["features"]),
        )
        feature_properties = [
            feature["properties"] for feature in payload["features"]
        ]
        self.assertEqual(
            feature_properties, expectedResponses["general"]["features"]
        )
        bboxes = [feature["bbox"] for feature in payload["features"]]
        self.assertEqual(bboxes, expectedResponses["general"]["bboxes"])

        params = {
            "service": "WFS",
            "version": cnf.APP_CONFIG.GS_WFS_VERSION,
            "request": "GetFeature",
            "outputFormat": "application/json",
            "typename": cnf.APP_CONFIG.CATASTO_OPEN_SHEET_LAYER_TEMP,
            "viewparams": "cityCode:H224;sectionCode:A;startDate:0001-01-01;endDate:{}".format(
                datetime.datetime.today().strftime("%Y-%m-%d")
            ),
        }
        response = requests.get(
            f"{cnf.GEOSERVER_HOST}:"
            f"{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/ows",
            params,
        )
        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.text)
        self.assertEqual(
            payload["totalFeatures"],
            len(expectedResponses["temp"]["features"]),
        )
        feature_properties = [
            feature["properties"] for feature in payload["features"]
        ]
        self.assertEqual(
            feature_properties, expectedResponses["temp"]["features"]
        )
        bboxes = [feature["bbox"] for feature in payload["features"]]
        self.assertEqual(bboxes, expectedResponses["temp"]["bboxes"])

    def test_geoserver_get_terreni(self):
        expectedResponses = get_json_from_file("expected_terreni_geoserver")
        params = {
            "service": "WFS",
            "version": cnf.APP_CONFIG.GS_WFS_VERSION,
            "request": "GetFeature",
            "outputFormat": "application/json",
            "typename": cnf.APP_CONFIG.CATASTO_OPEN_LAND_LAYER,
            "viewparams": "cityCode:H224;sectionCode:A;sheetCode:2",
        }
        response = requests.get(
            f"{cnf.GEOSERVER_HOST}:"
            f"{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/ows",
            params,
        )
        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.text)
        self.assertEqual(
            payload["totalFeatures"], len(expectedResponses["general"])
        )
        feature_properties = [
            feature["properties"] for feature in payload["features"]
        ]
        self.assertEqual(feature_properties, expectedResponses["general"])

        params = {
            "service": "WFS",
            "version": cnf.APP_CONFIG.GS_WFS_VERSION,
            "request": "GetFeature",
            "outputFormat": "application/json",
            "typename": cnf.APP_CONFIG.CATASTO_OPEN_LAND_LAYER_TEMP,
            "viewparams": "cityCode:H224;sectionCode:A;sheetCode:2;startDate:0001-01-01;endDate:{}".format(
                datetime.datetime.today().strftime("%Y-%m-%d")
            ),
        }
        response = requests.get(
            f"{cnf.GEOSERVER_HOST}:"
            f"{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/ows",
            params,
        )
        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.text)
        self.assertEqual(
            payload["totalFeatures"], len(expectedResponses["temp"])
        )
        feature_properties = [
            feature["properties"] for feature in payload["features"]
        ]
        self.assertEqual(feature_properties, expectedResponses["temp"])

    def test_geoserver_get_fabbricati(self):
        expectedResponses = get_json_from_file("expected_fabbricati_geoserver")

        params = {
            "service": "WFS",
            "version": cnf.APP_CONFIG.GS_WFS_VERSION,
            "request": "GetFeature",
            "outputFormat": "application/json",
            "typename": cnf.APP_CONFIG.CATASTO_OPEN_BUILDING_LAYER,
            "viewparams": "cityCode:H224;sectionCode:A;sheetCode:2",
        }
        response = requests.get(
            f"{cnf.GEOSERVER_HOST}:"
            f"{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/ows",
            params,
        )
        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.text)
        self.assertEqual(payload["totalFeatures"], len(expectedResponses))
        feature_properties = [
            feature["properties"] for feature in payload["features"]
        ]
        self.assertEqual(feature_properties, expectedResponses)

        params = {
            "service": "WFS",
            "version": cnf.APP_CONFIG.GS_WFS_VERSION,
            "request": "GetFeature",
            "outputFormat": "application/json",
            "typename": cnf.APP_CONFIG.CATASTO_OPEN_BUILDING_LAYER_TEMP,
            "viewparams": "cityCode:H224;sectionCode:A;sheetCode:2;startDate:0001-01-01;endDate:{}".format(
                datetime.datetime.today().strftime("%Y-%m-%d")
            ),
        }
        response = requests.get(
            f"{cnf.GEOSERVER_HOST}:"
            f"{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/ows",
            params,
        )
        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.text)
        self.assertEqual(payload["totalFeatures"], len(expectedResponses))
        feature_properties = [
            feature["properties"] for feature in payload["features"]
        ]
        self.assertEqual(feature_properties, expectedResponses)

    def test_geoserver_get_terreno_detail(self):
        expectedResponses = get_json_from_file("expected_ter_detail_geoserver")

        params = {
            "service": "WFS",
            "version": cnf.APP_CONFIG.GS_WFS_VERSION,
            "request": "GetFeature",
            "outputFormat": "application/json",
            "typename": cnf.APP_CONFIG.CATASTO_OPEN_LAND_DETAIL_LAYER,
            "viewparams": "cityCode:H224;sheetCode:2;number:00001",
        }
        response = requests.get(
            f"{cnf.GEOSERVER_HOST}:"
            f"{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/ows",
            params,
        )
        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.text)
        self.assertEqual(
            payload["numberReturned"], len(expectedResponses["general"])
        )
        feature_properties = [
            feature["properties"] for feature in payload["features"]
        ]
        from app.tests.fixtures import object_hook

        features = json.loads(
            json.dumps(feature_properties), object_hook=object_hook
        )
        self.assertEqual(features, expectedResponses["general"])

        params = {
            "service": "WFS",
            "version": cnf.APP_CONFIG.GS_WFS_VERSION,
            "request": "GetFeature",
            "outputFormat": "application/json",
            "typename": cnf.APP_CONFIG.CATASTO_OPEN_LAND_DETAIL_LAYER_TEMP,
            "viewparams": "cityCode:H224;sheetCode:2;number:00001;startDate:0001-01-01;endDate:{}".format(
                datetime.datetime.today().strftime("%Y-%m-%d")
            ),
        }
        response = requests.get(
            f"{cnf.GEOSERVER_HOST}:"
            f"{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/ows",
            params,
        )
        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.text)
        self.assertEqual(
            payload["numberReturned"], len(expectedResponses["temp"])
        )
        feature_properties = [
            feature["properties"] for feature in payload["features"]
        ]
        from app.tests.fixtures import object_hook

        features = json.loads(
            json.dumps(feature_properties), object_hook=object_hook
        )
        self.assertEqual(features, expectedResponses["temp"])

    def test_geoserver_get_fabbricati_detail(self):
        expectedResponses = get_json_from_file("expected_fab_detail_geoserver")

        params = {
            "service": "WFS",
            "version": cnf.APP_CONFIG.GS_WFS_VERSION,
            "request": "GetFeature",
            "outputFormat": "application/json",
            "typename": cnf.APP_CONFIG.CATASTO_OPEN_BUILDING_DETAIL_LAYER,
            "viewparams": "cityCode:H224;sheetCode:3;number:00001",
        }
        response = requests.get(
            f"{cnf.GEOSERVER_HOST}:"
            f"{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/ows",
            params,
        )
        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.text)
        self.assertEqual(
            payload["numberReturned"], len(expectedResponses["general"])
        )
        feature_properties = [
            feature["properties"] for feature in payload["features"]
        ]
        from app.tests.fixtures import object_hook

        features = json.loads(
            json.dumps(feature_properties), object_hook=object_hook
        )
        self.assertEqual(features, expectedResponses["general"])

        params = {
            "service": "WFS",
            "version": cnf.APP_CONFIG.GS_WFS_VERSION,
            "request": "GetFeature",
            "outputFormat": "application/json",
            "typename": cnf.APP_CONFIG.CATASTO_OPEN_BUILDING_DETAIL_LAYER_TEMP,
            "viewparams": "cityCode:H224;sheetCode:3;number:00001;startDate:0001-01-01;endDate:{}".format(
                datetime.datetime.today().strftime("%Y-%m-%d")
            ),
        }
        response = requests.get(
            f"{cnf.GEOSERVER_HOST}:"
            f"{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/ows",
            params,
        )
        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.text)
        self.assertEqual(
            payload["numberReturned"], len(expectedResponses["temp"])
        )
        feature_properties = [
            feature["properties"] for feature in payload["features"]
        ]
        from app.tests.fixtures import object_hook

        features = json.loads(
            json.dumps(feature_properties), object_hook=object_hook
        )
        self.assertEqual(features, expectedResponses["temp"])

    def test_geoserver_get_titolare_immobili(self):
        expectedResponses = get_json_from_file(
            "expected_titolare_immobile_geoserver"
        )

        params = {
            "service": "WFS",
            "version": cnf.APP_CONFIG.GS_WFS_VERSION,
            "request": "GetFeature",
            "outputFormat": "application/json",
            "typename": cnf.APP_CONFIG.CATASTO_OPEN_PROPERTY_OWNER_LAYER,
            "viewparams": "cityCode:H224;property:315;propertyType:T",
        }
        response = requests.get(
            f"{cnf.GEOSERVER_HOST}:"
            f"{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/ows",
            params,
        )
        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.text)
        self.assertEqual(payload["numberReturned"], len(expectedResponses))
        feature_properties = [
            feature["properties"] for feature in payload["features"]
        ]
        from app.tests.fixtures import object_hook

        features = json.loads(
            json.dumps(feature_properties, sort_keys=False),
            object_hook=object_hook,
        )
        self.assertEqual(features, expectedResponses)

        params = {
            "service": "WFS",
            "version": cnf.APP_CONFIG.GS_WFS_VERSION,
            "request": "GetFeature",
            "outputFormat": "application/json",
            "typename": cnf.APP_CONFIG.CATASTO_OPEN_PROPERTY_OWNER_LAYER_TEMP,
            "viewparams": "cityCode:H224;property:315;propertyType:T;startDate:0001-01-01;endDate:{}".format(
                datetime.datetime.today().strftime("%Y-%m-%d")
            ),
        }
        response = requests.get(
            f"{cnf.GEOSERVER_HOST}:"
            f"{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/ows",
            params,
        )
        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.text)
        self.assertEqual(payload["numberReturned"], len(expectedResponses))
        feature_properties = [
            feature["properties"] for feature in payload["features"]
        ]
        from app.tests.fixtures import object_hook

        features = json.loads(
            json.dumps(feature_properties, sort_keys=False),
            object_hook=object_hook,
        )
        self.assertEqual(features, expectedResponses)

    def test_geoserver_get_persone_fisica(self):
        expectedResponses = get_json_from_file("expected_pfisica_geoserver")
        params = {
            "service": "WFS",
            "version": cnf.APP_CONFIG.GS_WFS_VERSION,
            "request": "GetFeature",
            "outputFormat": "application/json",
            "typename": cnf.APP_CONFIG.CATASTO_OPEN_NATURAL_SUBJECT_LAYER,
            "viewparams": "fiscalCode:'AAAAAAAAAAAAAAAA'",
        }
        response = requests.get(
            f"{cnf.GEOSERVER_HOST}:"
            f"{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/ows",
            params,
        )
        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.text)
        self.assertEqual(payload["totalFeatures"], len(expectedResponses))
        feature_properties = [
            feature["properties"] for feature in payload["features"]
        ]
        from app.tests.fixtures import object_hook

        features = json.loads(
            json.dumps(feature_properties, sort_keys=False),
            object_hook=object_hook,
        )
        self.assertEqual(features, expectedResponses)

        params = {
            "service": "WFS",
            "version": cnf.APP_CONFIG.GS_WFS_VERSION,
            "request": "GetFeature",
            "outputFormat": "application/json",
            "typename": cnf.APP_CONFIG.CATASTO_OPEN_NATURAL_SUBJECT_LAYER,
            "viewparams": "subjectCode:2",
        }
        response = requests.get(
            f"{cnf.GEOSERVER_HOST}:"
            f"{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/ows",
            params,
        )
        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.text)
        self.assertEqual(payload["totalFeatures"], len(expectedResponses))
        feature_properties = [
            feature["properties"] for feature in payload["features"]
        ]
        from app.tests.fixtures import object_hook

        features = json.loads(
            json.dumps(feature_properties, sort_keys=False),
            object_hook=object_hook,
        )
        self.assertEqual(features, expectedResponses)

        params = {
            "service": "WFS",
            "version": cnf.APP_CONFIG.GS_WFS_VERSION,
            "request": "GetFeature",
            "outputFormat": "application/json",
            "typename": cnf.APP_CONFIG.CATASTO_OPEN_NATURAL_SUBJECT_LAYER,
            "viewparams": "lastName:'ALICE';firstName:'ALICE'",
        }
        response = requests.get(
            f"{cnf.GEOSERVER_HOST}:"
            f"{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/ows",
            params,
        )
        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.text)
        self.assertEqual(payload["totalFeatures"], len(expectedResponses))
        feature_properties = [
            feature["properties"] for feature in payload["features"]
        ]
        from app.tests.fixtures import object_hook

        features = json.loads(
            json.dumps(feature_properties, sort_keys=False),
            object_hook=object_hook,
        )
        self.assertEqual(features, expectedResponses)

        params = {
            "service": "WFS",
            "version": cnf.APP_CONFIG.GS_WFS_VERSION,
            "request": "GetFeature",
            "outputFormat": "application/json",
            "typename": cnf.APP_CONFIG.CATASTO_OPEN_NATURAL_SUBJECT_LAYER_WBOTH,
            "viewparams": "lastName:'ALICE';firstName:'ALICE';birthDate:'1940-08-15';birthPlace:H224",
        }
        response = requests.get(
            f"{cnf.GEOSERVER_HOST}:"
            f"{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/ows",
            params,
        )
        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.text)
        self.assertEqual(payload["totalFeatures"], len(expectedResponses))
        feature_properties = [
            feature["properties"] for feature in payload["features"]
        ]
        from app.tests.fixtures import object_hook

        features = json.loads(
            json.dumps(feature_properties, sort_keys=False),
            object_hook=object_hook,
        )
        self.assertEqual(features, expectedResponses)

    def test_geoserver_get_non_fisica(self):
        expectedResponses = get_json_from_file("expected_non_fisica_geoserver")
        params = {
            "service": "WFS",
            "version": cnf.APP_CONFIG.GS_WFS_VERSION,
            "request": "GetFeature",
            "outputFormat": "application/json",
            "typename": cnf.APP_CONFIG.CATASTO_OPEN_LEGAL_SUBJECT_LAYER,
            "viewparams": "vatNumber:'00101010101';",
        }
        response = requests.get(
            f"{cnf.GEOSERVER_HOST}:"
            f"{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/ows",
            params,
        )
        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.text)
        self.assertEqual(payload["totalFeatures"], len(expectedResponses))
        feature_properties = [
            feature["properties"] for feature in payload["features"]
        ]
        self.assertEqual(feature_properties, expectedResponses)

        params = {
            "service": "WFS",
            "version": cnf.APP_CONFIG.GS_WFS_VERSION,
            "request": "GetFeature",
            "outputFormat": "application/json",
            "typename": cnf.APP_CONFIG.CATASTO_OPEN_LEGAL_SUBJECT_LAYER,
            "viewparams": "businessName:'FOO S.R.L'",
        }
        response = requests.get(
            f"{cnf.GEOSERVER_HOST}:"
            f"{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/ows",
            params,
        )
        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.text)
        self.assertEqual(payload["totalFeatures"], len(expectedResponses))
        feature_properties = [
            feature["properties"] for feature in payload["features"]
        ]
        self.assertEqual(feature_properties, expectedResponses)

        params = {
            "service": "WFS",
            "version": cnf.APP_CONFIG.GS_WFS_VERSION,
            "request": "GetFeature",
            "outputFormat": "application/json",
            "typename": cnf.APP_CONFIG.CATASTO_OPEN_LEGAL_SUBJECT_LAYER,
            "viewparams": "subjectCode:3",
        }
        response = requests.get(
            f"{cnf.GEOSERVER_HOST}:"
            f"{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/ows",
            params,
        )
        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.text)
        self.assertEqual(payload["totalFeatures"], len(expectedResponses))
        feature_properties = [
            feature["properties"] for feature in payload["features"]
        ]
        self.assertEqual(feature_properties, expectedResponses)

    def test_geoserver_soggetti(self):
        expectedResponses = get_json_from_file("expected_soggetti_geoserver")

        params = {
            "service": "WFS",
            "version": cnf.APP_CONFIG.GS_WFS_VERSION,
            "request": "GetFeature",
            "outputFormat": "application/json",
            "typename": cnf.APP_CONFIG.CATASTO_OPEN_SUBJECT_PROPERTY_LAYER,
            "viewparams": "subjects:{0};subjectType:P".format("1\\,2"),
        }
        response = requests.get(
            f"{cnf.GEOSERVER_HOST}:"
            f"{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/ows",
            params,
        )
        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.text)
        self.assertEqual(
            payload["totalFeatures"], len(expectedResponses["general"])
        )
        feature_properties = [
            feature["properties"] for feature in payload["features"]
        ]
        from app.tests.fixtures import object_hook

        features = json.loads(
            json.dumps(feature_properties, sort_keys=False),
            object_hook=object_hook,
        )
        self.assertEqual(features, expectedResponses["general"])

        params = {
            "service": "WFS",
            "version": cnf.APP_CONFIG.GS_WFS_VERSION,
            "request": "GetFeature",
            "outputFormat": "application/json",
            "typename": cnf.APP_CONFIG.CATASTO_OPEN_SUBJECT_PROPERTY_LAYER_TEMP,
            "viewparams": "subjects:{0};subjectType:P;startDate:0001-01-01;endDate:{1}".format(
                "1\\,2", datetime.datetime.today().strftime("%Y-%m-%d")
            ),
        }
        response = requests.get(
            f"{cnf.GEOSERVER_HOST}:"
            f"{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/ows",
            params,
        )
        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.text)
        feature_properties = [
            feature["properties"] for feature in payload["features"]
        ]
        from app.tests.fixtures import object_hook

        features = json.loads(
            json.dumps(feature_properties, sort_keys=False),
            object_hook=object_hook,
        )
        self.assertEqual(features, expectedResponses["temp"])

    def test_geoserver_toponym(self):
        expectedResponses = get_json_from_file("expected_toponimo")

        params = {
            "service": "WFS",
            "version": cnf.APP_CONFIG.GS_WFS_VERSION,
            "request": "GetFeature",
            "outputFormat": "application/json",
            "typename": cnf.APP_CONFIG.CATASTO_OPEN_TOPONIMO_LAYER,
        }
        response = requests.get(
            f"{cnf.GEOSERVER_HOST}:"
            f"{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/ows",
            params,
        )
        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.text)
        self.assertEqual(
            payload["totalFeatures"], len(expectedResponses["all"])
        )
        feature_properties = [
            feature["properties"] for feature in payload["features"]
        ]

        from app.tests.fixtures import object_hook

        features = json.loads(
            json.dumps(feature_properties, sort_keys=False),
            object_hook=object_hook,
        )
        self.assertEqual(features, expectedResponses["all"])

        params = {
            "service": "WFS",
            "version": cnf.APP_CONFIG.GS_WFS_VERSION,
            "request": "GetFeature",
            "outputFormat": "application/json",
            "typename": cnf.APP_CONFIG.CATASTO_OPEN_TOPONIMO_LAYER,
            "viewparams": "toponym:VI",
        }
        response = requests.get(
            f"{cnf.GEOSERVER_HOST}:"
            f"{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/ows",
            params,
        )
        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.text)
        self.assertEqual(
            payload["totalFeatures"], len(expectedResponses["VI"])
        )
        feature_properties = [
            feature["properties"] for feature in payload["features"]
        ]

        from app.tests.fixtures import object_hook

        features = json.loads(
            json.dumps(feature_properties, sort_keys=False),
            object_hook=object_hook,
        )
        self.assertEqual(features, expectedResponses["VI"])

    def test_geoserver_immobile_by_address(self):
        expectedResponses = get_json_from_file(
            "expected_immobile_by_address_geoserver"
        )

        params = {
            "service": "WFS",
            "version": cnf.APP_CONFIG.GS_WFS_VERSION,
            "request": "GetFeature",
            "outputFormat": "application/json",
            "typename": cnf.APP_CONFIG.CATASTO_OPEN_INDIRIZZO_IMMOBILE_LAYER,
            "viewparams": "toponymCode:236;addressName:CRISTOFORO SABBADINO;houseNumber:68;cityCode:H501",
        }
        response = requests.get(
            f"{cnf.GEOSERVER_HOST}:"
            f"{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/ows",
            params,
        )
        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.text)
        self.assertEqual(
            payload["totalFeatures"], len(expectedResponses["general"])
        )
        feature_properties = [
            feature["properties"] for feature in payload["features"]
        ]

        from app.tests.fixtures import object_hook

        features = json.loads(
            json.dumps(feature_properties, sort_keys=False),
            object_hook=object_hook,
        )
        self.assertEqual(features, expectedResponses["general"])


class TemporalGeoServer(unittest.TestCase):
    START_DATE = "2022-06-01"
    END_DATE = "2022-06-30"
    expectedCity = "REGGIO DI CALABRIA"
    expectedCode = "H224"

    def __ask_geoserver(self, layer, view_params):
        params = {
            "service": "WFS",
            "version": cnf.APP_CONFIG.GS_WFS_VERSION,
            "request": "GetFeature",
            "outputFormat": "application/json",
            "typename": layer,
            "viewparams": view_params,
        }
        response = requests.get(
            f"{cnf.GEOSERVER_HOST}:"
            f"{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/ows",
            params,
        )
        assert response.status_code == 200
        payload = json.loads(response.text)
        return [feature["properties"] for feature in payload["features"]]

    def __assertTemporal(self, startDate, endDate):
        st = datetime.datetime.strptime(startDate, "%Y-%m-%d")
        ed = datetime.datetime.strptime(endDate, "%Y-%m-%d")
        rst = datetime.datetime.strptime(self.START_DATE, "%Y-%m-%d")
        red = datetime.datetime.strptime(self.END_DATE, "%Y-%m-%d")
        late_start = max(st, rst)
        early_end = min(ed, red)
        self.assertTrue(late_start <= early_end)

    @classmethod
    def setUpClass(cls):
        conn_string = (
            f"postgresql://"
            f"{cnf.POSTGRES_USER}:{cnf.POSTGRES_PASS}"
            f"@{cnf.POSTGRES_HOST}:{cnf.POSTGRES_HOST_PORT}/"
            f"{cnf.POSTGRES_DB}"
        )
        dal.db_init(conn_string)
        populate_db_with_sample_data()

    @classmethod
    def tearDownClass(cls):
        for schema in dal.get_schema_names():
            if schema == "public":
                continue
            for table in dal.get_table_names(schema):
                d = dal.get_table(table_name=table, schema=schema).delete()
                d.execute()

    def test_ricerca_per_immobili(self):
        view_params = f"city:RE;endDate:{self.END_DATE}"
        cities_ret = self.__ask_geoserver(
            layer=cnf.APP_CONFIG.CATASTO_OPEN_CITY_LAYER_TEMP,
            view_params=view_params,
        )
        cities = list(map(lambda x: x["name"], cities_ret))
        codes = list(map(lambda x: x["code"], cities_ret))
        self.assertTrue(self.expectedCity in cities)
        self.assertTrue(self.expectedCode in codes)

        sec_params = f"cityCode:{self.expectedCode};endDate:{self.END_DATE}"
        sections_ret = self.__ask_geoserver(
            layer=cnf.APP_CONFIG.CATASTO_OPEN_SECTION_LAYER_TEMP,
            view_params=sec_params,
        )
        sections_names = list(map(lambda x: x["name"], sections_ret))
        self.assertTrue("A" in sections_names)

        sheet_params = f"cityCode:{self.expectedCode};sectionCode:A;startDate:{self.START_DATE};endDate:{self.END_DATE};"
        sheets_ret = self.__ask_geoserver(
            layer=cnf.APP_CONFIG.CATASTO_OPEN_SHEET_LAYER_TEMP,
            view_params=sheet_params,
        )
        self.assertTrue(len(sheets_ret) != 0)

        for each_sheet in sheets_ret:
            foglio = each_sheet["number"]
            ter_params = f"cityCode:H224;sectionCode:A;sheetCode:{foglio};startDate:{self.START_DATE};endDate:{self.END_DATE};"
            terreni_ret = self.__ask_geoserver(
                layer=cnf.APP_CONFIG.CATASTO_OPEN_LAND_LAYER_TEMP,
                view_params=ter_params,
            )
            for feat in terreni_ret:
                view_p = f"cityCode:{feat['citycode']};sheetCode:{feat['sheet']};number:{feat['number']};startDate:{self.START_DATE};endDate:{self.END_DATE};"
                ter_detail = self.__ask_geoserver(
                    layer=cnf.APP_CONFIG.CATASTO_OPEN_LAND_DETAIL_LAYER_TEMP,
                    view_params=view_p,
                )
                self.__assertTemporal(
                    startDate=ter_detail[0]["startdate"],
                    endDate=ter_detail[0]["enddate"],
                )
                view_pp = f"cityCode:{feat['citycode']};property:{ter_detail[0]['property']};propertyType:{ter_detail[0]['propertytype']};startDate:{self.START_DATE};endDate:{self.END_DATE};"
                properties = self.__ask_geoserver(
                    layer=cnf.APP_CONFIG.CATASTO_OPEN_PROPERTY_OWNER_LAYER_TEMP,
                    view_params=view_pp,
                )
                self.__assertTemporal(
                    startDate=properties[0]["startdate"],
                    endDate=properties[0]["enddate"],
                )

            fab_params = f"cityCode:H224;sectionCode:A;sheetCode:{foglio};startDate:{self.START_DATE};endDate:{self.END_DATE};"
            fabbricati_ret = self.__ask_geoserver(
                layer=cnf.APP_CONFIG.CATASTO_OPEN_BUILDING_LAYER_TEMP,
                view_params=fab_params,
            )
            for feat in fabbricati_ret:
                view_p = f"cityCode:{feat['citycode']};sheetCode:{feat['sheet']};number:{feat['number']};startDate:{self.START_DATE};endDate:{self.END_DATE};"
                ter_detail = self.__ask_geoserver(
                    layer=cnf.APP_CONFIG.CATASTO_OPEN_BUILDING_DETAIL_LAYER_TEMP,
                    view_params=view_p,
                )
                self.__assertTemporal(
                    startDate=ter_detail[0]["startdate"],
                    endDate=ter_detail[0]["enddate"],
                )
                view_pp = f"cityCode:{feat['citycode']};property:{ter_detail[0]['property']};propertyType:{ter_detail[0]['propertytype']};startDate:{self.START_DATE};endDate:{self.END_DATE};"
                properties = self.__ask_geoserver(
                    layer=cnf.APP_CONFIG.CATASTO_OPEN_PROPERTY_OWNER_LAYER_TEMP,
                    view_params=view_pp,
                )
                self.__assertTemporal(
                    startDate=properties[0]["startdate"],
                    endDate=properties[0]["enddate"],
                )

    def test_ricerca_persone_fisica(self):
        view_params = "lastName:'BOB';firstName:'BOB'"
        persona = self.__ask_geoserver(
            layer=cnf.APP_CONFIG.CATASTO_OPEN_NATURAL_SUBJECT_LAYER,
            view_params=view_params,
        )
        view_p = f"subjects:{persona[0]['subjects']};subjectType:{persona[0]['subjecttype']};startDate:{self.START_DATE};endDate:{self.END_DATE};"
        subjects_owned = self.__ask_geoserver(
            layer=cnf.APP_CONFIG.CATASTO_OPEN_SUBJECT_PROPERTY_LAYER_TEMP,
            view_params=view_p,
        )
        for stuff in subjects_owned:
            self.__assertTemporal(
                startDate=stuff["startdate"], endDate=stuff["enddate"]
            )

    def test_ricerca_persone_giuridiche(self):
        view_params = "vatNumber:'00101010101';"
        persona = self.__ask_geoserver(
            layer=cnf.APP_CONFIG.CATASTO_OPEN_LEGAL_SUBJECT_LAYER,
            view_params=view_params,
        )
        view_p = f"subjects:{persona[0]['subjects']};subjectType:{persona[0]['subjecttype']};startDate:{self.START_DATE};endDate:{self.END_DATE};"
        subjects_owned = self.__ask_geoserver(
            layer=cnf.APP_CONFIG.CATASTO_OPEN_SUBJECT_PROPERTY_LAYER_TEMP,
            view_params=view_p,
        )
        for stuff in subjects_owned:
            self.__assertTemporal(
                startDate=stuff["startdate"], endDate=stuff["enddate"]
            )
