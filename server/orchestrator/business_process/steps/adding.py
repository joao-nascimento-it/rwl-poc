from rwl_core import Injector
from server.bots.adder import AdderBot
from server.bots.printer import PrinterBot
from server.orchestrator.business_process.steps.abstract import AbstractStep


class AddingStep(AbstractStep):
    def execute(self) -> None:
        self.__add_lhs_and_rhs()
        self.__print_sum()

    def __add_lhs_and_rhs(self):
        adder_bot = Injector.inject(AdderBot)
        self.pipeline.result = adder_bot.add(self.pipeline.lhs, self.pipeline.rhs)

    def __print_sum(self):
        printer_bot = Injector.inject(PrinterBot)
        printer_bot.print(
            f"{self.pipeline.step} > {self.pipeline.lhs} + {self.pipeline.rhs} = {self.pipeline.result}"
        )
