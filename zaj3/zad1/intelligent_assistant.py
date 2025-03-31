from zaj3.zad1.asistant import Assistant
from zaj3.zad1.generator import Generator


class IntelligentAssistant(Assistant):
    def __init__(self, generator: Generator, version):
        super().__init__('IntelligentAssistant', version)
        self.generator = generator
