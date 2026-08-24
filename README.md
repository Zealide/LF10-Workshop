# Teilnehmerprojekt: Factory Method

Dieses Projekt ist eine Lernaufgabe zum Design Pattern **Factory Method**.
Du arbeitest mit einem Dokumenten-Export: Ein Bericht kann entweder als TXT-
oder als JSON-Datei exportiert werden.

## Lernziel

Nach der Aufgabe kannst du:

- das gemeinsame Produkt eines Patterns erkennen,
- eine Factory Method in einem Creator finden,
- erklären, warum der allgemeine Ablauf nicht in jeder Unterklasse dupliziert wird,
- einen weiteren konkreten Creator und ein weiteres Produkt ergänzen.

## Projekt starten

```bash
python3 main.py
```

Tests ausführen:

```bash
python3 -m unittest -v
```

## Projektstruktur

- `exporters.py`: Produkt und konkrete Produkte
- `report_creators.py`: Creator und konkrete Creator
- `main.py`: kleines ausführbares Beispiel
- `test_factory_method.py`: Tests als Lernhilfe
- `aufgaben.md`: Aufgaben für die Teilnehmer

## So liest du den Code

1. Öffne `exporters.py`. `ReportExporter` ist das gemeinsame Produkt.
2. Öffne `report_creators.py`. `ReportCreator` definiert die Factory Method.
3. Vergleiche `TextReportCreator` und `JsonReportCreator`.
4. Verfolge in `export_report()`, wie ein konkreter Exporter erzeugt und benutzt wird.

Die Basisklasse kennt nur `ReportExporter`. Sie muss nicht wissen, ob später
`TextReportExporter` oder `JsonReportExporter` verwendet wird.