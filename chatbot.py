# realistic_micro_investment_chatbot.py

import math

class InvestmentChatbot:
    def __init__(self):
        self.user_profile = {}
        self.state = "greeting"

    def run(self):
        print(" Welcome to MicroInvest Advisor!\nI help you build wealth through smart micro-investments.")
        print("Type 'start' to begin or 'exit' to quit.")

        while True:
            user_input = input("You: ").strip().lower()

            if user_input in ["exit", "quit", "bye"]:
                print(" Thanks for using MicroInvest. Invest wisely, grow consistently!")
                break

            response = self.handle_input(user_input)
            print(f"Bot: {response}")

    def handle_input(self, user_input):
        if self.state == "greeting":
            if user_input == "start":
                self.state = "collect_age"
                return "Great! Let's get to know you. How old are you?"
            return "Type 'start' to begin the investment onboarding process."

        elif self.state == "collect_age":
            if user_input.isdigit() and 10 < int(user_input) < 100:
                self.user_profile["age"] = int(user_input)
                self.state = "collect_income"
                return "What's your monthly income (in ₹)?"
            else:
                return "Please enter a valid age."

        elif self.state == "collect_income":
            try:
                income = int(user_input)
                if income <= 0:
                    return "Enter a positive income."
                self.user_profile["income"] = income
                self.state = "collect_risk"
                return "What's your risk appetite? (low / medium / high)"
            except:
                return "Please enter income as a number."

        elif self.state == "collect_risk":
            if user_input in ["low", "medium", "high"]:
                self.user_profile["risk"] = user_input
                self.state = "suggest_portfolio"
                return self.suggest_portfolio()
            else:
                return "Please enter one of: low, medium, high."

        elif self.state == "suggest_portfolio":
            if "calculator" in user_input:
                self.state = "sip_calculator"
                return "Enter monthly investment (SIP amount):"
            return "Type 'calculator' to estimate returns, or 'exit' to quit."

        elif self.state == "sip_calculator":
            try:
                if "sip_amount" not in self.user_profile:
                    self.user_profile["sip_amount"] = float(user_input)
                    return "Expected annual return rate (in %, e.g., 12):"

                elif "sip_rate" not in self.user_profile:
                    self.user_profile["sip_rate"] = float(user_input)
                    return "Investment duration (in years):"

                elif "sip_years" not in self.user_profile:
                    self.user_profile["sip_years"] = int(user_input)
                    result = self.calculate_sip_returns()
                    self.state = "suggest_portfolio"
                    return f" Estimated returns: ₹{result} after {self.user_profile['sip_years']} years.\nType 'calculator' to try again or 'exit'."

            except:
                return "Please enter valid numeric input."

        return "I'm not sure how to respond. Type 'start' to begin."

    def suggest_portfolio(self):
        age = self.user_profile["age"]
        income = self.user_profile["income"]
        risk = self.user_profile["risk"]

        suggestion = "\n Based on your profile:\n"
        if risk == "low":
            suggestion += "-  Recommended: Government bonds, large-cap mutual funds, FD-linked SIPs.\n"
        elif risk == "medium":
            suggestion += "-  Recommended: Balanced mutual funds, index ETFs, hybrid equity-debt portfolios.\n"
        else:
            suggestion += "-  Recommended: Equity mutual funds, stocks, and small-cap investments.\n"

        if income < 20000:
            suggestion += "-  Tip: Start with ₹500 SIPs. Consistency > Amount.\n"
        elif income < 50000:
            suggestion += "-  Tip: Allocate 10-20% of income monthly into diversified funds.\n"
        else:
            suggestion += "-  Tip: Consider tax-saving ELSS funds & aggressive growth plans.\n"

        suggestion += "\nWould you like to use the 'calculator' to estimate SIP returns?"
        return suggestion

    def calculate_sip_returns(self):
        P = self.user_profile["sip_amount"]
        r = self.user_profile["sip_rate"] / 100 / 12  # Monthly rate
        n = self.user_profile["sip_years"] * 12

        # SIP future value formula
        future_value = P * (((1 + r) ** n - 1) * (1 + r)) / r
        return round(future_value, 2)


if __name__ == "__main__":
    bot = InvestmentChatbot()
    bot.run()
