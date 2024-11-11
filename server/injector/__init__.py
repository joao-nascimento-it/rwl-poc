from rwl_core import Injector

from server.bots.adder import AdderBot
from server.bots.multiplier import MultiplierBot
from server.bots.printer import PrinterBot
from server.bots.subtractor import SubtractorBot
from server.orchestrator import Orchestrator


INJECTOR = Injector(
    dependencies={
        AdderBot: lambda: AdderBot(),
        MultiplierBot: lambda: MultiplierBot(),
        PrinterBot: lambda: PrinterBot(),
        SubtractorBot: lambda: SubtractorBot(),
        Orchestrator: lambda: Orchestrator(),
    },
)
