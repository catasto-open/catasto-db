import datetime
import json
import unittest

import requests
from sqlalchemy import text

from app.configs import cnf
from app.utils.db import dal
from app.tests.fixtures import prep_db
import geoalchemy2  # noqa

from app.tests.queries import (
    get_city_by_name,
    get_section_by_city_code,
    get_sheet_by_city_code,
    get_building_by_city_code_and_sheet_code,
    get_land_by_city_code_and_sheet_code,
    get_land_details,
    get_building_details,
    get_property_by_subject,
    get_subject_by_property,
    get_natural_subject,
    get_legal_subject,
    get_cttitola,
    get_cuindiri,
    get_cuutilit,
    get_cuidenti,
    get_cuarcuiu,
    get_curiserv,
    get_ctpartic,
    get_ctdeduzi,
    get_ctporzio,
    get_metadata,
    get_waters,
    get_trusts,
    get_dress_lines,
    get_texts,
    get_symbols,
    get_streets,
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
        prep_db()

    @classmethod
    def tearDownClass(cls):
        for schema in dal.get_schema_names():
            if schema == "public":
                continue
            for table in dal.get_table_names(schema):
                d = dal.get_table(table_name=table, schema=schema).delete()
                d.execute()

    def test_city_by_blank_name(self):
        results = get_city_by_name("")
        expected_results = [("RIETI", "H282"), ("ROMA", "H501")]
        self.assertEqual(results, expected_results)

    def test_city_by_name(self):
        results = get_city_by_name("Ro")
        expected_results = [("ROMA", "H501")]
        self.assertEqual(results, expected_results)

    def test_section_by_city_code(self):
        results = get_section_by_city_code("H501")
        expected_results = [("A",), ("B",), ("C",), ("D",)]
        self.assertEqual(results, expected_results)

    def test_sheet_by_city_code(self):
        results = get_sheet_by_city_code("H501")
        expected_results = [
            (
                "H501",
                "A",
                "130",
                130,
                "0103000020110F00000100000005000000C79E4D8AD8343541C0"
                "11BE3C32A953412FA8A7E2B3343541F0B0005A6BAA5341BCF65D"
                "D43F373541ADE7FD2670AA5341C1763A6664373541F336360937"
                "A95341C79E4D8AD8343541C011BE3C32A95341",
                "0103000020110F000001000000050000002FA8A7E2B3343541C0"
                "11BE3C32A953412FA8A7E2B3343541ADE7FD2670AA5341C1763A"
                "6664373541ADE7FD2670AA5341C1763A6664373541C011BE3C32"
                "A953412FA8A7E2B3343541C011BE3C32A95341",
            ),
            (
                "H501",
                "D",
                "172",
                172,
                "0103000020110F00000100000005000000FD4FFC7476E734417C"
                "7881BB37AA5341F336FC632CE734415C16156986AC53418532E5"
                "A7FEF33441EC7DE030A0AC53410A0BFEE947F43441DA2A097E51"
                "AA5341FD4FFC7476E734417C7881BB37AA5341",
                "0103000020110F00000100000005000000F336FC632CE734417C"
                "7881BB37AA5341F336FC632CE73441EC7DE030A0AC53410A0BFE"
                "E947F43441EC7DE030A0AC53410A0BFEE947F434417C7881BB37"
                "AA5341F336FC632CE734417C7881BB37AA5341",
            ),
            (
                "H501",
                "A",
                "233",
                233,
                "0103000020110F000001000000050000001D072196912A35411C"
                "8A592E1DA853419A8DE4AC782A354171FBDA08F0A853417A750B"
                "01292F35412A2829F2F8A853411FF945CF412F3541BF5A011726"
                "A853411D072196912A35411C8A592E1DA85341",
                "0103000020110F000001000000050000009A8DE4AC782A35411C"
                "8A592E1DA853419A8DE4AC782A35412A2829F2F8A853411FF945"
                "CF412F35412A2829F2F8A853411FF945CF412F35411C8A592E1D"
                "A853419A8DE4AC782A35411C8A592E1DA85341",
            ),
            (
                "H501",
                "C",
                "1022",
                1022,
                "0103000020110F000001000000050000008AE03B12FB7D3541BB"
                "3CBC08689D5341729EDB3DD77D35410A531692B09E534157E106"
                "79B5863541C5F16918C09E5341AA08E7FDD886354148134C8D77"
                "9D53418AE03B12FB7D3541BB3CBC08689D5341",
                "0103000020110F00000100000005000000729EDB3DD77D3541BB"
                "3CBC08689D5341729EDB3DD77D3541C5F16918C09E5341AA08E7"
                "FDD8863541C5F16918C09E5341AA08E7FDD8863541BB3CBC0868"
                "9D5341729EDB3DD77D3541BB3CBC08689D5341",
            ),
            (
                "H501",
                "B",
                "1093",
                1093,
                "0103000020110F000001000000050000000D902E594FCF3441E6"
                "6F2CCFA58953418710ECE53FCF3441D9955D161F8A53419B743D"
                "9CA1D23441C8B7D105268A534163835804B1D23441B0FA55BEAC"
                "8953410D902E594FCF3441E66F2CCFA5895341",
                "0103000020110F000001000000050000008710ECE53FCF3441E6"
                "6F2CCFA58953418710ECE53FCF3441C8B7D105268A5341638358"
                "04B1D23441C8B7D105268A534163835804B1D23441E66F2CCFA5"
                "8953418710ECE53FCF3441E66F2CCFA5895341",
            ),
        ]
        self.assertEqual(results, expected_results)

    def test_building_by_city_code_and_sheet_code(self):
        results = get_building_by_city_code_and_sheet_code("H501", "130")
        expected_results = [
            (
                "H501",
                "A",
                "130",
                "00164",
                "0103000020110F000001000000050000006F2AD9CF5535354149"
                "29B7F064A953417FAB379855353541CE5E32CC66A9534187B61BC"
                "961353541562330E366A953411B97BC00623535410FEAB40765A9"
                "53416F2AD9CF553535414929B7F064A95341",
                "0103000020110F000001000000050000007FAB37985535354149"
                "29B7F064A953417FAB379855353541562330E366A953411B97BC"
                "0062353541562330E366A953411B97BC00623535414929B7F064"
                "A953417FAB3798553535414929B7F064A95341",
            )
        ]

        self.assertEqual(results, expected_results)

    def test_land_by_city_code_and_sheet_code(self):
        results = get_land_by_city_code_and_sheet_code("H501", "130")
        expected_results = [
            (
                "H501",
                "A",
                130,
                "00150",
                "0103000020110F00000100000005000000AAB7D296D635354150"
                "1F051482AA5341591BDA63D53535413D0889548CAA5341DF06FC"
                "6AFD3535411C7DFF9F8CAA5341656CE99DFE353541AD4F7B5F82"
                "AA5341AAB7D296D6353541501F051482AA5341",
                "0103000020110F00000100000005000000591BDA63D535354150"
                "1F051482AA5341591BDA63D53535411C7DFF9F8CAA5341656CE9"
                "9DFE3535411C7DFF9F8CAA5341656CE99DFE353541501F051482"
                "AA5341591BDA63D5353541501F051482AA5341",
            )
        ]
        self.assertEqual(results, expected_results)

    def test_land_details(self):
        results = get_land_details("H501", "130", "00150")
        expected_results = [
            (2598, "T", None, "FABB RURALE", "", 0, 3, 67, "103625", "0", "0")
        ]
        self.assertEqual(results, expected_results)

    def test_building_details(self):
        results = get_building_details("H501", "130", "00164")
        expected_results = [
            (None, 68609, "F", "6", "C/6", "14", "40 mq", "218,98", "2409126")
        ]
        self.assertEqual(results, expected_results)

    def test_property_by_subject(self):
        results = get_property_by_subject(234428, "P")
        expected_results = [
            (
                "H501",
                "A",
                "233",
                "205",
                "0103000020110F00000100000005000000A868B859DB2C3541C1"
                "CD72F57EA85341438B3C3CDA2C3541860DFC6A88A853416B2451"
                "1FF52C35414D05149E88A85341260FC63CF62C3541B99A8A287F"
                "A85341A868B859DB2C3541C1CD72F57EA85341",
                "0103000020110F00000100000005000000438B3C3CDA2C3541C1"
                "CD72F57EA85341438B3C3CDA2C35414D05149E88A85341260FC6"
                "3CF62C35414D05149E88A85341260FC63CF62C3541C1CD72F57E"
                "A85341438B3C3CDA2C3541C1CD72F57EA85341",
                "ROMA (RM) (H501)",
                "12",
                "Usufrutto",
                "1/2",
                "zona 4, cat. C/6",
                "6",
                "13 mq",
                "93,32",
                "1669321",
                "Fabbricati",
            )
        ]
        self.assertEqual(results, expected_results)

    def test_subject_by_property(self):
        results = get_subject_by_property("H501", 68609, "F")
        expected_results = [
            ("FOO SRL", "00000000000", "ROMA", "Proprieta'", "")
        ]
        self.assertEqual(results, expected_results)

    def test_natural_subject_by_fiscal_code(self):
        results = get_natural_subject(fiscal_code="AAAAAAAAAAAAAAAA")
        expected_results = [
            (
                "234428",
                "P",
                "John",
                "Doe",
                "AAAAAAAAAAAAAAAA",
                datetime.date(1900, 1, 1),
                "ROMA (RM)",
                "Maschio",
            )
        ]
        self.assertEqual(results, expected_results)

    def test_natural_subject_by_full_name(self):
        results = get_natural_subject(first_name="JOHN", last_name="DOE")
        expected_results = [
            (
                "234428",
                "P",
                "John",
                "Doe",
                "AAAAAAAAAAAAAAAA",
                datetime.date(1900, 1, 1),
                "ROMA (RM)",
                "Maschio",
            ),
            (
                "2593",
                "P",
                "John",
                "Doe",
                "BBBBBBBBBBBBBBBB",
                datetime.date(1951, 8, 22),
                "ROMA (RM)",
                "Femmina",
            ),
        ]
        self.assertEqual(results, expected_results)

    def test_legal_subject_by_vat_number(self):
        results = get_legal_subject(vat_number="'00000000000'")
        expected_results = [("290560", "G", "FOO SRL", "00000000000", "ROMA")]
        self.assertEqual(results, expected_results)

    def test_legal_subject_by_business_name(self):
        results = get_legal_subject(business_name="'FOO'")
        expected_results = [
            ("290560", "G", "FOO SRL", "00000000000", "ROMA"),
            ("411567", "G", "FOO SPA", "11111111111", "ROMA"),
            ("41528", "G", "FOO SRLS", "22222222222", "ROMA"),
        ]
        self.assertEqual(results, expected_results)

    def test_gs_get_city_by_name(self):
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
        self.assertEqual(payload["totalFeatures"], 2)
        feature_properties = [
            feature["properties"] for feature in payload["features"]
        ]
        self.assertEqual(
            feature_properties,
            [
                {"name": "RIETI", "code": "H282"},
                {"name": "ROMA", "code": "H501"},
            ],
        )

    def test_gs_get_section_by_city_code(self):
        params = {
            "service": "WFS",
            "version": cnf.APP_CONFIG.GS_WFS_VERSION,
            "request": "GetFeature",
            "outputFormat": "application/json",
            "typename": cnf.APP_CONFIG.CATASTO_OPEN_SECTION_LAYER,
            "viewparams": "cityCode:H501",
        }
        response = requests.get(
            f"{cnf.GEOSERVER_HOST}:"
            f"{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/ows",
            params,
        )
        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.text)
        self.assertEqual(payload["totalFeatures"], 4)
        feature_properties = [
            feature["properties"] for feature in payload["features"]
        ]
        self.assertEqual(
            feature_properties,
            [{"name": "A"}, {"name": "B"}, {"name": "C"}, {"name": "D"}],
        )

    def test_gs_get_sheet_by_city_code(self):
        params = {
            "service": "WFS",
            "version": cnf.APP_CONFIG.GS_WFS_VERSION,
            "request": "GetFeature",
            "outputFormat": "application/json",
            "typename": cnf.APP_CONFIG.CATASTO_OPEN_SHEET_LAYER,
            "viewparams": "cityCode:H501;sectionCode:A",
        }
        response = requests.get(
            f"{cnf.GEOSERVER_HOST}:"
            f"{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/ows",
            params,
        )
        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.text)
        self.assertEqual(payload["totalFeatures"], 2)
        feature_properties = [
            feature["properties"] for feature in payload["features"]
        ]
        self.assertEqual(
            [
                {
                    "citycode": "H501",
                    "section": "A",
                    "sheet": "130",
                    "number": 130,
                    "extent": {
                        "type": "Polygon",
                        "coordinates": [
                            [
                                [1389747.88537074, 5153992.94910091],
                                [1389747.88537074, 5155264.60924713],
                                [1390436.39932959, 5155264.60924713],
                                [1390436.39932959, 5153992.94910091],
                                [1389747.88537074, 5153992.94910091],
                            ]
                        ],
                    },
                },
                {
                    "citycode": "H501",
                    "section": "A",
                    "sheet": "233",
                    "number": 233,
                    "extent": {
                        "type": "Polygon",
                        "coordinates": [
                            [
                                [1387128.67536244, 5152884.72421506],
                                [1387128.67536244, 5153763.78376202],
                                [1388353.80966146, 5153763.78376202],
                                [1388353.80966146, 5152884.72421506],
                                [1387128.67536244, 5152884.72421506],
                            ]
                        ],
                    },
                },
            ],
            feature_properties,
        )
        bboxes = [feature["bbox"] for feature in payload["features"]]
        self.assertEqual(
            [
                [
                    1389747.88537074,
                    5153992.94910091,
                    1390436.39932959,
                    5155264.60924713,
                ],
                [
                    1387128.67536244,
                    5152884.72421506,
                    1388353.80966146,
                    5153763.78376202,
                ],
            ],
            bboxes,
        )

    def test_gs_get_land_by_city_code_and_sheet_number(self):
        params = {
            "service": "WFS",
            "version": cnf.APP_CONFIG.GS_WFS_VERSION,
            "request": "GetFeature",
            "outputFormat": "application/json",
            "typename": cnf.APP_CONFIG.CATASTO_OPEN_LAND_LAYER,
            "viewparams": f"cityCode:H501;sectionCode:A;"
            f"citySheet:130;"
            f"checkDate:"
            f"{datetime.datetime.today().strftime('%Y-%m-%d')}",
        }
        response = requests.get(
            f"{cnf.GEOSERVER_HOST}:"
            f"{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/ows",
            params,
        )
        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.text)
        self.assertEqual(payload["totalFeatures"], 1)
        feature_properties = [
            feature["properties"] for feature in payload["features"]
        ]
        self.assertEqual(
            [
                {
                    "citycode": "H501",
                    "section": "A",
                    "sheet": 130,
                    "number": "00150",
                    "extent": {
                        "type": "Polygon",
                        "coordinates": [
                            [
                                [1390037.3900468, 5155336.31281264],
                                [1390037.3900468, 5155378.49996879],
                                [1390078.61684301, 5155378.49996879],
                                [1390078.61684301, 5155336.31281264],
                                [1390037.3900468, 5155336.31281264],
                            ]
                        ],
                    },
                }
            ],
            feature_properties,
        )

    def test_gs_get_building_by_city_code_and_sheet_number(self):
        params = {
            "service": "WFS",
            "version": cnf.APP_CONFIG.GS_WFS_VERSION,
            "request": "GetFeature",
            "outputFormat": "application/json",
            "typename": cnf.APP_CONFIG.CATASTO_OPEN_BUILDING_LAYER,
            "viewparams": f"cityCode:H501;sectionCode:A;"
            f"citySheet:130;"
            f"checkDate:"
            f"{datetime.datetime.today().strftime('%Y-%m-%d')}",
        }
        response = requests.get(
            f"{cnf.GEOSERVER_HOST}:"
            f"{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/ows",
            params,
        )
        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.text)
        self.assertEqual(payload["totalFeatures"], 1)
        feature_properties = [
            feature["properties"] for feature in payload["features"]
        ]
        self.assertEqual(
            [
                {
                    "citycode": "H501",
                    "section": "A",
                    "sheet": "130",
                    "number": "00164",
                    "extent": {
                        "type": "Polygon",
                        "coordinates": [
                            [
                                [1389909.59459946, 5154195.76117928],
                                [1389909.59459946, 5154203.54981311],
                                [1389922.00287766, 5154203.54981311],
                                [1389922.00287766, 5154195.76117928],
                                [1389909.59459946, 5154195.76117928],
                            ]
                        ],
                    },
                }
            ],
            feature_properties,
        )

    def test_gs_get_natural_subject_by_name(self):
        params = {
            "service": "WFS",
            "version": cnf.APP_CONFIG.GS_WFS_VERSION,
            "request": "GetFeature",
            "outputFormat": "application/json",
            "typename": cnf.APP_CONFIG.CATASTO_OPEN_NATURAL_SUBJECT_LAYER,
            "viewparams": "firstName:'John';lastName:'Doe'",
        }
        response = requests.get(
            f"{cnf.GEOSERVER_HOST}:"
            f"{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/ows",
            params,
        )
        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.text)
        self.assertEqual(payload["totalFeatures"], 2)
        feature_properties = [
            feature["properties"] for feature in payload["features"]
        ]
        self.assertEqual(
            [
                {
                    "subjects": "234428",
                    "subjecttype": "P",
                    "firstname": "John",
                    "lastname": "Doe",
                    "fiscalcode": "AAAAAAAAAAAAAAAA",
                    "dateofbirth": "1900-01-01",
                    "cityofbirth": "ROMA (RM)",
                    "gender": "Maschio",
                },
                {
                    "subjects": "2593",
                    "subjecttype": "P",
                    "firstname": "John",
                    "lastname": "Doe",
                    "fiscalcode": "BBBBBBBBBBBBBBBB",
                    "dateofbirth": "1951-08-22",
                    "cityofbirth": "ROMA (RM)",
                    "gender": "Femmina",
                },
            ],
            feature_properties,
        )

    def test_gs_get_natural_subject_by_fiscal_code(self):
        params = {
            "service": "WFS",
            "version": cnf.APP_CONFIG.GS_WFS_VERSION,
            "request": "GetFeature",
            "outputFormat": "application/json",
            "typename": cnf.APP_CONFIG.CATASTO_OPEN_NATURAL_SUBJECT_LAYER,
            "viewparams": "fiscalCode:'AAAAAAAAAAAAAAAA';",
        }
        response = requests.get(
            f"{cnf.GEOSERVER_HOST}:"
            f"{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/ows",
            params,
        )
        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.text)
        self.assertEqual(payload["totalFeatures"], 1)
        feature_properties = [
            feature["properties"] for feature in payload["features"]
        ]
        self.assertEqual(
            [
                {
                    "subjects": "234428",
                    "subjecttype": "P",
                    "firstname": "John",
                    "lastname": "Doe",
                    "fiscalcode": "AAAAAAAAAAAAAAAA",
                    "dateofbirth": "1900-01-01",
                    "cityofbirth": "ROMA (RM)",
                    "gender": "Maschio",
                }
            ],
            feature_properties,
        )

    def test_gs_get_legal_subject_by_vat_number(self):
        params = {
            "service": "WFS",
            "version": cnf.APP_CONFIG.GS_WFS_VERSION,
            "request": "GetFeature",
            "outputFormat": "application/json",
            "typename": cnf.APP_CONFIG.CATASTO_OPEN_LEGAL_SUBJECT_LAYER,
            "viewparams": "vatNumber:'00000000000';",
        }
        response = requests.get(
            f"{cnf.GEOSERVER_HOST}:"
            f"{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/ows",
            params,
        )
        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.text)
        self.assertEqual(payload["totalFeatures"], 1)
        feature_properties = [
            feature["properties"] for feature in payload["features"]
        ]
        self.assertEqual(
            [
                {
                    "subjects": "290560",
                    "subjecttype": "G",
                    "businessname": "FOO SRL",
                    "vatnumber": "00000000000",
                    "branch": "ROMA",
                }
            ],
            feature_properties,
        )

    def test_gs_get_legal_subject_by_business_name(self):
        params = {
            "service": "WFS",
            "version": cnf.APP_CONFIG.GS_WFS_VERSION,
            "request": "GetFeature",
            "outputFormat": "application/json",
            "typename": cnf.APP_CONFIG.CATASTO_OPEN_LEGAL_SUBJECT_LAYER,
            "viewparams": "businessName:'Foo';",
        }
        response = requests.get(
            f"{cnf.GEOSERVER_HOST}:"
            f"{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/ows",
            params,
        )
        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.text)
        self.assertEqual(payload["totalFeatures"], 3)
        feature_properties = [
            feature["properties"] for feature in payload["features"]
        ]
        self.assertEqual(
            [
                {
                    "subjects": "290560",
                    "subjecttype": "G",
                    "businessname": "FOO SRL",
                    "vatnumber": "00000000000",
                    "branch": "ROMA",
                },
                {
                    "subjects": "411567",
                    "subjecttype": "G",
                    "businessname": "FOO SPA",
                    "vatnumber": "11111111111",
                    "branch": "ROMA",
                },
                {
                    "subjects": "41528",
                    "subjecttype": "G",
                    "businessname": "FOO SRLS",
                    "vatnumber": "22222222222",
                    "branch": "ROMA",
                },
            ],
            feature_properties,
        )

    def test_gs_get_property_by_subject(self):
        params = {
            "service": "WFS",
            "version": cnf.APP_CONFIG.GS_WFS_VERSION,
            "request": "GetFeature",
            "outputFormat": "application/json",
            "typename": cnf.APP_CONFIG.CATASTO_OPEN_SUBJECT_PROPERTY_LAYER,
            "viewparams": "subjects:234428;subjectType:P",
        }
        response = requests.get(
            f"{cnf.GEOSERVER_HOST}:"
            f"{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/ows",
            params,
        )
        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.text)
        self.assertEqual(payload["totalFeatures"], 1)
        feature_properties = [
            feature["properties"] for feature in payload["features"]
        ]
        self.assertEqual(
            [
                {
                    "citycode": "H501",
                    "section": "A",
                    "sheet": "233",
                    "number": "205",
                    "extent": {
                        "type": "Polygon",
                        "coordinates": [
                            [
                                [1387738.23529883, 5153275.83513206],
                                [1387738.23529883, 5153314.46997197],
                                [1387766.23739714, 5153314.46997197],
                                [1387766.23739714, 5153275.83513206],
                                [1387738.23529883, 5153275.83513206],
                            ]
                        ],
                    },
                    "city": "ROMA (RM) (H501)",
                    "subordinate": "12",
                    "right": "Usufrutto",
                    "part": "1/2",
                    "classification": "zona 4, cat. C/6",
                    "class": "6",
                    "consistency": "13 mq",
                    "income": "93,32",
                    "lot": "1669321",
                    "propertytype": "Fabbricati",
                }
            ],
            feature_properties,
        )

    def test_gs_get_land_details(self):
        params = {
            "service": "WFS",
            "version": cnf.APP_CONFIG.GS_WFS_VERSION,
            "request": "GetFeature",
            "outputFormat": "application/json",
            "typename": cnf.APP_CONFIG.CATASTO_OPEN_LAND_DETAIL_LAYER,
            "viewparams": f"cityCode:H501;"
            f"citySheet:130;"
            f"landNumber:00150;"
            f"checkDate:"
            f"{datetime.datetime.today().strftime('%Y-%m-%d')}",
        }
        response = requests.get(
            f"{cnf.GEOSERVER_HOST}:"
            f"{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/ows",
            params,
        )
        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.text)
        self.assertEqual(payload["numberReturned"], 1)
        feature_properties = [
            feature["properties"] for feature in payload["features"]
        ]
        self.assertEqual(
            [
                {
                    "property": 2598,
                    "propertytype": "T",
                    "subordinate": None,
                    "quality": "FABB RURALE",
                    "class": "",
                    "hectares": 0,
                    "are": 3,
                    "centiare": 67,
                    "lot": "103625",
                    "cadastralrent": "0",
                    "agriculturalrent": "0",
                }
            ],
            feature_properties,
        )

    def test_gs_get_building_details(self):
        params = {
            "service": "WFS",
            "version": cnf.APP_CONFIG.GS_WFS_VERSION,
            "request": "GetFeature",
            "outputFormat": "application/json",
            "typename": cnf.APP_CONFIG.CATASTO_OPEN_BUILDING_DETAIL_LAYER,
            "viewparams": f"cityCode:H501;"
            f"citySheet:130;"
            f"buildingNumber:00164;"
            f"checkDate:"
            f"{datetime.datetime.today().strftime('%Y-%m-%d')}",
        }
        response = requests.get(
            f"{cnf.GEOSERVER_HOST}:"
            f"{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/ows",
            params,
        )
        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.text)
        self.assertEqual(payload["totalFeatures"], 1)
        feature_properties = [
            feature["properties"] for feature in payload["features"]
        ]
        self.assertEqual(
            [
                {
                    "subordinate": None,
                    "property": 68609,
                    "propertytype": "F",
                    "censuszone": "6",
                    "category": "C/6",
                    "_class": "14",
                    "consistency": "40 mq",
                    "rent": "218,98",
                    "lot": "2409126",
                }
            ],
            feature_properties,
        )

    def test_gs_get_property_owner(self):
        params = {
            "service": "WFS",
            "version": cnf.APP_CONFIG.GS_WFS_VERSION,
            "request": "GetFeature",
            "outputFormat": "application/json",
            "typename": cnf.APP_CONFIG.CATASTO_OPEN_PROPERTY_OWNER_LAYER,
            "viewparams": f"cityCode:H501;"
            f"property:68609;"
            f"propertyType:F;"
            f"checkDate:"
            f"{datetime.datetime.today().strftime('%Y-%m-%d')}",
        }
        response = requests.get(
            f"{cnf.GEOSERVER_HOST}:"
            f"{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/ows",
            params,
        )
        self.assertEqual(response.status_code, 200)
        payload = json.loads(response.text)
        self.assertEqual(payload["totalFeatures"], 1)
        feature_properties = [
            feature["properties"] for feature in payload["features"]
        ]
        self.assertEqual(
            [
                {
                    "nominative": "FOO SRL",
                    "fiscalcode": "00000000000",
                    "city": "ROMA",
                    "right": "Proprieta'",
                    "part": "",
                }
            ],
            feature_properties,
        )

    def test_cttitola(self):
        results = get_cttitola()
        expected_results = [
            (
                "A054",
                " ",
                41189,
                "F",
                4,
                236,
                "PRENESTINA",
                None,
                None,
                None,
                "68",
            )
        ]
        self.assertEqual(results, expected_results)

    def test_cuidenti(self):
        results = get_cuidenti()
        expected_results = [
            (
                "H501",
                " ",
                68609,
                "F",
                2,
                None,
                "0130",
                "00164",
                None,
                None,
                None,
            ),
            (
                "H501",
                " ",
                197859,
                "F",
                2,
                None,
                "0233",
                "00205",
                None,
                "0012",
                None,
            ),
            (
                "A054",
                " ",
                41189,
                "F",
                4,
                None,
                "0002",
                "00058",
                None,
                "0001",
                None,
            ),
        ]
        self.assertEqual(results, expected_results)

    def test_cuindiri(self):
        results = get_cuindiri()
        expected_results = [
            (
                "A054",
                " ",
                41189,
                "F",
                4,
                236,
                "PRENESTINA",
                None,
                None,
                None,
                "68",
            )
        ]
        self.assertEqual(results, expected_results)

    def test_cuutilit(self):
        results = get_cuutilit()
        expected_results = [
            ("A054", " ", 41320, "F", 2, None, "0003", "00205", None, "0001")
        ]
        self.assertEqual(results, expected_results)

    def test_cuarcuiu(self):
        results = get_cuarcuiu()
        expected_results = [
            (
                "H501",
                " ",
                68609,
                "F",
                2,
                "006",
                "C06",
                "14",
                "40",
                "47",
                "424000",
                "218,98",
                None,
                None,
                None,
                None,
                None,
                "T",
                None,
                None,
                None,
                "08051996",
                "06031999",
                "V",
                "051104",
                "001",
                "1996",
                None,
                None,
                None,
                None,
                None,
                None,
                "2409126",
                None,
                2843695,
                None,
                None,
                None,
                "VAR",
                "DIVERSA DISTRIBUZIONE SPAZI INTERNI",
                None,
                None,
                "4",
            ),
            (
                "H501",
                " ",
                197859,
                "F",
                2,
                "004",
                "C06",
                "06",
                "13",
                "13",
                "180700",
                "93,32",
                None,
                None,
                None,
                None,
                None,
                "T",
                None,
                None,
                None,
                "12031981",
                "01031989",
                "D",
                "  3494",
                None,
                "1981",
                None,
                None,
                None,
                None,
                None,
                None,
                "1669321",
                None,
                1350882,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
            ),
            (
                "A054",
                " ",
                41189,
                "F",
                4,
                None,
                "A02",
                "04",
                "5,5",
                None,
                "742500",
                "383,47",
                None,
                None,
                None,
                None,
                None,
                "T",
                None,
                None,
                None,
                "18032003",
                "18032003",
                "V",
                "003770",
                "001",
                "2003",
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                1821413,
                None,
                None,
                None,
                "VTO",
                "VARIAZIONE DI TOPONOMASTICA",
                None,
                None,
                None,
            ),
        ]
        self.assertEqual(results, expected_results)

    def test_curiserv(self):
        results = get_curiserv()
        expected_results = [("A054", " ", 41450, "F", 3, "1", "1000942")]
        self.assertEqual(results, expected_results)

    def test_ctpartic(self):
        results = get_ctpartic()
        expected_results = [
            (
                "H501",
                "A",
                2598,
                "T",
                2,
                130,
                "00150",
                None,
                None,
                None,
                279,
                "00",
                0,
                3,
                67,
                "1",
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "01010001",
                "28071988",
                "F",
                "243175",
                "000",
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                "0103625",
                None,
                684232,
                None,
                "FRZ",
                None,
                None,
                None,
            ),
            (
                "A054",
                " ",
                62761,
                "T",
                1,
                1,
                "00001",
                None,
                None,
                None,
                1,
                "04",
                0,
                52,
                10,
                "0",
                "0",
                "0",
                "8857",
                "8857",
                "4,57",
                "4,57",
                "01010001",
                "20091975",
                "I",
                None,
                "000",
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                "0000172",
                None,
                264837,
                None,
                None,
                None,
                None,
                None,
            ),
        ]
        self.assertEqual(results, expected_results)

    def test_ctdeduzi(self):
        results = get_ctdeduzi()
        expected_results = [("D452", " ", 1467499, "T", 4, "A1")]
        self.assertEqual(results, expected_results)

    def test_ctporzio(self):
        results = get_ctporzio()
        expected_results = [
            (
                "A054",
                " ",
                1467478,
                "T",
                3,
                "AA",
                36,
                "02",
                0,
                12,
                0,
                "5,58",
                "2,79",
            ),
            ("A054", " ", 1467478, "T", 3, "AB", 1, "00", 0, 0, 98, "0", "0"),
        ]
        self.assertEqual(results, expected_results)

    def test_archive_map(self):
        archive_map_func = "ctmp.archivia_mappa"
        water_result = get_waters("ctmp_a")
        self.assertEqual(0, len(water_result))
        trust_result = get_trusts("ctmp_a")
        self.assertEqual(0, len(trust_result))
        dress_line_result = get_dress_lines("ctmp_a")
        self.assertEqual(0, len(dress_line_result))
        text_result = get_texts("ctmp_a")
        self.assertEqual(0, len(text_result))
        symbol_result = get_symbols("ctmp_a")
        self.assertEqual(0, len(symbol_result))
        street_result = get_streets("ctmp_a")
        self.assertEqual(0, len(street_result))
        metadata_result = get_metadata("ctmp_a")
        self.assertEqual(0, len(metadata_result))
        dal.engine.execute(
            text(
                f"SELECT {archive_map_func}('H501', 'A', '130', '0', '0', 2);"
            ).execution_options(autocommit=True)
        )
        water_result = get_waters("ctmp_a")
        self.assertEqual(1, len(water_result))
        trust_result = get_trusts("ctmp_a")
        self.assertEqual(1, len(trust_result))
        dress_line_result = get_dress_lines("ctmp_a")
        self.assertEqual(1, len(dress_line_result))
        text_result = get_texts("ctmp_a")
        self.assertEqual(1, len(text_result))
        symbol_result = get_symbols("ctmp_a")
        self.assertEqual(1, len(symbol_result))
        street_result = get_streets("ctmp_a")
        self.assertEqual(1, len(street_result))
        metadata_result = get_metadata("ctmp_a")
        self.assertEqual(1, len(metadata_result))

        metadata_result = get_metadata("ctmp")
        self.assertEqual(2, len(metadata_result))
        dal.engine.execute(
            text(
                f"SELECT {archive_map_func}('AAAA', 'A', '130', '0', '0', 1);"
            ).execution_options(autocommit=True)
        )
        metadata_result = get_metadata("ctmp")
        self.assertEqual(1, len(metadata_result))
