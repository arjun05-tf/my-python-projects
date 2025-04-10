rates = {
    "USD": {
        "INR": 83.0,
        "EUR": 0.92
    },
    "INR": {
        "USD": 1 / 83.0,
        "EUR": 0.010
    },
    "EUR": {
        "USD": 1.09,
        "INR": 96.51
    }
}

symbols = {"USD": "$", "INR": "₹", "EUR": "€"}

def main():
    source = input("\n1. INR\n2. USD\n3. EUR\nchoose the currency: ").upper()
    amount = float(input("enter amount to be converted: "))
    target = input("\n1. INR\n2. USD\n3. EUR\nchoose the currency: ").upper()
    converter(amount, source, target)

def converter(amount, source, target):
    if source == "INR":
        if target == "INR":
            print("Cannot convert to the same currency, try again later!")
            return
        elif target == "USD":
            rate = rates[source][target]
            symbol = symbols[target]
            converted = amount * rate
            print(f"You get {symbol}{converted:.2f} back")
        elif target == "EUR":
            rate = rates[source][target]
            symbol = symbols[target]
            converted = amount * rate
            print(f"You get {symbol}{converted:.2f} back")
        else:
            print("Currency yet to be added, thanks for the suggestion")
    elif source == "USD":
        if target == "USD":
            print("Cannot convert to the same currency, try again later!")
            return
        elif target == "INR":
            rate = rates[source][target]
            symbol = symbols[target]
            converted = amount * rate
            print(f"You get {symbol}{converted:.2f} back")
            
        elif target == "EUR":
            rate = rates[source][target]
            symbol = symbols[target]
            converted = amount * rate
            print(f"You get {symbol}{converted:.2f} back")
        else:
            print("Currency yet to be added, thanks for the suggestion")
    elif source == "EUR":
        if target == "EUR":
            print("Cannot convert to the same currency, try again later!")
            return
        elif target == "USD":
            rate = rates[source][target]
            symbol = symbols[target]
            converted = amount * rate
            print(f"You get {symbol}{converted:.2f} back")
        elif target == "INR":
            rate = rates[source][target]
            symbol = symbols[target]
            converted = amount * rate
            print(f"You get {symbol}{converted:.2f} back")
        else:
            print("Currency yet to be added, thanks for the suggestion")
    else:
        print("Currency yet to be added, stay tuned")


main()