---
title: Goals
parent: Team Evaluation
nav_order: 1
---

{: .label }
[Kadir Aksoy]

{: .no_toc }
# Goals achieved and missed

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## Achieved Goals

1. Erfolgreiche Implementierung der Benutzerregistrierung: 

Wir haben eine funktionale Registrierung mit der Validierung von Universitäts-E-Mail-Adressen umgesetzt, sodass nur berechtigte Studenten Zugang zur Plattform haben.

2. Passwort Vergessen Link:

Benutzer müssen sich keine Gedanken machen, falls sie das Passwort für deren Account vergessen. Mittels unserer Passwort Vergessen Funktion können Benutzer deren Studenten Email eingeben und bekommen einen Link zur Zurücksetzung des Passwortes.

3. Erstellung eines benutzerfreundlichen Login-Bildschirms:

Der Login-Bildschirm wurde gemäß den bereitgestellten Designs entwickelt und ermöglicht eine einfache und sichere Anmeldung für Benutzer.

4. Matchmaking durch Likes bzw. Dislikes

Das Matchmaking System wurde wie vorgesehen umgesetzt. Die Likes der Nutzer werden jeweils in der Datanbank eingetragen. Sobald zwei Benutzer sich gegenseiten Liken, bekommen diese eine Benachrichtigung in Form eines Alerts womit die über deren neuen Match informiert werden.

5. Chat Funktion & Speicherung des Verlaufs

Die Chatfunktion wurde ebenfalls wie vorgesehen umgesetzt. Benutzer können nach einem erfolgreichen Match miteinander über Chat in Echtzeit kommunizieren. Außerdem haben wir eine neue Funktion, die Anfangs nicht vorgesehen war hinzugefügt, nämlich einen Chat Verlauf, wodurch Benutzer den Überblick von deren Konversationen behalten.

6. Datenbankintegration mit SQLite:

Die Datenbank wurde mit SQLite eingerichtet, um Benutzerinformationen sicher zu speichern und abzurufen.

7. Fehlerbehebung und Debugging:

Wir haben zahlreiche Programmierfehler identifiziert und behoben, was die Stabilität und Zuverlässigkeit der Anwendung erhöht hat.

8. Styling des Welcome Screens & des Login & Registration Screens:

Das Styling des Login und Registration Screens wurde wie vorgesehen implementiert. Der Welcome Screen wurde angepasst, da die Möglichkeit, ein Profilbild hinzuzufügen entfernt wurde. 

9. Dokumentation und ReadMe-Datei:

Eine umfassende Dokumentation und eine detaillierte ReadMe-Datei wurden erstellt, um die Installation, Nutzung und Beitragsrichtlinien der WebApp klar zu kommunizieren.

10. Einhaltung des Projektzeitplans:

Trotz einiger Herausforderungen und Anpassungen konnten wir den Projektzeitplan einhalten unter einigen Absprichen erreichen.

## Missed Goals

1. Push-Benachrichtigungen:

Die Implementierung von Push-Benachrichtigungen für wichtige Ereignisse wie, dass der Benutzer einen neuen Match hat, wurde aufgrund technischer Herausforderungen und Zeitmangels nicht realisiert. Stattdessen, haben wir Alerts anstatt Push-Benachrichtigungen eingebaut.

2. Suchfunktion:

Die Einrichtung von einer Suchfunktion, mittels Benutzer andere Benutzer mittels der Studenten Email leichter finden können, wurde aufgrund des Zeitmangels nicht umgesetzt.

3. Benutzerprofile:

Benutzerprofile, mittels die Benutzer einen besseren Einblick über deren gespeicherten Daten erhalten können, wurde ebenfalls aufgrund von Zeitmangel nicht umgesetzt. 

4. Filter:

Filter, mittels Benutzer gezielt nach anderen Benutzern, die deren Vorstellungen bzw. Vorraussetzungen entsprechen suchen können. 
Die Filter wurden nicht umgesetzt, da wir eine zu kleine UserBase haben und sich das somit sowohl zeitlich als auch Ressourcenbedingt nicht lohnen würde. Diese Funktion wäre jedoch, eine gute Addition zum Matching. Bei einer steigenden Nutzeranzahl, wäre dies durchaus sinnvoll. 

5. Emoji Button:

Innerhalb von der Chat Funktion, wollten wir dem Benutzer die Möglichkeit geben, sich durch Emojis noch besser auszudrücken. 
Leider, hat dies jedoch nicht funktioniert und aufgrund von anderen Priorisierungen, wie Backend, insbesondere die Umsetzung vom Matchmaking wurde diese Funtkion entfernt.

6. Keine Profilbilder:

Die Implementierung von Profilbildern in der StudyBuddy-WebApp wurde aufgrund technischer Herausforderungen und Zeitmangels nicht abgeschlossen. Diese Funktion hätte die Benutzerprofile individueller und ansprechender gestaltet, konnte jedoch nicht rechtzeitig fertiggestellt werden.

7. Password Reset:

Obwohl, Passwörter in der Datenbank geändert werden, nachdem der Benutzer sein neues Passwort mittles dem Password Reset Link eingegeben hat, wird das bei dem Login nicht mehr berücksichtigt. Gecheckt wurden die Password Hash Methoden und auch alle definierten Funktionen. Leider konnten wir jedoch hierbei aufgrund von Zeitmangel den Fehler nicht lösen. Das gleiche Problem gibt es auch bei der Registrierung, wobei wenn der Benutzer da sein Passwort festlegt wird es dann beim Login Verusuch als "falsch" erkannt. 
--> Workaround: Wir haben herausgefunden, dass man die hashed passwords von den Nutzern "Dzhan Nezhdet" oder "Kadir Aksoy" übernimmt und das selbst in der database.db Datei ändert, man sich problemlos einloggen kann. 

Die Anmeldedaten für den Account "Dzhan Nezhdet" sind:
Email: s_nezhdet22@stud.hwr-berlin.de
Passwort: 123456789

Die Anmeldedaten für den Account "Kadir Aksoy" sind: 
Email: s_aksoy22@stud.hwr-berlin.de
Passwort: 23456789

8. Chat Style:

Leider wurde das Styling nicht wie in der Präsentation gezeigt desinged, da wir den Fokus auf die Implementierung der Funktionen gesetzt haben und den Umfang des stylings unterschätzt haben. 


