#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author : bw.ling
create_time : 2025/3/12
"""
import os

from langchain_openai import ChatOpenAI

class LLMConfigFactory:
    @staticmethod
    def create_deepseek():
        return ChatOpenAI(
            base_url='https://api.deepseek.com/v1',
            model='deepseek-chat',
            api_key=os.getenv('DEEPSEEK_API_KEY')
        )