#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author : bw.ling
create_time : 2025/3/12
"""
from browser_use import Browser, BrowserContextConfig
from browser_use.browser.context import BrowserContext
from allure.screenshot_handler import capture_screenshot
from allure.step_logger import StepLogger

from config.browser import BrowserConfigFactory


class BrowserContextManager:
    def __init__(self, config=None,step_logger=None):
        self.config = config or BrowserConfigFactory.create_default()
        self.step_logger = step_logger or StepLogger(BrowserContextManager())


    def create_context(self):
        browser = Browser(config=self.config)
        ctx_config = BrowserContextConfig(
            locale='en-US',
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64)...',
            highlight_elements=True,
        screenshot_handler = capture_screenshot
            )
        return BrowserContext(browser=browser, config=ctx_config)

    def __enter__(self):
        self.ctx = self.create_context()
        return self.ctx

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.ctx.close()