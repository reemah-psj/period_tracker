from datetime import datetime, timedelta

class PeriodTracker:
    def __init__(self, last_period_start, cycle_length, period_length):
        self.last_period_start = datetime.strptime(last_period_start, "%Y-%m-%d")
        self.cycle_length = cycle_length
        self.period_length = period_length

    def next_period_date(self):
        next_period = self.last_period_start + timedelta(days=self.cycle_length)
        return next_period.strftime("%Y-%m-%d")

    def fertile_window(self):
        ovulation_day = self.last_period_start + timedelta(days=self.cycle_length // 2)
        fertile_start = ovulation_day - timedelta(days=3)
        fertile_end = ovulation_day + timedelta(days=3)
        return {
            "fertile_start": fertile_start.strftime("%Y-%m-%d"),
            "fertile_end": fertile_end.strftime("%Y-%m-%d")
        }

    def period_end_date(self):
        period_end = self.last_period_start + timedelta(days=self.period_length)
        return period_end.strftime("%Y-%m-%d")

# Input from the user
def get_user_input():
    last_period_start = input("Enter the start date of your last period (YYYY-MM-DD): ")
    cycle_length = int(input("Enter your menstrual cycle length in days (e.g., 28): "))
    period_length = int(input("Enter your period length in days (e.g., 5): "))
    
    return last_period_start, cycle_length, period_length

def main():
    print("Welcome to the Period Tracker!")
    
    # Getting inputs from the user
    last_period_start, cycle_length, period_length = get_user_input()

    # Create an instance of the PeriodTracker class with user inputs
    tracker = PeriodTracker(last_period_start, cycle_length, period_length)

    # Display the results
    print("\nYour next period is expected to start on:", tracker.next_period_date())
    fertile_window = tracker.fertile_window()
    print(f"Your fertile window is from {fertile_window['fertile_start']} to {fertile_window['fertile_end']}.")
    print("Your period is expected to end on:", tracker.period_end_date())

if __name__ == "__main__":
    main()
