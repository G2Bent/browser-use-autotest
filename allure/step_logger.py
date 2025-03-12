#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author : bw.ling
create_time : 2025/3/12
"""
from allure import step, title
from context.browser_context import BrowserContextManager


class StepLogger:
    def __init__(self, browser_manager):
        self.browser_manager = browser_manager

    @title("Initialize Test Environment")
    def log_init(self):
        with self.browser_manager as ctx:
            step("Starting browser with config: {}".format(ctx.config))

    @title("Execute Test Task")
    def log_task_execution(self, task):
        step("Executing task: {}".format(task[:30]))