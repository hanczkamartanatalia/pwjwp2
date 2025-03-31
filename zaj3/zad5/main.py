class SimpleChatbot:
    def __init__(self, questions):
        self.questions = questions
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.questions):
            raise StopIteration
        question = self.questions[self.index]
        self.index += 1
        return question

if __name__ == "__main__":
    bot = SimpleChatbot(["Jak się nazywasz?", "Jaki jest Twój ulubiony kolor?"])
    for question in bot:
        print(question)
        input()
