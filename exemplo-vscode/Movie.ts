export default class Movie {

    public static CHILDRENS = 2 as const;
    public static REGULAR = 0 as const;
    public static NEW_RELEASE = 1 as const;

    private _title: string;
    private _priceCode: number;

    public Movie(title: string, priceCode: number) {
        this._title = title;
        this._priceCode = priceCode;
    }

    public getPriceCode(): number {
        return this._priceCode;
    }

    public setPriceCode(arg: number): void {
        this._priceCode = arg;
    }

    public getTitle(): string {
        return this._title;
    }
}