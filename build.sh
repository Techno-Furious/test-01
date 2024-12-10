#!/usr/bin/env bash
# Install Playwright and its dependencies
pip install -r requirements.txt
playwright install --with-deps
sudo apt update
sudo apt install -y wget unzip
sudo apt install -y chromium-browser chromium-chromedriver
