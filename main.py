# main.py
import os

from dotenv import load_dotenv
from runner.task_runner import TaskRunner
from allure.reporter import AllureReporter
from tasks.example import get_task

load_dotenv()

if __name__=="__main__":
    # 初始化Allure报告
    reporter = AllureReporter(
        output_dir=os.getenv('ALLURE_OUTPUT_DIR', 'allure-results')
        )

    # 运行任务并生成报告
    task_runner = TaskRunner(
        get_task(),
        reporter=reporter
        )

    result = task_runner.run()

    # 打印生成的报告路径
    print("Allure reports generated at:")
    for fmt, path in reporter.generate_report():
        print(f"- {fmt}: {path}")