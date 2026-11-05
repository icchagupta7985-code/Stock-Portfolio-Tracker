"""
Stock Portfolio Tracker
-----------------------
A simple console program that calculates the total investment value
of a portfolio using manually defined (hardcoded) stock prices.

Concepts used: dictionary, input/output, loops, conditions,
               basic arithmetic, functions, file handling.
"""

# ---------------------------------------------------------------
# 1. Predefined stock prices (hardcoded dictionary - no live API)
# ---------------------------------------------------------------
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 190,
    "MSFT": 420
}


def show_available_stocks():
    """Print all stocks and their prices."""
    print("\nAvailable Stocks")
    print("-" * 25)
    for symbol, price in stock_prices.items():
        print(f"{symbol:<8} ${price}")
    print("-" * 25)


def get_stock_symbol():
    """Keep asking until the user enters a valid stock symbol."""
    while True:
        symbol = input("Enter stock symbol (e.g. AAPL): ").strip().upper()
        if symbol == "":
            print("Error: Symbol cannot be empty. Please try again.")
        elif symbol in stock_prices:
            return symbol
        else:
            print(f"Error: '{symbol}' is not in our stock list. Please try again.")


def get_quantity():
    """Keep asking until the user enters a valid whole number greater than 0."""
    while True:
        text = input("Enter quantity of shares purchased: ").strip()
        try:
            quantity = int(text)          # fails for text like "abc" or "2.5"
        except ValueError:
            print("Error: Please enter a whole number (e.g. 5). Letters/decimals are not allowed.")
            continue

        if quantity <= 0:                 # rejects zero and negative numbers
            print("Error: Quantity must be greater than 0.")
        else:
            return quantity


def ask_yes_no(question):
    """Ask a yes/no question. Returns True for yes, False for no."""
    while True:
        answer = input(question + " (yes/no): ").strip().lower()
        if answer in ("yes", "y"):
            return True
        if answer in ("no", "n"):
            return False
        print("Error: Please type 'yes' or 'no'.")


def display_summary(portfolio):
    """Print a detailed investment summary and return the total value."""
    print("\n" + "=" * 52)
    print("            INVESTMENT SUMMARY")
    print("=" * 52)
    print(f"{'Stock':<8}{'Quantity':>10}{'Price ($)':>14}{'Value ($)':>16}")
    print("-" * 52)

    total = 0
    for symbol, quantity in portfolio.items():
        price = stock_prices[symbol]
        value = quantity * price          # investment value for this stock
        total += value                    # add to running total
        print(f"{symbol:<8}{quantity:>10}{price:>14}{value:>16}")

    print("-" * 52)
    print(f"{'TOTAL INVESTMENT':<32}{total:>20}")
    print("=" * 52)
    return total


def save_as_txt(portfolio, total, filename="portfolio_summary.txt"):
    """Save the summary as a text file."""
    with open(filename, "w") as file:
        file.write("STOCK PORTFOLIO SUMMARY\n")
        file.write("=" * 52 + "\n")
        file.write(f"{'Stock':<8}{'Quantity':>10}{'Price ($)':>14}{'Value ($)':>16}\n")
        file.write("-" * 52 + "\n")
        for symbol, quantity in portfolio.items():
            price = stock_prices[symbol]
            file.write(f"{symbol:<8}{quantity:>10}{price:>14}{quantity * price:>16}\n")
        file.write("-" * 52 + "\n")
        file.write(f"{'TOTAL INVESTMENT':<32}{total:>20}\n")
    return filename


def save_as_csv(portfolio, total, filename="portfolio_summary.csv"):
    """Save the summary as a CSV file (opens in Excel / Numbers)."""
    with open(filename, "w") as file:
        file.write("Stock,Quantity,Price,Value\n")
        for symbol, quantity in portfolio.items():
            price = stock_prices[symbol]
            file.write(f"{symbol},{quantity},{price},{quantity * price}\n")
        file.write(f"TOTAL INVESTMENT,,,{total}\n")
    return filename


def save_results(portfolio, total):
    """Ask the user whether and how to save the results."""
    if not ask_yes_no("\nDo you want to save the results to a file?"):
        print("Results not saved.")
        return

    while True:
        choice = input("Choose file format - type 'csv' or 'txt': ").strip().lower()
        if choice in ("csv", "txt"):
            break
        print("Error: Please type either 'csv' or 'txt'.")

    try:
        if choice == "csv":
            filename = save_as_csv(portfolio, total)
        else:
            filename = save_as_txt(portfolio, total)
        print(f"Success! Results saved to '{filename}' in the project folder.")
    except OSError:
        print("Error: Could not save the file. Check folder permissions.")


def main():
    print("=" * 52)
    print("          STOCK PORTFOLIO TRACKER")
    print("=" * 52)
    show_available_stocks()

    portfolio = {}                        # stores {symbol: quantity}

    # Loop to allow multiple stocks
    while True:
        symbol = get_stock_symbol()
        quantity = get_quantity()

        # If the same stock is entered again, add to the old quantity
        if symbol in portfolio:
            portfolio[symbol] += quantity
        else:
            portfolio[symbol] = quantity

        value = quantity * stock_prices[symbol]
        print(f"Added: {symbol} = {quantity} x {stock_prices[symbol]} = {value}\n")

        if not ask_yes_no("Do you want to add another stock?"):
            break

    total = display_summary(portfolio)
    save_results(portfolio, total)
    print("\nThank you for using Stock Portfolio Tracker!")


# Program starts here
if __name__ == "__main__":
    main()