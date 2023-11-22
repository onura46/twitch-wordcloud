# twitch-wordcloud

This program logs into a Twitch channel, captures chat into a text file, and converts the most used words into a wordcloud. You can also mask the output with an input image.

Uses [word_cloud](https://github.com/amueller/word_cloud) and matplotlib. See `requirements.txt` for full requirements. 

## Instructions

Please change configuration options in `config.py`. It's recommended that any images you intend to use as a mask be between 500 and 1000px on an edge. Use the `SCALE` parameter to adjust this, if needed.

It's recommended - though OPTIONAL - to run all this from a virtual environment. Below are directions for Windows. For other operating systems, you may check out this link: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

1. Download this entire repo or `git clone` it into an empty directory.
2. Run a command prompt from this folder. 
3. (OPTIONAL) Set up a virtual environment: `python -m venv venv`
4. (OPTIONAL) Activate the virtual environment: `.\venv\Scripts\activate` or `python venv\Scripts\activate`
5. Install packages from requirements: `pip install -r requirements.txt`
6. Run `main.py` from your IDE, or use `python main.py` from a command line.

## Controls

Pause and Create Chart - "Shift+Backspace"

You may reconfigure this button in `TwitchPlays_TTS_READER.py`.

## License

Includes and modifies elements of https://github.com/DougDougGithub/TwitchPlays

Please see the included LICENSE for details on all other files.

## Issues

This repository is uploaded mostly for demonstration purposes and personal use, but pull requests and issues are welcome. Please give me some time to respond.

![wordcloud](https://github.com/onura46/twitch-wordcloud/assets/67405765/0480b5b2-a6cd-4bef-b580-d8db9e8b389f)
