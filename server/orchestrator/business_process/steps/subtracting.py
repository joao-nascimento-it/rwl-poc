from rwl_core import Injector
from server.bots.printer import PrinterBot
from server.bots.subtractor import SubtractorBot
from server.orchestrator.business_process.steps.abstract import AbstractStep


class SubtractingStep(AbstractStep):
    def execute(self) -> None:
        initial = self.result
        self.subtract_result_by_15()
        self.__print_subtraction(initial)

    def subtract_result_by_15(self):
        subtractor_bot = Injector.inject(SubtractorBot)
        self.pipeline.result = subtractor_bot.subtract(self.result, 15)

    def __print_subtraction(self, initial: int):
        printer_bot = Injector.inject(PrinterBot)
        printer_bot.print(
            f"{self.pipeline.step} > {initial} - 15 = {self.pipeline.result}"
        )
