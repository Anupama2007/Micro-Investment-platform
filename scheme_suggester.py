# realistic_scheme_suggester.py

def suggest_schemes(age, income, risk, goal):
    schemes = []

    # Tax saving goal
    if goal == "tax saving":
        if risk in ["low", "medium"]:
            schemes.append("Public Provident Fund (PPF)")
            schemes.append("Tax-saving Fixed Deposits (FDs)")
        if risk != "low":
            schemes.append("Equity Linked Savings Scheme (ELSS)")
        schemes.append("National Pension Scheme (NPS)")

    # Retirement goal
    if goal == "retirement":
        if age < 35:
            schemes.append("NPS")
            schemes.append("Index Mutual Funds")
        elif age < 50:
            schemes.append("Balanced Mutual Funds")
        else:
            schemes.append("Senior Citizen Savings Scheme (SCSS)")
            schemes.append("Post Office Monthly Income Scheme")

    # Wealth growth goal
    if goal == "wealth growth":
        if risk == "high":
            schemes.append("Direct Equity (Stocks)")
            schemes.append("SIP in Small Cap Mutual Funds")
        elif risk == "medium":
            schemes.append("SIP in Balanced Mutual Funds")
            schemes.append("Real Estate Investment Trusts (REITs)")
        else:
            schemes.append("Large Cap Mutual Funds")
            schemes.append("Recurring Deposits + Gold ETF")

    # Education or short-term
    if goal == "education":
        if risk == "low":
            schemes.append("Recurring Deposits")
            schemes.append("Short-term Debt Mutual Funds")
        else:
            schemes.append("ELSS")
            schemes.append("Child Education Mutual Funds")

    # Income based diversification
    if income < 20000:
        schemes.append("Start SIPs with ₹500 in index funds")
    elif income < 50000:
        schemes.append("15% income into hybrid mutual funds + RD")
    else:
        schemes.append("Diversify into ELSS, SIPs, NPS, and gold")

    return schemes


def main():
    print(" Welcome to the Investment Scheme Suggester\n")
    age = int(input(" Enter your age: "))
    income = int(input(" Enter your monthly income (in ₹): "))
    risk = input("⚖️  Risk appetite (low / medium / high): ").lower().strip()
    goal = input(" Financial goal (tax saving / retirement / wealth growth / education): ").lower().strip()

    print("\n Generating your personalized suggestions...\n")
    recommendations = suggest_schemes(age, income, risk, goal)

    if recommendations:
        print(" Based on your profile, we suggest:")
        for scheme in recommendations:
            print(f" {scheme}")
    else:
        print(" Sorry, we couldn't find a match. Please check your inputs.")

if __name__ == "__main__":
    main()
