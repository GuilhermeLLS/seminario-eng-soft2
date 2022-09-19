# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import Movie


class Rental:
    def __init__(self, movie, daysRented):
        self._movie = movie
        self._daysRented = daysRented

    def getDaysRented(self) -> int:
        return self._daysRented

    def getMovie(self) -> Movie: #
        return self._movie

