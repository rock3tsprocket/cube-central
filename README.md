# Cube Central
This repository hosts a reimplementation of (some of) [goober central](https://github.com/gooberinc/goober-central)'s features

# Implementation status

- [x] Alive pings
- [x] Alerts
- [x] Version checking
- [ ] Token authentication (probably won't be implemented, at least by me)

# How to use

For the official instance of cube central, just set the version URL to "http://cube.rockpie.frii.site:6008" in your bot's configuration:
- In mainline goober (if you even have an old enough version to support goober central), set "VERSION\_URL" in `config.py` to the previously mentioned value, or
- In [cube](https://github.com/rock3tsprocket/cube) versions 0.10.4.6.6-alternate and beyond, modify (or add) a variable named "version\_url" to the previously mentioned value.

> [!NOTE]
> For unofficial instances, do the same thing but replace the version URL with your own.

> [!NOTE]
> For bots other than the ones mentioned, you're on your own.

## Self-hosting set-up

# Configuration

- Rename the file named `example.env` to `.env` and modify the values in it to what you need.
- Run `pip install -r requirements.txt` to install any dependencies (you may need a virtual environment)
- Run the main.py script (`python3 main.py`)

## Version checking

1. Modify the file named `latest_version.json` in the folder named `static` to fit your needs.
2. If desired, add the latest version of your bot to `static/goob`

> [!IMPORTANT]
> Unless you're mirroring the official central server, do not use the `latest_version.json` in `static/` as-is.

## Hosting a webpage

TODO: complete this


By the way, yes i know the official server uses HTTP, i can't be bothered to set up SSL
