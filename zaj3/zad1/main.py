from zaj3.zad1.generator import Generator
from zaj3.zad1.intelligent_assistant import IntelligentAssistant
from zaj3.zad1.lang_analyzer import LangAnalyzer

lang_analyzer = LangAnalyzer()
generator = Generator(lang_analyzer)
intelligent_assistant = IntelligentAssistant(generator, '1')

print(intelligent_assistant.generator.generate('aa'))
