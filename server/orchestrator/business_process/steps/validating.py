from rwl_core import Injector
from server.bots.printer import PrinterBot
from server.orchestrator.business_process.steps.abstract import AbstractStep


class ValidatingStep(AbstractStep):
    def execute(self) -> None:
        self.__validate()
        self.__print()

    def __validate(self): ...

    def __print(self):
        printer_bot = Injector.inject(PrinterBot)
        printer_bot.print(f"{self.pipeline.step} > {self.pipeline.result}")
