from rwl_core import Injector
from server.bots.multiplier import MultiplierBot
from server.bots.printer import PrinterBot
from server.orchestrator.business_process.steps.abstract import AbstractStep


class MultiplingStep(AbstractStep):
    def execute(self) -> None:
        initial = self.result
        self.__multiply_by_4()
        self.__print_multiplication(initial)

    def __multiply_by_4(self):
        multiplier_bot = Injector.inject(MultiplierBot)
        self.pipeline.result = multiplier_bot.multiply(self.result, 4)

    def __print_multiplication(self, initial: int):
        printer_bot = Injector.inject(PrinterBot)
        printer_bot.print(
            f"{self.pipeline.step} > {initial} * 4 = {self.pipeline.result}"
        )
