"""Creator-Klassen: Sie wählen den passenden ReportExporter aus."""

from abc import ABC, abstractmethod

from exporters import JsonReportExporter, ReportExporter, TextReportExporter


class ReportCreator(ABC):
    """Creator mit dem gemeinsamen Export-Ablauf."""

    @abstractmethod
    def factory_method(self) -> ReportExporter:
        """Erzeugt den konkreten Exporter."""

    def export_report(self, report: dict[str, str]) -> str:
        """Exportiert einen Bericht, ohne das Format direkt zu kennen."""
        exporter = self.factory_method()
        return exporter.export(report)


class TextReportCreator(ReportCreator):
    """Konkreter Creator für Text-Exporte."""

    def factory_method(self) -> ReportExporter:
        return TextReportExporter()


class JsonReportCreator(ReportCreator):
    """Konkreter Creator für JSON-Exporte."""

    def factory_method(self) -> ReportExporter:
        return JsonReportExporter()