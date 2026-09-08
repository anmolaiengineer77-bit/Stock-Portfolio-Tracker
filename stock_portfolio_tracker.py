stock_prices= {
"AAPL": 180,
    "TSLA": 250,
    "MSFT": 420,
    "GOOGL": 160,
    "AMZN": 190,
    "META": 500,
    "NVDA": 120,
    "NFLX": 700,
    "ORCL": 180,
    "IBM": 250,
    "INTC": 25,
    "AMD": 160,
    "ADBE": 350,
    "CRM": 300,
    "PYPL": 70,
    "DIS": 100,
    "UBER": 90,
    "NKE": 75,
    "PEP": 170,
    "KO": 65
}
total = 0
portfolio = {}
for i in range(2):
    stock = input("Enter stock name: ")
    quantity = int(input("Enter quantity: "))
    price = stock_prices[stock]
    investment = price * quantity
    total = total + investment
print("Total Investment =", total)
save = input("Do you want to save the result? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio\n")
        file.write("----------------\n")

        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            investment = price * quantity
            file.write(f"{stock} = {quantity} shares = {investment}\n")

        file.write("----------------\n")
        file.write(f"Total Investment = {total}\n")

    print("Result saved successfully.")
