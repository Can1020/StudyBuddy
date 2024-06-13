---
title: Features and Functions
nav_order: 7
---

{: .attention }
> (This page contains a description of the each feature and screen explaining what it is and how it works)

# UI Screens of StudyBuddy (In works)

## Sign-In Page

![get_list_todos_sample](/StudyBuddy/assets/images/Sign in.jpg)

**Ziel**
Der Sign-In Screen ermöglicht es Benutzern, sich mit ihrer Universitäts-E-Mail-Adresse und einem Passwort bei der StudyBuddy-Webanwendung anzumelden.

**Komponenten**

    1.	**Header:**
        o Logo der Anwendung (StudyBuddy).
        o Begrüßungstext: „Welcome to StudyBuddy“.
    2.	**Formular:**
        o **Eingabefeld für die Universitäts-E-Mail**:
             Platzhalter: „University Email“.
             E-Mail-Validierung, um sicherzustellen, dass nur gültige E-Mail-Adressen akzeptiert werden.
        o **Eingabefeld für das Passwort:**
             Platzhalter: „Password“.
             Passwort wird standardmäßig maskiert.
             Ein Icon (Auge) zum Umschalten der Sichtbarkeit des Passworts.
        o **Link „Forgot Password?“:**
             Leitet den Benutzer zur Seite „Passwort zurücksetzen“ weiter.
    3.	**Login-Button:**
        o Text: „LOG IN“.
        o Reagiert auf Klick, indem er die Anmeldeinformationen überprüft.
    4.	**Registrierungsaufforderung:**
        o Text: „Don’t have an account? REGISTER“.
        o Leitet den Benutzer zur Registrierungsseite weiter.

**Technologien und Tools**
    • **Frontend:**
        o React für die Benutzeroberfläche.
        o Axios für HTTP-Anfragen.
        o CSS für das Styling.
    • **Backend:**
        o Node.js mit Express für den Server.
        o Mongoose zur Verwaltung der MongoDB-Datenbank.
        o Bcrypt für die Passwort-Hashing.
        o Jsonwebtoken (JWT) für die Token-basierte Authentifizierung.
    • **Datenbank:**
        o MongoDB für die Speicherung von Benutzerdaten

## Homescreen Page

![get_list_todos_sample](/StudyBuddy/assets/images/Homescreen.jpg)

**Ziel**

Der Home Screen von StudyBuddy dient dazu, Benutzern Profile anderer Studenten anzuzeigen, um die Vernetzung und Zusammenarbeit zu fördern.
Benutzer können Profile durchsehen und sich entscheiden, ob sie sich mit anderen Studenten verbinden möchten.

**Features**
    • Anzeige von Studentenprofilen mit Namen, Alter, Universität, Studiengang und Interessen.
    • Möglichkeit, Profile zu liken oder abzulehnen.
    • Navigation zu anderen Bereichen der App wie Suche, Nachrichten und Profil.

**Technologien**
    • **Frontend:** React, CSS
    • **Backend:** Node.js, Express.js
    • **Datenbank:** MongoDB
    • **Versionskontrolle:** Git und GitHub

**Komponenten und Funktionen**
    1.	**Frontend-Komponenten:**
        o Home: Diese Komponente ist für die Anzeige der Profile verantwortlich.
        o ProfileCard: Eine Unterkomponente von Home, die einzelne Profile darstellt.
    2.	**Backend-Routen:**
        o GET /api/profiles: Route zum Abrufen aller Profile aus der Datenbank.
    3.	**Datenmodell:**
        o User: Enthält Felder wie Name, Alter, Universität, Studiengang, Interessen und Bild-URL.

**Ablauf**
    **1. Frontend:**
        o Die Home-Komponente sendet beim Laden eine Anfrage an das Backend, um alle Profile abzurufen.
        o Die Profile werden in der Benutzeroberfläche als Karten angezeigt, die Name, Alter, Universität, Studiengang und Interessen des Studenten zeigen.
        o Benutzer können auf Like- oder Dislike-Buttons klicken, um ihre Präferenz für jedes Profil auszudrücken.
    **2. Backend:**
        o Der Server empfängt die Anfrage zum Abrufen der Profile und fragt die Datenbank ab.
        o Die Profile werden als JSON-Objekte zurück an das Frontend gesendet.
    **3. Datenbank:**
        o MongoDB speichert die Benutzerdaten, einschließlich Name, Alter, Universität, Studiengang, Interessen und Bild-URL.

**Benutzeroberfläche (UI)**
   ** •	Design:**
        o Ein einfaches, klares Layout mit einer Liste von Profilkarten.
        o Jede Profilkarte zeigt ein Bild, Name, Alter, Universität, Studiengang und Interessen.
        o Like- und Dislike-Buttons unten auf jeder Karte.
    **•	Navigationsleiste:**
        o Linksseitige Navigation mit Links zu Home, Suche, Nachrichten und Profil.


## Messages Page

![get_list_todos_sample](/StudyBuddy/assets/images/Messages.jpg)
    **Ziel**
        Der Messages Screen von StudyBuddy bietet eine Chat-Funktionalität, die es Benutzern ermöglicht, in Echtzeit Nachrichten auszutauschen. Dies fördert die Kommunikation und Zusammenarbeit zwischen Studenten.
    **Features**
        • Anzeige einer Liste aller Chats.
        • Möglichkeit, zwischen verschiedenen Chats zu wechseln.
        • Echtzeit-Nachrichtenübertragung.
        • Eingabefeld für neue Nachrichten.
    **Technologien**
        • Frontend: React, CSS
        • Backend: Node.js, Express.js, Socket.io (für Echtzeit-Kommunikation)
        • Datenbank: MongoDB
        • Versionskontrolle: Git und GitHub

**Komponenten und Funktionen**

    1. **Frontend-Komponenten:**
        o **Messages:** Diese Hauptkomponente zeigt die Chat-Übersicht und die Nachrichten für den ausgewählten Chat.
        o **ChatList:** Eine Unterkomponente von Messages, die die Liste der Chats anzeigt.
        o **ChatWindow:** Eine Unterkomponente von Messages, die die Nachrichten des ausgewählten Chats anzeigt.
        o **MessageInput:** Eine Unterkomponente von ChatWindow, die das Eingabefeld für neue Nachrichten bereitstellt.

    2. **Backend-Routen und -Funktionen:**
        o **GET /api/chats:** Route zum Abrufen aller Chats eines Benutzers.
        o **GET /api/chats/:chatId:** Route zum Abrufen aller Nachrichten eines bestimmten Chats.
        o **POST /api/chats/**
        **/messages:** Route zum Senden einer neuen Nachricht.
    o **Socket.io:** Für die Echtzeit-Kommunikation zwischen Benutzern.

    3. **Datenmodell:**
        o User: Enthält Felder wie Name, E-Mail, und Profilbild-URL.
        o Chat: Enthält Felder wie Teilnehmer (Array von User-IDs) und Nachrichten (Array von Message-IDs).
        o Message: Enthält Felder wie Absender (User-ID), Inhalt, Zeitstempel und Chat-ID.

**Ablauf**

    1. **Frontend:**
        o Die Messages-Komponente sendet beim Laden Anfragen an das Backend, um die Chat-Übersicht und die Nachrichten des ausgewählten Chats abzurufen.
        o Benutzer können zwischen verschiedenen Chats wechseln, indem sie in der ChatList-Komponente auf einen Chat klicken.
        o Nachrichten werden in Echtzeit durch Socket.io empfangen und in der ChatWindow-Komponente angezeigt.
        o Neue Nachrichten können im MessageInput eingegeben und abgesendet werden.
    2. **Backend:**
        o Der Server empfängt Anfragen zum Abrufen von Chats und Nachrichten und fragt die Datenbank ab.
        o Der Server verwendet Socket.io, um neue Nachrichten in Echtzeit an alle Teilnehmer eines Chats zu senden.
        o Neue Nachrichten werden in der Datenbank gespeichert und an die verbundenen Clients gesendet.
    3. **Datenbank:**
        o MongoDB speichert die Benutzerdaten, Chat-Daten und Nachrichten.

**Benutzeroberfläche (UI)**
    • **Design:**
        o Linke Seite: Chat-Übersicht mit Liste aller Chats und Profilbildern der Teilnehmer.
        o Rechte Seite: Nachrichtenbereich mit dem aktuellen Chatverlauf und einem Eingabefeld für neue Nachrichten.
    • **Navigationsleiste:**
        o Linksseitige Navigation mit Links zu Home, Suche, Nachrichten und Profil.

{: .fs-2 }
Last build: {{ site.time | date: '%d %b %Y, %R%:z' }}