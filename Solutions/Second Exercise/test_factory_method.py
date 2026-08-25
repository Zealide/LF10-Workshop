import json
import unittest

from exporters import (
    JsonReportExporter,
    MarkdownReportExporter,
    ReportExporter,
    TextReportExporter,
)
from report_creators import (
    JsonReportCreator,
    MarkdownReportCreator,
    ReportCreator,
    TextReportCreator,
)


class FactoryMethodSolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.report = {
            "title": "Monatsbericht",
            "content": "Umsatz: 1200 Euro",
        }

    def test_product_hierarchy(self) -> None:
        self.assertTrue(issubclass(TextReportExporter, ReportExporter))
        self.assertTrue(issubclass(JsonReportExporter, ReportExporter))
        self.assertTrue(issubclass(MarkdownReportExporter, ReportExporter))

    def test_creator_hierarchy(self) -> None:
        self.assertTrue(issubclass(TextReportCreator, ReportCreator))
        self.assertTrue(issubclass(JsonReportCreator, ReportCreator))
        self.assertTrue(issubclass(MarkdownReportCreator, ReportCreator))

    def test_factory_methods_create_matching_products(self) -> None:
        self.assertIsInstance(
            TextReportCreator().factory_method(), TextReportExporter
        )
        self.assertIsInstance(
            JsonReportCreator().factory_method(), JsonReportExporter
        )
        self.assertIsInstance(
            MarkdownReportCreator().factory_method(), MarkdownReportExporter
        )

    def test_existing_outputs_are_preserved(self) -> None:
        self.assertEqual(
            TextReportCreator().export_report(self.report),
            "Monatsbericht\nUmsatz: 1200 Euro",
        )
        self.assertEqual(
            json.loads(JsonReportCreator().export_report(self.report)),
            self.report,
        )

    def test_markdown_creator_exports_markdown(self) -> None:
        self.assertEqual(
            MarkdownReportCreator().export_report(self.report),
            "# Monatsbericht\n\nUmsatz: 1200 Euro",
        )


if __name__ == "__main__":
    unittest.main()
