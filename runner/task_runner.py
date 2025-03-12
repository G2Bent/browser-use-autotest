# runner/task_runner.py
from allure.reporter import AllureReporter
from agent.agent_factory import AgentFactory


class TaskRunner:
    def __init__(self, task_module, reporter=None):
        self.task = task_module.get_task()
        self.reporter = reporter or AllureReporter()

    def run(self):
        agent = AgentFactory.create_agent(
            self.task,
            reporter=self.reporter
            )
        result = agent.run()
        self.reporter.generate_report()
        return result