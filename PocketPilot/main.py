# main.py - PocketPilot (Student Finance Assistant)
# Integrated launcher for all modules

import os
from datetime import datetime

# Startup banner for PocketPilot
def startup_banner():
    print("=" * 50)
    print("               POCKETPILOT (v1.0)               ")
    print("=" * 50)
    print("    Student Pocket Money & Finance Assistant\n")

def main_menu():
    while True:
        print("\n=== PocketPilot Main Menu ===")
        print("1. 💸 Bill Splitter")
        print("2. 📺 Subscription Manager")
        print("3. 🤝 Debt / Lend Tracker")
        print("4. 📚 Money-Saving Resources")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            import bills
            bills.bill_splitter()
        elif choice == '2':
            import subs
            subs.subscription_menu()
        elif choice == '3':
            import debts
            debts.debts_menu()
        elif choice == '4':
            import tips
            tips.tips_menu()
        elif choice == '5':
            print("\nThank you for using PocketPilot! 😊")
            print("Goodbye and remember: small savings lead to big wins!")
            break
        else:
            print("Invalid option. Please enter a number from 1–5.")

if __name__ == "__main__":
    # ensure data folder exists
    if not os.path.exists("data"):
        os.makedirs("data")

    startup_banner()
    main_menu()
