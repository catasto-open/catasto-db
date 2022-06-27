import datetime
import unittest

from app.tests import CONN_STRING
from app.tests.db import dal
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
)


class TestApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        dal.db_init(CONN_STRING)
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
            )
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
        ]
        self.assertEqual(results, expected_results)
