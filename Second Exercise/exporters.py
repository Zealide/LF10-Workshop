"""Legacy-Produkte: verschiedene Exporter für einen Bericht."""

import json


class TextReportExporter:
    """Konkretes Produkt für einfachen Text."""

    def export(self, report: dict[str, str]) -> str:
        return f"{report['title']}\n{report['content']}"


class JsonReportExporter:
    """Konkretes Produkt für JSON."""

    def export(self, report: dict[str, str]) -> str:
        return json.dumps(report, ensure_ascii=False)
