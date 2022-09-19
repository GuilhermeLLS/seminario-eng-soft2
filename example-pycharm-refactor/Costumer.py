import string
from typing import List

import Movie
import Rental


class Customer:
  _name: string = None
  _rentals = List[Rental]

  def __init__(self, name):
      self._name = name

  def addRental(self, arg):
      self._rentals.insert(arg)

  def getName(self):
    return self._name


  def statement(self) -> string:
    totalAmount = 0
    frequentRenterPoints = 0
    rentals = self._rentals
    result = "Rental Record for " + self.getName() + "\n"

    for i, rental in enumerate(rentals):
      thisAmount = 0
      # determine amounts for each line
      priceCode = rental.getMovie().getPriceCode()
      if priceCode == Movie.REGULAR:
          thisAmount += 2
          if rental.getDaysRented() > 2:
            thisAmount += (rental.getDaysRented() - 2) * 1.5
      elif priceCode == Movie.NEW_RELEASE:
        thisAmount += rental.getDaysRented() * 3
      elif Movie.CHILDRENS:
        thisAmount += 1.5
        if (rental.getDaysRented() > 3):
            thisAmount += (rental.getDaysRented() - 3) * 1.5

      # add frequent renter points
      frequentRenterPoints += 1
      # add bonus for a two day new release rental
      if (
        rental.getMovie().getPriceCode() == Movie.NEW_RELEASE and
        rental.getDaysRented() > 1
      ):
        frequentRenterPoints += 1

      #show figures for this rental
      result += "\t" + rental.getMovie().getTitle() + "\t" + str(thisAmount) + "\n"
      totalAmount += thisAmount

    # add footer lines
    result += "Amount owed is " + str(totalAmount) + "\n"
    result += "You earned " + str(frequentRenterPoints) + " frequent renter points"
    return result


