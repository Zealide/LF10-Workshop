"""Produkte: verschiedene Exporter fuer einen Bericht."""

from abc import ABC, abstractmethod
import json


class ReportExporter(ABC):
    """Gemeinsames Produkt: Jeder Exporter kann einen Bericht exportieren."""

    @abstractmethod
    def export(self, report: dict[str, str]) -> str:
        """Wandelt einen Bericht in ein Ausgabeformat um."""


class TextReportExporter(ReportExporter):
    """Konkretes Produkt fuer einfachen Text."""

    def export(self, report: dict[str, str]) -> str:
        return f"{report['title']}\n{report['content']}"


class JsonReportExporter(ReportExporter):
    """Konkretes Produkt fuer JSON."""

    def export(self, report: dict[str, str]) -> str:
        return json.dumps(report, ensure_ascii=False)


class MarkdownReportExporter(ReportExporter):
    """Konkretes Produkt fuer Markdown."""

    def export(self, report: dict[str, str]) -> str:
        return f"# {report['title']}\n\n{report['content']}"
