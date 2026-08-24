import unittest

from exporters import JsonReportExporter, TextReportExporter
from report_creators import JsonReportCreator, TextReportCreator


class FactoryMethodTest(unittest.TestCase):
    def setUp(self) -> None:
        self.report = {
            "title": "Monatsbericht",
            "content": "Umsatz: 1200 Euro",
        }

    def test_text_creator_creates_text_exporter(self) -> None:
        self.assertIsInstance(
            TextReportCreator().factory_method(), TextReportExporter
        )

    def test_json_creator_creates_json_exporter(self) -> None:
        self.assertIsInstance(
            JsonReportCreator().factory_method(), JsonReportExporter
        )

    def test_creators_export_the_report(self) -> None:
        self.assertEqual(
            TextReportCreator().export_report(self.report),
            "Monatsbericht\nUmsatz: 1200 Euro",
        )
        self.assertEqual(
            JsonReportCreator().export_report(self.report),
            '{"title": "Monatsbericht", "content": "Umsatz: 1200 Euro"}',
        )


if __name__ == "__main__":
    unittest.main()