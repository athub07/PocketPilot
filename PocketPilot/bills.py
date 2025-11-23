# bills.py - PocketPilot Bill Splitter
from datetime import datetime
import os

def now_date_time():
    n = datetime.now()
    return n.strftime("%d-%m-%Y"), n.strftime("%H:%M:%S")

def header():
    date_str, time_str = now_date_time()
    print("\n=== 💸 PocketPilot — Bill Splitter ===")
    print("Date:", date_str)
    print("Time:", time_str)
    print("-" * 40)

def bill_splitter():
    header()

    desc = input("Bill description (optional): ").strip()
    total = float(input("Total amount: ").strip())
    n = int(input("Number of people: ").strip())
    names = [s.strip() for s in input("Enter names (comma-separated): ").split(",")][:n]

    share = round(total / n, 2)

    print("\n--- Split Result ---")
    if desc:
        print(f"Description : {desc}")
    print(f"Total amount: {total}")
    print(f"Each person pays: {share}\n")
    print("Breakdown:")
    for name in names:
        print(f"  {name} -> {share}")

    # save to csv
    try:
        os.makedirs("data", exist_ok=True)
        with open("data/bills.csv", "a", encoding="utf-8") as f:
            participants = ";".join(names)
            date_str, time_str = now_date_time()
            f.write(f"{date_str},{time_str},{desc},{total},{n},{share},{participants}\n")
        print("\n(Saved to data/bills.csv)")
    except:
        pass

    print("\nP.S. Tip: Keep a screenshot — receipts and memories both matter 🙂\n")

if __name__ == "__main__":
    bill_splitter()
