#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author : bw.ling
create_time : 2025/3/12
"""
import os

from browser_use import BrowserConfig

class BrowserConfigFactory:
    @staticmethod
    def create_default():
        return BrowserConfig(
            # 可扩展的默认配置
            chrome_instance_path=os.getenv('CHROME_PATH', ''),
            headless=False
        )