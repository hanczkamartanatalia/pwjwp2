from zaj2.zad1.audiobook import Audiobook
from zaj2.zad1.ebook import Ebook

ebook = Ebook('dd', 'Anna', '2001', '3')
audiobook = Audiobook('ss', 'Ewa', '2011', '5')

print(ebook.desc())
print(audiobook.desc())
