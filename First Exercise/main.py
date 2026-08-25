"""Startpunkt für das Teilnehmerprojekt."""

from report_creators import JsonReportCreator, TextReportCreator


def main() -> None:
    report = {
        "title": "Monatsbericht",
        "content": "Umsatz: 1200 Euro",
    }

    creators = [TextReportCreator(), JsonReportCreator()]

    for creator in creators:
        print(creator.export_report(report))
        print()


if __name__ == "__main__":
    main()