"""Legacy-Creator mit absichtlich dupliziertem Export-Ablauf."""

from exporters import JsonReportExporter, TextReportExporter


class TextReportCreator:
    """Legacy-Creator für Text-Exporte."""

    def export_report(self, report: dict[str, str]) -> str:
        exporter = TextReportExporter()
        return exporter.export(report)


class JsonReportCreator:
    """Legacy-Creator für JSON-Exporte."""

    def export_report(self, report: dict[str, str]) -> str:
        exporter = JsonReportExporter()
        return exporter.export(report)
