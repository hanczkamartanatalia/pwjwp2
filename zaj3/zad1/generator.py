from zaj3.zad1.lang_analyzer import LangAnalyzer


class Generator:
    def __init__(self, lang_analyzer: LangAnalyzer):
        self.lang_analyzer = lang_analyzer

    def generate(self, query):
        return self.lang_analyzer.analyze_query(query)
