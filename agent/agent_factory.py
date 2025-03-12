# agent/agent_factory.py
from browser_use.agent.service import Agent

from allure.step_logger import StepLogger
from allure.reporter import AllureReporter
from config.llm import LLMConfigFactory
from context.browser_context import BrowserContextManager


class AgentFactory:
    def __init__(self, reporter=None):
        self.reporter = reporter or AllureReporter()

    @staticmethod
    def create_agent(task, llm_config=None, browser_manager=None, reporter=None):
        browser_manager = browser_manager or BrowserContextManager(step_logger=StepLogger())
        llm_config = llm_config or LLMConfigFactory.create_deepseek()
        agent = Agent(
            browser_context=browser_manager,
            task=task,
            llm=llm_config
            )
        agent.reporter = reporter
        return agent