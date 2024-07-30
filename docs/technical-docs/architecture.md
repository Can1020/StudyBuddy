---
title: Architecture
parent: Technical Docs
nav_order: 1
---

{: .label }
[Kadir Aksoy]


# AppArchitecture
{: .no_toc }

{: .attention }
> This page describes how the application is structured and how important parts of the app work. It should give a new-joiner sufficient technical knowledge for contributing to the codebase.
> 
> See [this blog post](https://matklad.github.io/2021/02/06/ARCHITECTURE.md.html) for an explanation of the concept and these examples:
>
> + <https://github.com/rust-lang/rust-analyzer/blob/master/docs/dev/architecture.md>
> + <https://github.com/Uriopass/Egregoria/blob/master/ARCHITECTURE.md>
> + <https://github.com/davish/obsidian-full-calendar/blob/main/src/README.md>
> 
> For structural and behavioral illustration, you might want to leverage [Mermaid](../ui-components.md), e.g., by charting common [C4](https://c4model.com/) or [UML](https://www.omg.org/spec/UML) diagrams.
> 
>
> You may delete this `attention` box.

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

**Aufbau der Anwendung "StudyBuddy"**

| Dateien | Charakterisierung |
| ------- | ----------------- |
| 'db.py' | dafür zuständig, die SQLite-Datenbankinstanz zu initialisieren und bereitzustellen, um die Datenbankoperationen zu verwalten |
| 'app.py'| die Datei app.py dient als zentraler Einstiegspunkt und Hauptsteuerdatei der Anwendung. Verantwortlich für die erstellung der Flask-Anwendung, zu konfigurieren und den Server zu starten |
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

## Overview

[Give a high-level overview of what your app does and how it achieves it: similar to the value proposition, but targeted at a fellow developer who wishes to contribute.]

## Codemap

[Describe how your app is structured. Don't aim for completeness, rather describe *just* the most important parts.]

## Cross-cutting concerns

[Describe anything that is important for a solid understanding of your codebase. Most likely, you want to explain the behavior of (parts of) your application. In this section, you may also link to important [design decisions](../design-decisions.md).]
