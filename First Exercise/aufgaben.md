# Aufgaben

## Aufgabe 1: Pattern finden

Beantworte diese Fragen, bevor du den Code veränderst:

1. Welche Klasse ist das gemeinsame Produkt?
2. Welche Klassen sind konkrete Produkte?
3. Welche Methode ist die Factory Method?
4. Welche Klassen entscheiden, welches Produkt erzeugt wird?

## Aufgabe 2: Eigenen Exporter ergänzen

Ergänze einen Markdown-Export.

1. Erstelle in `exporters.py` die Klasse `MarkdownReportExporter`.
2. Sie soll von `ReportExporter` erben.
3. Die Methode `export()` soll zum Beispiel zurückgeben:

   `# Monatsbericht\n\nUmsatz: 1200 Euro`

4. Erstelle in `report_creators.py` den passenden `MarkdownReportCreator`.
5. Überschreibe dort nur `factory_method()`.
6. Ergänze einen Test für den neuen Creator.
7. Füge den neuen Creator in `main.py` ein.

## Merksatz

Der allgemeine Ablauf bleibt im Creator. Die Unterklasse entscheidet nur,
welches konkrete Produkt die Factory Method erstellt.