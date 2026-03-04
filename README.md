# ViberChatbot (Uzbunko)

A Flask-based Viber bot server with a plugin architecture for infrastructure automation, IoT control, and monitoring — built for sysadmin use cases.

## What It Does

The bot acts as a messaging interface to your server infrastructure. Users send commands via Viber and receive responses from plugins — server status, temperatures, camera snapshots, employee schedules, parking info, UPS status, and more. Access to each plugin is granted per-user via filesystem symlinks, so different users see different capabilities.

Additionally, the bot exposes a webhook endpoint compatible with Alertmanager (and similar tools), so it can receive infrastructure alerts and forward them to Viber instead of Telegram or Slack.

## Architecture

```
viberChatbot.py          # Main Flask app (Blueprint), Viber webhook handler
plugins/                 # Plugin library — one .py file per command
    ping.py              # Ping a list of hosts, report UP/DOWN
    temp.py              # Query server room temperature sensor
    smene.py             # Employee schedule (next 7 days)
    skamere.py           # IP camera live snapshot
    radijacija.py        # Radiation sensor readout
    dust.py              # Air quality visualization from MRTG
    ups.py               # UPS status
    jelovnik.py          # Canteen menu
    racun.py             # Account/billing info
    link.py              # Quick links
    ...                  # Add your own
users/
    u<md5_of_viber_id>/  # Per-user privilege directory
        -> symlink to plugin   # User can call this plugin
script/
    sendViber.py         # CLI tool: send a Viber message from command line
    viberhook.py         # Helper: register/update the Viber webhook
    viberhook_443.py     # Same, for port 443
```

## How Plugins Work

Each plugin is a Python file with a `rep(text)` generator function:

```python
from viberbot.api.messages.text_message import TextMessage

def rep(text):
    if text.lower().startswith('temp'):
        yield TextMessage(text=get_temperature())
        yield 'stop_'   # stop processing further plugins
```

The bot iterates through all plugins the user has access to. If the user types `help` or `info`, it lists available plugin names instead of executing them.

## User Privileges

Access control is filesystem-based. To grant a user access to a plugin:

```bash
# 1. Create user directory (Viber ID hashed with MD5)
mkdir users/u$(python3 -c "import hashlib; print(hashlib.md5('VIBER_USER_ID'.encode()).hexdigest())")

# 2. Symlink the plugin into that directory
cd users/u<hash>/
ln -s ../../plugins/ping.py
```

Users with no symlinks for a given command get a friendly default reply (required by Viber's 5-second response timeout).

## Setup

### Requirements

```bash
pip install flask viberbot requests lxml
```

### Configuration

Edit `viberChatbot.py` and set:

```python
auth_token = 'YOUR_VIBER_BOT_TOKEN'   # from developers.viber.com
NESHA = 'YOUR_VIBER_ID_BASE64'         # admin user ID
```

User IDs are stored as `hashlib.md5(viber_id.encode()).hexdigest()` for the directory name.

### Register Webhook

```bash
python script/viberhook.py
# or for port 443:
python script/viberhook_443.py
```

Your server must be reachable over HTTPS (Viber requires a valid SSL certificate).

### Run

```python
# viberChatbot.py is a Flask Blueprint — mount it in your main Flask app:
from viberChatbot import uzbunkoBot
app.register_blueprint(uzbunkoBot)
```

Or use the commented-out standalone block at the bottom of `viberChatbot.py` to run directly with SSL:

```python
context = ('server.crt', 'server.key')
app.run(host='0.0.0.0', port=8080, debug=True, ssl_context=context)
```

## Sending Messages from the CLI / Scripts

```bash
python script/sendViber.py "Server is back up" NESHA USER2
```

Or via HTTP POST from any script or monitoring tool:

```bash
curl -X POST https://yourserver:8080/send \
  -H "Content-Type: application/json" \
  -d '{"password":"your_password","recipients":["NESHA"],"text":"Disk usage at 95%"}'
```

## Generic Webhook → Viber Notification Bridge

A lightweight webhook endpoint that receives generic HTTP POST alerts (e.g. Alertmanager/Prometheus, Grafana, Zabbix, and other monitoring systems) and forwards notifications to Viber.

```yaml
# alertmanager.yml
receivers:
  - name: viber
    webhook_configs:
      - url: 'https://yourserver:8080/ALERTMyourpassword'
```

Replace the route path with your own secret. The endpoint parses alert `status`, `labels`, and `annotations` and formats them into a readable Viber message sent to the admin user.

## Writing a Plugin

Create a new file in `plugins/`:

```python
# plugins/mycheck.py
from viberbot.api.messages.text_message import TextMessage

def rep(text):
    if text.lower().startswith('mycheck'):
        result = run_my_check()
        yield TextMessage(text=result)
        yield 'stop_'
```

Then symlink it into user directories as needed. The plugin name (minus `.py`) appears in the `help` output.

## Notes

- Built on the [Viber Python Bot API](https://developers.viber.com/docs/api/python-bot-api/)
- Duplicate message detection via `message_token` set
- Rolling log of last 50 non-admin messages, viewable by admins with `log` command
- Originally written for internal sysadmin use at a broadcast/ISP infrastructure environment

## Author

Nebojsa Milovanovic

