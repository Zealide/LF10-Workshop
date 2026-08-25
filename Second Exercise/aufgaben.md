# Aufgaben

## Aufgabe 1: Legacy-Code untersuchen

Führe zuerst die Anwendung und die Tests aus.

1. Markiere in `report_creators.py` die Codezeilen, die in beiden Klassen
   gleich oder sehr ähnlich sind.
2. Welche Klasse erzeugt das eigentliche Produkt?
3. Was müsste sich ändern, wenn ein drittes Exportformat hinzukommt?
4. Welche Teile des Ablaufs sollten unabhängig vom Format sein?

Bevor du refaktorierst, notiere dir die aktuellen Ausgaben der beiden Creator.
Sie dienen als Verhalten, das erhalten bleiben muss.

## Aufgabe 2: Gemeinsames Produkt herausarbeiten

Refaktoriere `exporters.py`:

1. Erstelle die abstrakte Basisklasse `ReportExporter`.
2. Verschiebe die gemeinsame Schnittstelle in die abstrakte Methode
   `export(report)`.
3. Lasse `TextReportExporter` und `JsonReportExporter` von
   `ReportExporter` erben.
4. Das Ausgabeformat der bestehenden Exporter darf sich nicht ändern.

## Aufgabe 3: Factory Method einführen

Refaktoriere `report_creators.py`:

1. Erstelle die abstrakte Basisklasse `ReportCreator`.
2. Definiere darin die abstrakte Methode `factory_method()`.
3. Verschiebe den gemeinsamen Ablauf in `export_report(report)`.
4. Erzeuge den Exporter in `export_report()` ausschließlich über
   `factory_method()`.
5. Passe `TextReportCreator` und `JsonReportCreator` an. Ihre einzige
   formatspezifische Aufgabe soll die Implementierung von `factory_method()`
   sein.
6. Entferne die duplizierte Ablauf-Logik aus den konkreten Creators.

## Aufgabe 4: Verhalten sichern

Führe die Tests erneut aus. Alle bestehenden Tests müssen weiterhin erfolgreich
sein. Ergänze außerdem Tests, die zeigen, dass:

- `factory_method()` den passenden konkreten Exporter erzeugt,
- beide konkreten Creator den Bericht korrekt exportieren,
- der gemeinsame Ablauf nicht in den Unterklassen dupliziert wird.

## Aufgabe 5: Neues Format ergänzen

Ergänze einen CSV-Export:

1. Erstelle `CsvReportExporter` in `exporters.py`.
2. Erzeuge eine Kopfzeile `title,content` und eine Datenzeile für den Bericht.
3. Erstelle `CsvReportCreator` in `report_creators.py`.
4. Überschreibe im neuen Creator nur `factory_method()`.
5. Ergänze passende Tests.
6. Füge den neuen Creator in `main.py` ein.

Beispielausgabe:

```text
title,content
Monatsbericht,Umsatz: 1200 Euro
```

## Reflexion

Beantworte zum Abschluss:

- Welche Verantwortung liegt im Creator und welche im konkreten Produkt?
- Warum bleibt `export_report()` in der Basisklasse?
- Welcher Teil des Codes muss sich beim nächsten Exportformat ändern?
- Woran erkennst du, dass ein Refactoring das Verhalten erhalten hat?

## Merksatz

Beim Refactoring bleibt der allgemeine Ablauf im Creator. Die Unterklasse
entscheidet über die Factory Method nur, welches konkrete Produkt verwendet
wird.
