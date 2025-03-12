#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author : bw.ling
create_time : 2025/3/12
"""
# allure/reporter.py
import allure
from pathlib import Path


class AllureReporter:
    def __init__(self, output_dir="allure-results"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        allure.init(output_dir=str(self.output_dir))

    def generate_report(self):
        # 生成PDF/HTML报告
        return [
            ("html", f"{self.output_dir}/index.html"),
            ("pdf", f"{self.output_dir}/report.pdf")
            ]

    @staticmethod
    def attach_file(name, content, attachment_type):
        with open(f"{AllureReporter.output_dir}/{name}", "wb") as f:
            f.write(content)
        allure.attach_file(
            name,
            f"{AllureReporter.output_dir}/{name}",
            attachment_type=attachment_type
            )