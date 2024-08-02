---
title: Design Decisions
nav_order: 3
---

{: .label }
[Kadir Aksoy]

{: .no_toc }
# Design decisions

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## 01: [Datenbank - SQLAlchemy Toolkit oder Plain SQL]

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 31-07-2024

### Problem statement

Die StudyBuddy-WebApp benötigt eine effiziente und zuverlässige Methode zur Speicherung und Verwaltung von Benutzerinformationen, Profilen, Nachrichten und Verbindungen zwischen Benutzern. Eine robuste Datenbanklösung ist erforderlich, um diese Daten sicher zu speichern, schnelle Abfragen zu ermöglichen und eine skalierbare Architektur zu bieten, die zukünftige Erweiterungen und zunehmende Benutzerzahlen unterstützt.

### Decision

Nach sorgfältiger Überlegung haben wir uns entschieden, SQLAlchemy als ORM (Object-Relational Mapping)-Werkzeug zu verwenden, um die Datenbankoperationen effizient zu verwalten und die Entwicklung zu erleichtern.

### Regarded options

#### SQLAlchemy

Vorteile:

* Deklarative Syntax zur Definition von Datenbankmodellen.
* Unterstützung für verschiedene Datenbanktypen (SQLite, PostgreSQL#
  MySQL).
* Einfache Integration mit Flask und Unterstützung für Datenbankmigrationen.

Nachteile:

* Weniger performant für sehr große Datenmengen und komplexe Abfragen.

#### Plain SQL

Vorteile:

* Volle Kontrolle über die SQL-Abfragen und Datenbankoperationen.
* Direkte Nutzung von Datenbank-spezifischen Optimierungen und
  Funktionen.

Nachteile:

* Erhöhter Entwicklungsaufwand und größere Fehleranfälligkeit.
* Mangel an Abstraktion führt zu komplexerer Wartung und weniger
  Portabilität.

We regarded two alternative options:

+ Plain SQL3
+ SQLAlchemy

| Criterion | Plain SQL | SQLAlchemy |
| --- | --- | --- |
| **Know-how** | ✔️ We know how to write SQL | ❌ We must learn ORM concept & SQLAlchemy |
| **Change DB schema** | ❌ SQL scattered across code | ✔️ Good: classes, bad: need Alembic on top |
| **Switch DB engine** | ❌ Different SQL dialect | ✔️ Abstracts away DB engine |


## 02: [Datenbankauswahl - SQLite, MySQL oder PostgreSQL]

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 31-06-2024

### Problem statement

Die StudyBuddy-WebApp benötigt eine Datenbanklösung, die leichtgewichtig, einfach zu verwalten und gut in die bestehende Infrastruktur integrierbar ist. Die Datenbank sollte für die aktuelle Größe und Nutzung der Anwendung ausreichend sein und gleichzeitig zukünftige Erweiterungen ermöglichen.

### Decision

Nach sorgfältiger Überlegung haben wir uns entschieden, SQLite als Datenbank zu verwenden, um die Daten der StudyBuddy-WebApp zu speichern. Diese Entscheidung wurde getroffen, um eine einfache und effiziente Entwicklung und Verwaltung zu gewährleisten.

### Regarded options

Vorteile:

* Leichtgewichtig und einfach zu verwenden.
* Keine separate Serverinstallation erforderlich.
* Gut geeignet für kleine bis mittelgroße Anwendungen.

Nachteile:

* Weniger geeignet für sehr große Anwendungen mit hohem Datenaufkommen.
* Eingeschränkte Unterstützung für parallele Schreibvorgänge.

#### MySQL

Vorteile:

* Weit verbreitet und gut dokumentiert.
* Leistungsstark und flexibel.

Nachteile:

* Erfordert eine separate Serverinstallation und Verwaltung.
* Komplexere Konfiguration und Administration im Vergleich zu SQLite.

#### PostgreSQL

Vorteile:

* Leistungsstark und skalierbar.
* Unterstützung für komplexe Abfragen und Datenbank-Transaktionen.

Nachteile:

* Erfordert eine separate Serverinstallation und Verwaltung.
* Höhere Komplexität und Verwaltungsaufwand im Vergleich zu SQLite.

## 03: [SocketIO]

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 30-06-2024

### Problem statement

Für die Echtzeit-Kommunikation zwischen Benutzern, insbesondere für die Chat-Funktion der StudyBuddy-WebApp, benötigen wir eine zuverlässige Lösung.

### Decision

Wir haben uns entschieden, SocketIO für die Echtzeit-Kommunikation zu verwenden, um eine reibungslose und zuverlässige Chat-Funktion in unserer WebApp zu gewährleisten.

### Regarded options

Vorteile:

* Bidirektionale, ereignisbasierte Kommunikation.
* Unterstützung für mehrere Transportschichten (WebSocket, Polling).
* Nahtlose Integration mit Flask-SocketIO.

Nachteile:

* Zusätzliche Komplexität bei der Verwaltung von Verbindungen und Echtzeitereignissen.

#### WebSockets

Vorteile:

* Direkte, bidirektionale Kommunikation zwischen Client und Server.
* Sehr performant und geeignet für Echtzeit-Anwendungen.
* Weniger Overhead im Vergleich zu SocketIO.

Nachteile:

* Keine Unterstützung für ältere Browser, die WebSockets nicht unterstützen.
* Erfordert mehr manuelle Arbeit für Fallback-Mechanismen und Verbindungshandling.
* Weniger benutzerfreundlich in Bezug auf Bibliotheken und Integrationen im Vergleich zu SocketIO.

## 04: [Flask-WTF]

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 28-06-2024

### Problem statement

Benötigung einer effizienten Lösung zur Erstellung und Validierung von Formularen, um Benutzereingaben sicher und benutzerfreundlich zu verarbeiten.

### Decision

Wir haben uns für Flask-WTF entschieden, um sichere und benutzerfreundliche Formulare in unserer WebApp zu erstellen und zu validieren.

### Regarded options

Vorteile:

* Einfache Erstellung und Validierung von Formularen.
* Integration mit Flask und Unterstützung für CSRF-Schutz.
* Nutzt die mächtige WTForms-Bibliothek.

Nachteile:

* Kann für sehr komplexe Formulare und Validierungsregeln umständlich werden.

#### WTForms

Vorteile:

* Leistungsstarke Bibliothek zur Erstellung und Validierung von Formularen.
* Flexibel und gut dokumentiert.
* Kann unabhängig von Flask verwendet werden, was mehr Flexibilität bietet.

Nachteile:

* Erfordert zusätzliche Arbeit für die Integration mit Flask.
* Kein eingebauter CSRF-Schutz, erfordert zusätzliche Sicherheitsmaßnahmen.

#### Django Forms

Vorteile:

* Integrierte Formular- und Validierungslösung im Django-Framework.
* Automatische Erstellung von Formularen basierend auf Datenbankmodellen.
* Umfangreiche Funktionen und Sicherheitsmaßnahmen, einschließlich CSRF-Schutz.

Nachteile:

* Nur für Django geeignet, nicht für Flask.
* Höhere Komplexität und Lernkurve im Vergleich zu Flask-WTF.

## 05: [Flask-Email]

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 10-07-2024

### Problem statement

Die StudyBuddy-WebApp benötigt eine zuverlässige und effiziente Methode zum Versenden von E-Mails, um Benutzer über wichtige Ereignisse wie Registrierungsbestätigungen, Passwort-Reset-Anfragen und Benachrichtigungen zu informieren. Die Lösung sollte sich nahtlos in Flask integrieren lassen und einfach zu implementieren und zu verwalten sein.

### Decision

Wir haben uns entschieden, Flask-Mail zu verwenden, um E-Mails in unserer StudyBuddy-WebApp zu versenden. Diese Entscheidung wurde getroffen, um eine einfache und effektive Methode zur E-Mail-Verwaltung zu gewährleisten.

### Regarded options

Vorteile:

* Nahtlose Integration mit Flask.
* Einfache Konfiguration und Nutzung.
* Unterstützt verschiedene E-Mail-Server und Protokolle (SMTP, SSL/TLS).
* Gute Dokumentation und Community-Unterstützung.
* Ermöglicht das Versenden von Text- und HTML-E-Mails sowie das Anhängen von Dateien.

Nachteile:

* Begrenzte erweiterte Funktionen im Vergleich zu spezialisierten E-Mail-Diensten.
* Erfordert die Konfiguration und Verwaltung eines eigenen E-Mail-Servers oder eines externen SMTP-Dienstes.

#### SendGrid

Vorteile:

* Leistungsstarker externer E-Mail-Dienst mit vielen erweiterten Funktionen (z.B. Zustellbarkeitsanalyse, API für Massen-E-Mails).
* Kein eigener E-Mail-Server erforderlich, einfachere Verwaltung.
* Gute Skalierbarkeit und Zuverlässigkeit.

Nachteile:

* Zusätzliche Kosten für die Nutzung des Dienstes.
* Abhängigkeit von einem externen Dienstleister.
* Komplexere API-Integration im Vergleich zu Flask-Mail.
---