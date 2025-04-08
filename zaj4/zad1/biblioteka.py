"""Moduł zawiera prosty system zarządzania biblioteką."""
class Ksiazka: # pylint: disable=too-few-public-methods
    """
    Reprezentuje książkę w bibliotece.
    """

    def __init__(self, tytul: str, autor: str, dostepna: bool = True):
        self.tytul = tytul
        self.autor = autor
        self.dostepna = dostepna

    def __str__(self) -> str:
        return f"{self.tytul} – {self.autor}"

class Biblioteka:
    """
    Prosty system zarządzania biblioteką.
    """

    def __init__(self):
        self.lista_ksiazek: list[Ksiazka] = []

    def dodaj_ksiazke(self, ksiazka: Ksiazka) -> None:
        """
        Dodaje książkę do biblioteki.
        """
        self.lista_ksiazek.append(ksiazka)

    def wypozycz_ksiazke(self, tytul: str) -> str:
        """
        Wypożycza książkę na podstawie tytułu.
        """
        for ksiazka in self.lista_ksiazek:
            if ksiazka.tytul == tytul:
                if ksiazka.dostepna:
                    ksiazka.dostepna = False
                    return f"Wypożyczono: {tytul}"
                return f"Książka {tytul} niedostępna"
        return f"Brak książki: {tytul}"

    def zwroc_ksiazke(self, tytul: str) -> str:
        """
        Zwraca książkę do biblioteki.
        """
        for ksiazka in self.lista_ksiazek:
            if ksiazka.tytul == tytul:
                ksiazka.dostepna = True
                return f"Zwrócono: {tytul}"
        return f"Nie należy do biblioteki: {tytul}"

    def dostepne_ksiazki(self) -> list[str]:
        """
        Zwraca listę dostępnych książek.
        """
        return [
            ksiazka.tytul
            for ksiazka in self.lista_ksiazek
            if ksiazka.dostepna
        ]


def main() -> None:
    """Funkcja testująca działanie systemu bibliotecznego."""
    biblioteka = Biblioteka()
    biblioteka.dodaj_ksiazke(Ksiazka("Wiedźmin", "Sapkowski"))
    biblioteka.dodaj_ksiazke(Ksiazka("Solaris", "Lem"))
    biblioteka.dodaj_ksiazke(Ksiazka("Lalka", "Prus", dostepna=False))

    print(biblioteka.wypozycz_ksiazke("Solaris"))
    print(biblioteka.wypozycz_ksiazke("Lalka"))
    print(biblioteka.zwroc_ksiazke("Lalka"))
    print("Dostępne książki:", biblioteka.dostepne_ksiazki())


if __name__ == "__main__":
    main()
