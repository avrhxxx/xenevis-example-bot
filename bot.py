# bot.py
# Simple SDK-native Telegram bot built with Xenevis.

import xenevis
from xenevis.telegram import button


xenevis.configure(
    observer=xenevis.observer.console(format="native")
)


@xenevis.telegram.command("start")
async def start(ctx):
    return xenevis.telegram.ui(
        screen="Start",
        text=(
            "Welcome to the Simple Xenevis Telegram Bot.\n\n"
            "This bot validates the SDK-native Runtime path:\n"
            "Telegram update → Xenevis Event → Runtime → UI output.\n\n"
            "Observer is enabled, so Runtime signals should appear in the console."
        ),
        inline=[
            button.callback("Run SDK demo", "demo.run"),
            button.callback("Help", "help.open"),
            button.callback("About", "about.open"),
        ],
    )


@xenevis.telegram.callback("start.open")
async def open_start(ctx):
    return xenevis.telegram.ui(
        screen="Start",
        text="Back on the start screen. Observer remains attached to Runtime signals.",
        inline=[
            button.callback("Run SDK demo", "demo.run"),
            button.callback("Help", "help.open"),
            button.callback("About", "about.open"),
        ],
    )


@xenevis.telegram.callback("demo.run")
async def run_demo(ctx):
    return xenevis.telegram.ui(
        screen="DemoResult",
        text=(
            "SDK demo executed.\n\n"
            "What happened:\n"
            "1. Telegram callback became a XenevisEvent.\n"
            "2. Runtime resolved this handler.\n"
            "3. Handler returned a Telegram UI component.\n"
            "4. Runtime captured output in the trace.\n"
            "5. Telegram renderer delivered the response.\n\n"
            "Check the console observer output for Runtime signals."
        ),
        inline=[
            button.callback("Run again", "demo.run"),
            button.callback("Back", "start.open"),
        ],
    )


@xenevis.telegram.callback("help.open")
async def open_help(ctx):
    return xenevis.telegram.ui(
        screen="Help",
        text=(
            "Available actions:\n\n"
            "• /start — open the start screen\n"
            "• Run SDK demo — validate Runtime flow\n"
            "• About — explain what this bot is testing\n\n"
            "The console observer should print Runtime signals while you interact with the bot."
        ),
        inline=[
            button.callback("Run SDK demo", "demo.run"),
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
            "No custom Telegram polling, router, or sendMessage code lives in the bot.\n"
            "Those responsibilities belong to the SDK.\n\n"
            "Observer is passive: it describes execution through signals, "
            "but it does not control Runtime execution."
        ),
        inline=[
            button.callback("Run SDK demo", "demo.run"),
            button.callback("Back", "start.open"),
            button.callback("Help", "help.open"),
        ],
    )


if __name__ == "__main__":
    xenevis.telegram.polling().run()
