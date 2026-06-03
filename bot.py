# bot.py
# Simple SDK-native Telegram bot built with Xenevis.

from __future__ import annotations

import xenevis
from xenevis.telegram import button


@xenevis.telegram.command("start")
async def start(ctx):
    return xenevis.telegram.ui(
        screen="Start",
        text=(
            "Welcome to the Simple Xenevis Telegram Bot.\n\n"
            "This bot validates the SDK-native Telegram path:\n"
            "command → Runtime → UI output → Telegram delivery."
        ),
        inline=[
            button.callback("Help", "help.open"),
            button.callback("About", "about.open"),
        ],
    )


@xenevis.telegram.callback("start.open")
async def open_start(ctx):
    return xenevis.telegram.ui(
        screen="Start",
        text="Back on the start screen.",
        inline=[
            button.callback("Help", "help.open"),
            button.callback("About", "about.open"),
        ],
    )


@xenevis.telegram.callback("help.open")
async def open_help(ctx):
    return xenevis.telegram.ui(
        screen="Help",
        text=(
            "Available actions:\n\n"
            "• /start — open the start screen\n"
            "• Help — show this screen\n"
            "• About — show SDK path information"
        ),
        inline=[
            button.callback("Back", "start.open"),
            button.callback("About", "about.open"),
        ],
    )


@xenevis.telegram.callback("about.open")
async def open_about(ctx):
    return xenevis.telegram.ui(
        screen="About",
        text=(
            "This example intentionally uses only public Xenevis SDK APIs.\n\n"
            "No custom Telegram polling, router, or sendMessage code lives in the bot."
        ),
        inline=[
            button.callback("Back", "start.open"),
            button.callback("Help", "help.open"),
        ],
    )


if __name__ == "__main__":
    xenevis.telegram.polling().run()
