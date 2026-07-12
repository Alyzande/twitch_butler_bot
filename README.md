# Twitch Butler Bot

A charming, deterministic Twitch bot that behaves like a discreet Victorian butler.

The Butler welcomes viewers, offers hospitality, fills quiet moments with gentle observations, and helps create a warm atmosphere in Twitch chat without dominating the conversation.

This project is intentionally designed to be lightweight, privacy-friendly and inexpensive to run. Rather than relying on AI for every response, the Butler uses carefully curated phrase libraries combined in interesting ways to create the illusion of personality.

---

## Current Features

- Connects securely to Twitch using EventSub
- Authenticates using OAuth
- Reads live Twitch chat
- Detects first-time chatters during a stream
- Maintains an in-memory guestbook
- Generates personalised greetings
- Loads greetings and drinks from JSON data files
- Separates application logic from personality content

---

## Planned Features

- Persistent guestbook (survives bot restarts)
- Welcome messages sent directly to Twitch chat
- Rolling end-of-stream guest credits
- Butler commands
- Random idle observations during quiet periods
- Curated joke library
- Multiple butler personalities
- Theme packs (Victorian, Sci-Fi, Christmas, Halloween, etc.)
- Optional AI personality upgrade
- Optional Text-to-Speech co-host mode

---

## Design Principles

The Butler should:

- Welcome guests politely.
- Never spam chat.
- Never dominate the streamer.
- Never remember viewers across streams without permission.
- Never rely on expensive AI APIs for core functionality.
- Be configurable through editable JSON files rather than code.

---

## Project Structure

```
twitchbutler/

butler/
    bot.py
    commands.py
    greetings.py
    guestbook.py
    personality.py
    silence.py

data/
    greetings.json
    drinks.json
    jokes.json
    coats.json

state/

app.py
config.py
requirements.txt
```

---

## Technology

- Python 3.13
- Twitch EventSub WebSockets
- twitchAPI
- python-dotenv

---

## Project Status

Early development.

The current prototype successfully:

- connects to Twitch,
- listens to live chat,
- records new guests,
- generates greetings using JSON-driven content.

---

## Philosophy

This project intentionally begins as a deterministic system rather than an AI chatbot.

The goal is to create a bot with character through thoughtful software design, reusable phrase libraries and careful timing instead of sending every interaction to a language model.

AI may be introduced later as an optional enhancement rather than a requirement.

---

## Author

Created by Alyzande

https://www.alyzande.co.uk
https://www.twitch.tv/butlerservice
