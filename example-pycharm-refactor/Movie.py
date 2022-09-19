import string

CHILDRENS = 2
REGULAR = 0
NEW_RELEASE = 1

class Movie:
    _title: string = None
    _priceCode: int = None

    def __init__(self, title: string, priceCode: int):
        self._title = title
        self._priceCode = priceCode

    def getPriceCode(self):
        return self._priceCode

    def setPriceCode(self, arg: int):
        self._priceCode = arg

    def getTitle(self):
        return self._title
