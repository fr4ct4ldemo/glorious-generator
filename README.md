# Glorious — Discord Account Generator Bot

A feature-rich Discord bot for distributing digital accounts to your server members with role-based access, cooldowns, subscriptions, a review system, and a live stock tracker.

---

## Features

- **Account Generation** — Generate free or premium accounts via slash commands, delivered straight to DMs
- **Live Stock Tracker** — `/stock` auto-updates every 30 seconds in chat
- **Role-Based Access** — Restrict gen commands to specific roles with configurable cooldowns
- **Subscription System** — Time-based premium subscriptions with stage management
- **Blacklist System** — Block specific users from using the bot
- **Review System** — Users can submit star ratings and reviews after generating, with a like button
- **Bulk Gen** — Admins can generate multiple accounts at once as a `.txt` file
- **Per-Guild Config** — Every server gets its own isolated config, stock, and channels
- **Auto Welcome** — Sends a greeting embed when the bot joins a new server
- **Ticket System** — Built-in ticket support via `src/tickets.py`

---

## Requirements

- Python 3.10+
- discord.py 2.3.2
- aiosqlite 0.19.0
- SQLAlchemy 2.0.29
- aiohttp 3.9.5

Install all dependencies:

```bash
pip install -r requirements.txt
```

---

## Setup

**1. Clone the repo**

```bash
git clone https://github.com/fr4ct4ldemo/Glorious
cd Glorious
```

**2. Configure the bot**

Edit `config.json` — this is the only file you need to touch:

```json
{
    "token": "YOUR_BOT_TOKEN_HERE",
    "stock-command-silent": false,
    "remove-capture-from-stock": true,
    "commands-give-cooldown": true,
    "default_cooldown": 5,
    "stock-storage-path": "/stock_data",
    "subscription-stages": ["Free", "Premium"],
    "messages": {
        "altsent": "Thank you for using Glorious",
        "footer-msg": "Your footer text here"
    },
    "generate-settings": {
        "gif-img-url": "https://your-gif-url-here"
    },
    "maximum-file-size": 2097152
}
```

| Key | Description |
|---|---|
| `token` | Your Discord bot token |
| `stock-command-silent` | If `true`, `/stock` is only visible to the user who ran it |
| `remove-capture-from-stock` | Strip capture groups from accounts on add |
| `default_cooldown` | Fallback cooldown in seconds if no role cooldown is set |
| `stock-storage-path` | Folder path where stock `.txt` files are stored |
| `subscription-stages` | List of subscription tiers (first = free tier) |
| `maximum-file-size` | Max upload size for `/addstock` in bytes (default 2MB) |

**3. Run the bot**

```bash
python glorious.py
```

---

## Slash Commands

### Stock & Generation

| Command | Description | Access |
|---|---|---|
| `/gen <service> [is_premium]` | Generate an account from stock, delivered via DM | Members |
| `/stock` | View live stock count (auto-updates every 30s) | Members |
| `/addstock <service> <file> [is_premium] [is_silent]` | Upload a `.txt` file of accounts to stock | Admin |
| `/bulkgen <service> <amount> <is_premium> [is_silent]` | Generate multiple accounts as a file | Admin |
| `/clearservice <service> [is_premium]` | Delete a service and all its stock | Admin |

### User Management

| Command | Description | Access |
|---|---|---|
| `/user <user>` | View a user's gen stats, subscription, and notes | Admin |
| `/blacklist <user> [status]` | Blacklist or unblacklist a user | Admin |
| `/setnote <user> <note>` | Attach a note to a user's profile | Admin |

### Subscription

| Command | Description | Access |
|---|---|---|
| `/subscription add <user> <time_sec>` | Add subscription time to a user | Admin |

### Cooldown

| Command | Description | Access |
|---|---|---|
| `/cooldown reset <user>` | Reset a user's free and premium cooldowns | Admin |
| `/cooldown set <user> <stage> <seconds>` | Manually set a user's cooldown | Admin |

### Setup & Config

| Command | Description | Access |
|---|---|---|
| `/setup genchannel <channel>` | Add a channel where `/gen` is allowed | Admin |
| `/setup premiumchannel <channel>` | Add a premium-only gen channel | Admin |
| `/setup adminrole <role>` | Add a bot admin role | Admin |
| `/setup freerole <role> <cooldown> <remove_if_expired>` | Configure a free member role | Admin |
| `/setup premiumrole <role> <cooldown> <remove_if_expired>` | Configure a premium member role | Admin |
| `/setup suggestions <channel>` | Set the suggestions channel | Admin |
| `/setup reviewchannel <channel>` | Set the channel where reviews are posted | Admin |
| `/setup view` | View current server configuration | Admin |

---

## File Structure

```
glorious.py          — Main bot file, all commands and events
config.json          — Bot configuration (edit this)
guilds.json          — Auto-generated per-guild config storage
run.py               — Entry point
requirements.txt     — Python dependencies

src/
  database.py        — SQLite database logic (users, stock, cooldowns)
  guild_config.py    — Per-guild config loader/saver
  stock_files.py     — File-based stock management
  tickets.py         — Ticket system
  reviews.py         — Review system helpers
  utils.py           — Role requirement checker

stock_data/
  <guild_id>/        — Stock .txt files stored per guild per service

dashboard/           — Optional web dashboard
```

---

## Adding Stock

1. Create a `.txt` file with one account per line, e.g.:
```
email@example.com:password123
user2@mail.com:pass456
```

2. Run `/addstock` in Discord, select the service name, and upload the file.

The bot supports both file-based stock (`stock_data/`) and database stock simultaneously — it pulls from files first, then falls back to the database.

---

## Admin Role vs Server Admin

A user counts as an admin if they have:
- Discord's built-in **Administrator** permission, **OR**
- A role that was added via `/setup adminrole`

Admins bypass cooldowns, channel restrictions, subscription checks, and blacklists.

---

## Notes

- Slash commands may take up to **1 hour** to appear globally after first adding the bot. Restart Discord if they're missing.
- Do **not** modify `glorious.py` unless you know what you're doing — all configuration is in `config.json`.
- Stock files are stored in the path set by `stock-storage-path` in config, organized by `<guild_id>/<service_name>.txt`.

---

## Credits

Glorious was developed by **fr4ct4ldemo**.

> ⚠️ **Disclaimer:**
this source does not violate discord's terms of service. glorious operates within the boundaries set by discord's developer policy and community guidelines. we do not engage in any activity that promotes account abuse, unauthorized access, or any other conduct prohibited by discord.

> ⚠️ **Do not remove or modify the credits.** Removing or altering the original credit will result in a **permanent blacklist** from updates, support, and future releases.
