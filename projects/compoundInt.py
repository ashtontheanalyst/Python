# Calc. for compound interest

print("-------- COMPOUND INTEREST CALCULATOR --------")

principal = float(input("Enter your principal balance: $"))
# Check to make sure it's not negative, if so user types in again
while principal < 0:
    print(f"{principal:.2f} is invalid, must be positive or zero")
    principal = float(input("Enter principal again please: $ "))


intRate = float(input("Enter your interest rate: "))
while intRate < 0:
    print(f"{intRate:.2f} is invalid, must be positive")
    intRate = float(input("Enter interest rate again please: "))


time = int(input("Enter an amount of years: "))
while time < 0:
    print(f"{time} is invalid, must be positive")
    time = int(input("Enter interest rate again please: "))

print("\n--------------------- RESULT ---------------------")
amount = principal * pow((1 + (intRate/100)), time)
print(f"${principal:.2f}, over {time} years, at {intRate}% interest becomes:")
print(f"${amount:.2f}")
print("--------------------------------------------------")
