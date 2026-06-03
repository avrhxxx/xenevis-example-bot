# Xenevis Example Bot

This repository is a branch-based laboratory for real Telegram bots built with Xenevis SDK.

`main` intentionally stays neutral and does not contain a bot implementation.

Each bot type lives on its own branch.

## Bot branches

- `bot-casedesk` — support cases, complaints, operator workflow
- `bot-booking` — appointment booking and scheduling flows
- `bot-lead-intake` — business lead intake and owner notification
- `bot-ecommerce-returns` — returns, complaints, order support, evidence intake
- `bot-community-manager` — group/community management and admin flows
- `bot-personal-assistant` — personal tasks, notes, lightweight workflows

## Rule

Every branch should behave like an independent real bot, not like an artificial test suite.
