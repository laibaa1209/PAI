def convert_currency(from_amount, from_currency, to_currency):
    if from_currency == to_currency:
        return from_amount

    rate = 0  

    if from_currency == 'EUR':
        if to_currency == 'USD':
            rate = 1.10
        elif to_currency == 'PKR':
            rate = 300.00
        elif to_currency == 'INR':
            rate = 90.00
        elif to_currency == 'JPY':
            rate = 160.00

    elif from_currency == 'USD':
        if to_currency == 'EUR':
            rate = 0.91
        elif to_currency == 'PKR':
            rate = 272.00
        elif to_currency == 'INR':
            rate = 82.00
        elif to_currency == 'JPY':
            rate = 145.00

    elif from_currency == 'PKR':
        if to_currency == 'EUR':
            rate = 0.0033
        elif to_currency == 'USD':
            rate = 0.0037
        elif to_currency == 'INR':
            rate = 0.30
        elif to_currency == 'JPY':
            rate = 0.53

    elif from_currency == 'INR':
        if to_currency == 'EUR':
            rate = 0.011
        elif to_currency == 'USD':
            rate = 0.012
        elif to_currency == 'PKR':
            rate = 3.33
        elif to_currency == 'JPY':
            rate = 1.76

    elif from_currency == 'JPY':
        if to_currency == 'EUR':
            rate = 0.0063
        elif to_currency == 'USD':
            rate = 0.0069
        elif to_currency == 'PKR':
            rate = 1.89
        elif to_currency == 'INR':
            rate = 0.57

    if rate == 0:
        print("Conversion rate not available for the given currency pair.")
    else:
        converted_currency = from_amount * rate
        print(f"The converted currency from {from_currency} to {to_currency} is: {converted_currency}")

def main():
    currency_options = {
        '1': 'EUR',
        '2': 'USD',
        '3': 'PKR',
        '4': 'INR',
        '5': 'JPY'
    }

    from_currency_choice = input("Which currency you want to convert? : \n1.Euro\n2.Dollar\n3.PKR\n4.INR\n5.Yen\nChoose: ")
    to_currency_choice = input("Which currency you want to convert into? : \n1.Euro\n2.Dollar\n3.PKR\n4.INR\n5.Yen\nChoose: ")
    from_amount = float(input("Enter the amount you want to convert: "))

    from_currency = currency_options.get(from_currency_choice)
    to_currency = currency_options.get(to_currency_choice)

    if from_currency and to_currency:
        convert_currency(from_amount, from_currency, to_currency)
    else:
        print("Invalid currency selection.")

main()
