# subs.py - PocketPilot Subscription Manager
from datetime import datetime
import os

DATA_FILE = "data/subscriptions.txt"

def now_date_time():
    n = datetime.now()
    return n.strftime("%d-%m-%Y"), n.strftime("%H:%M:%S")

def header(title):
    date_str, time_str = now_date_time()
    print(f"\n===  PocketPilot — {title} ===")
    print("Date:", date_str)
    print("Time:", time_str)
    print("-" * 50)

def ensure_data_dir():
    os.makedirs("data", exist_ok=True)

def read_subs():
    subs = []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",", 6)
                while len(parts) < 7:
                    parts.append("")
                name,cost,renewal,added_date,added_time,status,notes = parts
                subs.append({
                    "name": name,
                    "cost": float(cost) if cost else 0.0,
                    "renewal": renewal,
                    "added_date": added_date,
                    "added_time": added_time,
                    "status": status or "active",
                    "notes": notes
                })
    except FileNotFoundError:
        pass
    return subs

def write_subs(subs):
    ensure_data_dir()
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        for s in subs:
            f.write(f"{s['name']},{s['cost']},{s['renewal']},{s['added_date']},{s['added_time']},{s['status']},{s['notes']}\n")

def add_subscription():
    header("Add Subscription")
    ensure_data_dir()

    name = input("Name: ").strip()
    cost = float(input("Monthly cost (numeric): ").strip())
    renewal = input("Renewal date (DD-MM-YYYY): ").strip()
    notes = input("Notes (optional): ").strip()

    added_date, added_time = now_date_time()

    subs = read_subs()
    subs.append({
        "name": name,
        "cost": cost,
        "renewal": renewal,
        "added_date": added_date,
        "added_time": added_time,
        "status": "active",
        "notes": notes
    })
    write_subs(subs)

    print("\nSubscription added.")
    print(f"Date: {added_date}")
    print(f"Time: {added_time}\n")

def list_subscriptions():
    header("All Subscriptions")
    subs = read_subs()
    active = [s for s in subs if s["status"] == "active"]

    if not active:
        print("\nNo subscriptions found.\n")
        return

    print(f"{'Name':15} | {'Monthly':8} | {'Renewal':11} | {'Status':8} | Notes")
    print("-" * 65)

    for s in active:
        print(f"{s['name'][:15]:15} | {s['cost']:8.2f} | {s['renewal']:11} | {s['status']:8} | {s['notes']}")

    print("")

def monthly_total():
    header("Monthly Total")
    subs = read_subs()
    total = sum(s['cost'] for s in subs if s['status'] == "active")
    print(f"\nTotal monthly subscription cost: ₹ {total:.2f}\n")

def upcoming_renewals():
    header("Upcoming Renewals")
    subs = read_subs()
    days_in = input("Show renewals within how many days? (default 7): ").strip()
    days = int(days_in) if days_in else 7

    today = datetime.now().date()
    upcoming = []

    for s in subs:
        if s["status"] != "active":
            continue
        try:
            rdate = datetime.strptime(s["renewal"], "%d-%m-%Y").date()
            diff = (rdate - today).days
            if 0 <= diff <= days:
                upcoming.append((s["name"], s["renewal"], diff))
        except:
            pass

    if upcoming:
        for name, r, d in upcoming:
            print(f"{name} — renews in {d} days ({r})")
    else:
        print("No renewals in this window.")

    print("")

def remove_subscription():
    header("Remove Subscription")
    subs = read_subs()

    target = input("Enter subscription name (exact): ").strip()
    found = False

    for s in subs:
        if s["name"].lower() == target.lower() and s["status"] == "active":
            s["status"] = "cancelled"
            found = True

    if found:
        write_subs(subs)
        print(f"\nSubscription '{target}' marked as cancelled.\n")
    else:
        print("\nNo active subscription found by that name.\n")

def subscription_menu():
    while True:
        print("\n===  PocketPilot — Subscription Manager ===")
        print("1. Add subscription")
        print("2. List subscriptions")
        print("3. Show upcoming renewals")
        print("4. Monthly total")
        print("5. Remove subscription")
        print("6. Back to main menu")

        ch = input("Choose (1-6): ").strip()

        if ch == "1":
            add_subscription()
        elif ch == "2":
            list_subscriptions()
        elif ch == "3":
            upcoming_renewals()
        elif ch == "4":
            monthly_total()
        elif ch == "5":
            remove_subscription()
        elif ch == "6":
            break
        else:
            print("Invalid choice. Enter 1–6.")

if __name__ == "__main__":
    subscription_menu()

