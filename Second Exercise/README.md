# Teilnehmerprojekt: Factory Method refaktorieren

Dieses Projekt startet als kleines Legacy-Projekt. Es exportiert Berichte als
TXT- oder JSON-Text. Beide Creator enthalten derzeit fast denselben Ablauf.

Die Aufgabe ist, den bestehenden Code mit dem Design Pattern **Factory Method**
zu refaktorieren und anschließend um einen CSV-Export zu erweitern.

## Lernziel

Nach der Aufgabe kannst du:

- duplizierten Erzeugungs- und Ablaufcode in einem Legacy-Projekt erkennen,
- ein gemeinsames Produkt und einen gemeinsamen Creator herausarbeiten,
- die Factory Method so einsetzen, dass Unterklassen nur die Produktauswahl
  treffen,
- das bestehende Verhalten während eines Refactorings erhalten,
- einen weiteren konkreten Creator und ein weiteres Produkt ergänzen.

## Projekt starten

```bash
python3 main.py
```

Tests ausführen:

```bash
python3 -m unittest -v
```

Die Tests prüfen zunächst das Verhalten des alten Projekts. Nach der
Refaktorierung sollen sie unverändert weiterhin erfolgreich sein. Ergänze
zusätzliche Tests für den CSV-Export.

## Projektstruktur

- `exporters.py`: aktuelle Exporter und später das gemeinsame Produkt
- `report_creators.py`: aktuelle Creator und später die Factory Method
- `main.py`: ausführbares Beispiel
- `test_factory_method.py`: Verhaltenstests als Sicherheitsnetz
- `aufgaben.md`: Aufgaben für die Teilnehmer

## Ausgangslage

Das Projekt funktioniert, aber `TextReportCreator` und `JsonReportCreator`
implementieren denselben Ablauf selbst. Beide Klassen müssen außerdem wissen,
welcher Exporter erzeugt werden soll. Genau diese Verantwortlichkeiten sollen
durch die Factory Method sauber getrennt werden.
