def invest(amount, rate, years):
    """Investment rate and years function"""
    years = float(years)
    while years > 0:
        amount = (float(amount) * float(rate) + amount
        print(amount)
        years = years - 1


amount = input("Enter initial investment amount:")
rate = input("Enter an annual percentage rate:")
years = input("For how many years?")
print(f"{invest(amount, rate, years)}")

# Calculate compound interest to track the growth of an investment


def invest(amount, rate, years):
    for year in range(1, years + 1):
        amount = amount * (1 + rate)
        print(f"year {year}: ${amount:,.2f}")


amount = float(input("Enter a principal amount: "))
rate = float(input("Enter an anual rate of return: "))
years = int(input("Enter a number of years: "))

invest(amount, rate, years)