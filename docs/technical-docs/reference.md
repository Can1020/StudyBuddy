---
title: Reference
parent: Technical Docs
nav_order: 3
---

{: .label }
[Dzhan Nezhdet]

{: .no_toc }
# Reference documentation

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## Benutzerverwaltung

### `load_user(user_id)`

**Route:** `/`

**Methoden:** `GET` `POST`

**Zweck:** Lädt den Benutzer anhand der Benutzer-ID, um den aktuellen Benutzer für die Sitzung zu setzen.

**Beispielausgabe:** `User object`

---

### `logout()`

**Route:** `/logout`

**Methoden:** `GET`

**Zweck:** Loggt den aktuellen Benutzer aus und leitet zur Login-Seite weiter.

**Beispielausgabe:** ![`Redirect to /login`](../assets/images/redirect_to_login.png)


---

### `login()`

**Route:** `/`

**Methoden:** `GET` `POST`

**Zweck:** Authentifiziert den Benutzer und loggt ihn ein, wenn die Anmeldeinformationen korrekt sind.

**Beispielausgabe:** `Redirect to /welcome`

---

### `welcome()`

**Route:** `/welcome`

**Methoden:** `GET`

**Zweck:** Zeigt eine Begrüßungsseite mit einer Liste von Benutzern und möglichen Übereinstimmungen an.

**Beispielausgabe:** ![`/welcome`](../assets/images/welcome.png)

---

### `forgot_password()`

**Route:** `/forgot_password`

**Methoden:** `GET` `POST`

**Zweck:** Sendet einen Link zum Zurücksetzen des Passworts an die E-Mail des Benutzers, wenn diese existiert.

**Beispielausgabe:** ![`/forgot_password`](../assets/images/forgot_password.png)

---

### `reset_password(token)`

**Route:** `/reset_password/<token>`

**Methoden:** `GET` `POST`

**Zweck:** Ermöglicht dem Benutzer das Zurücksetzen des Passworts, wenn ein gültiger Token bereitgestellt wird.

**Beispielausgabe:** ![`/reset_password`](../assets/images/reset_password.png)

---

### `register()`

**Route:** `/register`

**Methoden:** `GET` `POST`

**Zweck:** Registriert einen neuen Benutzer und speichert die Informationen in der Datenbank.

**Beispielausgabe:** ![`/register`](../assets/images/register.png) --> `Redirect to /login`

---

### `like_user()`

**Route:** `/like`

**Methoden:** `POST`

**Zweck:** Markiert einen Benutzer als "geliked" und erstellt eine Übereinstimmung, wenn der andere Benutzer ebenfalls "geliked" hat.

**Beispielausgabe:** `Adding user_id and liked_user_id into Database`

---

### `dislike_user(user_id)`

**Route:** `/dislike/<int:user_id>`

**Methoden:** `POST`

**Zweck:** Markiert einen Benutzer als "nicht geliked" und leitet zur Begrüßungsseite weiter.

**Beispielausgabe:** `Redirect to /welcome`

---

### `matches()`

**Route:** `/matches`

**Methoden:** `GET`

**Zweck:** Zeigt eine Liste der Übereinstimmungen des aktuellen Benutzers an.

**Beispielausgabe:** ![`/matches`](../assets/images/your_matches.png)

---

### `chat(match_id)`

**Route:** `/chat/<int:match_id>`

**Methoden:** `GET`

**Zweck:** Zeigt den Chat mit einem Übereinstimmungsbenutzer an.

**Beispielausgabe:** ![`/chat`](../assets/images/chat.png)

---

### `handle_send_message(data)`

**SocketIO-Event:** `send_message`

**Zweck:** Handhabt das Senden einer Nachricht im Chat und speichert sie in der Datenbank.

**Beispielausgabe:** `Emit receive_message Event`

---

### `handle_join(data)`

**SocketIO-Event:** `join`

**Zweck:** Fügt den Benutzer einem Chatraum hinzu.

**Beispielausgabe:** `None`

---

### `handle_leave(data)`

**SocketIO-Event:** `leave`

**Zweck:** Entfernt den Benutzer aus einem Chatraum.

**Beispielausgabe:** `None`

---