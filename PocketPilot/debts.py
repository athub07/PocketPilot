# debts.py - PocketPilot Debt / Lend Tracker
from datetime import datetime
import os
import random

DATA_FILE = "data/debts.csv"

EASTER_ADD = [
    "Note: Trust but record. 😉",
    "Added! Don’t forget to remind them with a meme. 😄",
    "Saved — money today, friendship forever (mostly). 🫶"
]
EASTER_CLEAR = [
    "Debt cleared — peace restored. ✌️",
    "Paid — friendship level +1! 🏆",
    "All good! You owe them a chai now. ☕"
]

def now_date_time():
    n = datetime.now()
    return n.strftime("%d-%m-%Y"), n.strftime("%H:%M:%S")

def header(title):
    date_str, time_str = now_date_time()
    print(f"\n=== 🤝 PocketPilot — {title} ===")
    print("Date:", date_str)
    print("Time:", time_str)
    print("-" * 70)

def ensure_data_dir():
    os.makedirs("data", exist_ok=True)

def read_debts():
    debts = []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",", 7)
                while len(parts) < 8:
                    parts.append("")
                did, date_s, lender, borrower, amount, status, notes, time_s = parts
                debts.append({
                    "id": int(did),
                    "date": date_s,
                    "time": time_s,
                    "lender": lender,
                    "borrower": borrower,
                    "amount": float(amount),
                    "status": status,
                    "notes": notes
                })
    except:
        pass
    return debts

def write_debts(debts):
    ensure_data_dir()
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        for d in debts:
            f.write(f"{d['id']},{d['date']},{d['lender']},{d['borrower']},{d['amount']},{d['status']},{d['notes']},{d['time']}\n")

def next_id(debts):
    return 1 if not debts else max(d["id"] for d in debts) + 1

def add_debt():
    header("Add Debt / Lend")
    ensure_data_dir()

    lender = input("Lender name: ").strip()
    borrower = input("Borrower name: ").strip()

    try:
        amount = float(input("Amount (numeric): ").strip())
    except:
        print("Invalid amount.\n")
        return

    notes = input("Notes (optional): ").strip()

    date_s, time_s = now_date_time()
    debts = read_debts()
    did = next_id(debts)

    debts.append({
        "id": did,
        "date": date_s,
        "time": time_s,
        "lender": lender,
        "borrower": borrower,
        "amount": amount,
        "status": "open",
        "notes": notes
    })

    write_debts(debts)

    print(f"\nDebt ID #{did} added.")
    print(random.choice(EASTER_ADD))

def list_debts(filter_mode="all"):
    header("List Debts")
    debts = read_debts()

    if not debts:
        print("\nNo debt records found.\n")
        return

    print(f"{'ID':3} | {'Date':10} | {'Time':8} | {'Lender':10} | {'Borrower':10} | {'Amt':7} | {'Status':7} | Notes")
    print("-" * 90)

    for d in debts:
        if filter_mode == "open" and d["status"] != "open":
            continue
        print(f"{d['id']:3} | {d['date']:10} | {d['time']:8} | {d['lender'][:10]:10} | {d['borrower'][:10]:10} | {d['amount']:7.2f} | {d['status'][:7]:7} | {d['notes']}")

def clear_debt():
    header("Clear Debt")
    debts = read_debts()

    try:
        did = int(input("Enter debt ID to clear: ").strip())
    except:
        print("Invalid ID.\n")
        return

    found = False

    for d in debts:
        if d["id"] == did and d["status"] == "open":
            d["status"] = "cleared"
            d["time"] = now_date_time()[1]
            found = True
            break

    if found:
        write_debts(debts)
        print(f"\nDebt #{did} cleared.")
        print(random.choice(EASTER_CLEAR))
    else:
        print("\nNo matching open debt found.\n")

def summary_for_user():
    header("Summary")
    name = input("Enter name: ").strip().lower()
    debts = read_debts()

    owes = sum(d["amount"] for d in debts if d["borrower"].lower() == name and d["status"] == "open")
    owed = sum(d["amount"] for d in debts if d["lender"].lower() == name and d["status"] == "open")

    print(f"\n{name.title()} owes: ₹ {owes:.2f}")
    print(f"{name.title()} is owed: ₹ {owed:.2f}")

def search_debts():
    header("Search by Name")
    key = input("Search (lender or borrower): ").strip().lower()
    debts = read_debts()

    results = [d for d in debts if key in d["lender"].lower() or key in d["borrower"].lower()]

    if not results:
        print("\nNo matching records.\n")
        return

    print(f"\nFound {len(results)} record(s):")
    print(f"{'ID':3} | {'Date':10} | {'Lender':10} | {'Borrower':10} | {'Amt':7} | {'Status':7} | Notes")
    print("-" * 70)

    for d in results:
        print(f"{d['id']:3} | {d['date']:10} | {d['lender'][:10]:10} | {d['borrower'][:10]:10} | {d['amount']:7.2f} | {d['status'][:7]:7} | {d['notes']}")

def debts_menu():
    while True:
        print("\n=== 🤝 PocketPilot — Debt / Lend Tracker ===")
        print("1. Add debt / lend")
        print("2. List all records")
        print("3. List open records")
        print("4. Clear a debt")
        print("5. Summary for a name")
        print("6. Search by name")
        print("7. Back to main menu")

        ch = input("Choose (1-7): ").strip()

        if ch == "1":
            add_debt()
        elif ch == "2":
            list_debts("all")
        elif ch == "3":
            list_debts("open")
        elif ch == "4":
            clear_debt()
        elif ch == "5":
            summary_for_user()
        elif ch == "6":
            search_debts()
        elif ch == "7":
            break
        else:
            print("Invalid option. Enter 1–7.")

if __name__ == "__main__":
    debts_menu()
