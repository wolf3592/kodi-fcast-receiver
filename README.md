# FCast receiver add-on for Kodi

## FCast

FCast is an open source protocol that enables wireless streaming of audio and video content between devices, supporting various stream types such as DASH, HLS, and mp4.

Unlike proprietary protocols like Chromecast and AirPlay, FCast offers an open approach, empowering third-party developers to create their own receiver devices or integrate the FCast protocol into their own apps. 

Official web site: [fcast.org](https://fcast.org)

## Receiver

This add-on is an unofficial FCast receiver for Kodi. It allows you to stream content from any FCast client to Kodi media center.

## Status

The original addon by c4valli has not been updated for over 9 months and is currently non-functional. This fork aims to:
- Restore functionality by fixing broken features.
- Ensure compatibility with the latest Kodi versions (e.g., Kodi 21 "Omega").
- Provide ongoing maintenance and updates.

## Acknowledgments
- Original creator: [c4valli](https://github.com/c4valli/kodi-fcast-receiver) 

## Development Environment
1. Create virtual environment
```bash
python -m venv venv
```
2. Activate virtual environment
```bash
source ./venv/bin/activate
```
3. Install required modules
```bash
pip install -U mpv kodistubs
```
