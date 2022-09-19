import Movie from './Movie';
import Rental from './Rental';


export default class Customer {
    private _name: string;
    private _rentals = new Array<Rental>();

    public Customer(name: string) {
        this._name = name;
    }

    public addRental(arg: Rental): void {
        this._rentals.push(arg);
    }
    
    public getName(): string {
        return this._name;
    }

    public statement(): string {
        let totalAmount = 0;
        let frequentRenterPoints = 0;
        const rentals = this._rentals;
        let result = "Rental Record for " + this.getName() + "\n";
        
        for (const rental of rentals) {
            let thisAmount = 0;
            //determine amounts for each line
            switch (rental.getMovie().getPriceCode()) {
                case Movie.REGULAR:
                    thisAmount += 2;
                    if (rental.getDaysRented() > 2)
                        thisAmount += (rental.getDaysRented() - 2) * 1.5;
                    break;
                case Movie.NEW_RELEASE:
                    thisAmount += rental.getDaysRented() * 3;
                    break;
                case Movie.CHILDRENS:
                    thisAmount += 1.5;
                    if (rental.getDaysRented() > 3)
                        thisAmount += (rental.getDaysRented() - 3) * 1.5;
                    break;
            }

            // add frequent renter points
            frequentRenterPoints++;
            // add bonus for a two day new release rental
            if ((rental.getMovie().getPriceCode() == Movie.NEW_RELEASE) &&
                rental.getDaysRented() > 1) frequentRenterPoints++;

            //show figures for this rental
            result += "\t" + rental.getMovie().getTitle() + "\t" +
                String(thisAmount) + "\n";
            totalAmount += thisAmount;
        }

        //add footer lines
        result += "Amount owed is " + totalAmount + "\n";
        result += "You earned " + frequentRenterPoints +
            " frequent renter points";
        return result;
    }
}