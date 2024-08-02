---
title: Architecture
parent: Technical Docs
nav_order: 1
---

{: .label }
[Kadir Aksoy]


# Architecture
{: .no_toc }

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

**Aufbau der Anwendung "StudyBuddy"**

| Dateien | Charakterisierung |
| ------- | ----------------- |
| 'app.py'| die Datei app.py dient als zentraler Einstiegspunkt und Hauptsteuerdatei der Anwendung. Verantwortlich für die erstellung der Flask-Anwendung, zu konfigurieren und den Server zu starten |
| 'routes.py'| die Datei routes.py beinhaltet unsere App Routes. Diese definieren, wie verschiedene URL's innerhalb der Anwendung verarbeiter werden. |
| 'utils.py'| die Datei utils.py dient für die Serialisierung und Deserialisierung von Daten. Spezifisch ist es dazu da, um die Daten in einer URL-sicheren Weise zu serialisieren, sodass sie sicher in URLs eingebettet und wiederhergestellt werden können.|
| 'forms.py' | zuständig für die Formulare, die Benutzereingabe zu definieren und zu verwalten, einschließlich Validierung und Verarbeitung der Formulardaten |
| 'get-pip.py' |  erledigt das Paketverwaltungstool pip zu installieren oder zu aktualisieren, um Python-Pakete zu verwalten |
| 'models.py' | dient dazu, die Datenbankmodelle zu definieren, die die Struktur und Beziehungen der Datenbanktabellen repräsentieren |
| 'static' | dafür zuständig, statische Dateien wie CSS, Bilder und andere Ressourcen zu speichern, die von der Anwendung verwendet werden |
| 'templates' | erledigt die HTML-Vorlagen speicherung, die für die Darstellung der Benutzeroberfläche verwendet werden |
| 'assets' | dafür zuständig, zusätzliche statische Ressourcen wie Bilder, Schriftarten und andere Mediendateien zu speichern, die von der Anwendung genutzt werden |
| 'gitignore' | dient dazu, festzulegen, welche Dateien und Verzeichnisse Git ignorieren soll, um sie nicht ins Versionskontrollsystem aufzunehmen |
| 'schema.sql' | zuständig für die SQL-Skripte zu enthalten, die zum Erstellen und Initialisieren der Datenbanktabellen und -strukturen verwendet werden |
| 'README.md' | dafür zuständig, eine umfassende Beschreibung des Projekts zu bieten, einschließlich Anweisungen zur Installation, Nutzung und Beitragsrichtlinien |
| 'database.db' | dafür zuständig, die SQLite-Datenbankdatei zu speichern, die alle Daten der Anwendung enthält |