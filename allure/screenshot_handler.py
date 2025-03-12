#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author : bw.ling
create_time : 2025/3/12
"""
# allure/screenshot_handler.py
from browser_use import Browser
import base64
from pathlib import Path

def capture_screenshot(browser: Browser):
    screenshot = browser.screenshot()
    return base64.b64encode(screenshot).decode('utf-8')