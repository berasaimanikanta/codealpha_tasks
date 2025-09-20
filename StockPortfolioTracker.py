import csv

def stock_portfolio():
    # Hardcoded stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "MSFT": 330,
        "AMZN": 135
    }

    portfolio = {}  # store user’s stock holdings
    total_investment = 0

    print("📈 Stock Portfolio Tracker")
    print("Available stocks:", ", ".join(stock_prices.keys()))

    while True:
        stock = input("\nEnter stock symbol (or type 'done' to finish): ").upper()

        if stock == "DONE":
            break

        if stock not in stock_prices:
            print("❌ Stock not found! Please choose from available stocks.")
            continue

        try:
            qty = int(input(f"Enter quantity of {stock}: "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        # Add to portfolio
        if stock in portfolio:
            portfolio[stock] += qty
        else:
            portfolio[stock] = qty

    print("\n📊 Your Portfolio Summary:")
    for stock, qty in portfolio.items():
        value = stock_prices[stock] * qty
        total_investment += value
        print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}")

    print(f"\n💰 Total Investment Value: ${total_investment}")

    # Optional: Save to CSV
    save_choice = input("\nDo you want to save portfolio to CSV? (yes/no): ").lower()
    if save_choice == "yes":
        with open("portfolio.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Stock", "Quantity", "Price", "Value"])
            for stock, qty in portfolio.items():
                writer.writerow([stock, qty, stock_prices[stock], stock_prices[stock] * qty])
            writer.writerow(["TOTAL", "", "", total_investment])
        print("✅ Portfolio saved to 'portfolio.csv'")

# Run the program
stock_portfolio()
