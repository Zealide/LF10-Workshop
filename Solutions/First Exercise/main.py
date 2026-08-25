"""Startpunkt fuer die Musterloesung."""

from report_creators import (
    JsonReportCreator,
    MarkdownReportCreator,
    TextReportCreator,
)


def main() -> None:
    report = {
        "title": "Monatsbericht",
        "content": "Umsatz: 1200 Euro",
    }

    creators = [
        TextReportCreator(),
        JsonReportCreator(),
        MarkdownReportCreator(),
    ]

    for creator in creators:
        print(creator.export_report(report))
        print()


if __name__ == "__main__":
    main()
