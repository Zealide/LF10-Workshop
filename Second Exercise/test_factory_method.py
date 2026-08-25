import json
import unittest

from report_creators import JsonReportCreator, TextReportCreator


class FactoryMethodRefactoringTest(unittest.TestCase):
    def setUp(self) -> None:
        self.report = {
            "title": "Monatsbericht",
            "content": "Umsatz: 1200 Euro",
        }

    def test_text_creator_keeps_existing_output(self) -> None:
        self.assertEqual(
            TextReportCreator().export_report(self.report),
            "Monatsbericht\nUmsatz: 1200 Euro",
        )

    def test_json_creator_keeps_existing_output(self) -> None:
        output = JsonReportCreator().export_report(self.report)

        self.assertEqual(
            json.loads(output),
            self.report,
        )


if __name__ == "__main__":
    unittest.main()
