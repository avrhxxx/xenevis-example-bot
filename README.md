# Simple Xenevis Telegram Bot

This branch contains the first real SDK-native Telegram bot for Xenevis.

The goal is to validate the public SDK path in a real bot:

```text
Telegram update
→ xenevis.telegram.polling()
→ Xenevis Runtime
→ handler
→ xenevis.telegram.ui(...)
→ Telegram delivery
```

## What this bot tests

- `xenevis.telegram.command("start")`
- `xenevis.telegram.callback(...)`
- `xenevis.telegram.ui(...)`
- inline buttons
- Runtime handler execution
- Runtime output capture
- Telegram rendering and polling delivery

## What this bot must not do

This bot intentionally does not implement its own Telegram transport, router, polling loop, or `sendMessage` calls.

Those responsibilities belong to the Xenevis SDK.

## Files

```text
bot.py
requirements.txt
.gitignore
```

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a local `.env` file and set the Telegram bot token variable expected by Xenevis SDK.

Then run:

```bash
python bot.py
```

## Expected bot flow

```text
/start
→ Start screen
→ Help button
→ Help screen
→ About button
→ About screen
→ Back button
→ Start screen
```

## Status

Foundation validation branch. This is not a final product bot.
