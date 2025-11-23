# tips.py - PocketPilot Money-Saving Resources
import os
from datetime import datetime

DATA_FILE = "data/resources.txt"

def now_date_time():
    n = datetime.now()
    return n.strftime("%d-%m-%Y"), n.strftime("%H:%M:%S")

def header(title):
    date_str, time_str = now_date_time()
    print(f"\n===  PocketPilot — {title} ===")
    print("Date:", date_str)
    print("Time:", time_str)
    print("-" * 60)

def ensure_data_dir():
    if not os.path.exists("data"):
        os.makedirs("data")

def read_resources():
    items = []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("|")
                while len(parts) < 5:
                    parts.append("")
                items.append({
                    "category": parts[0],
                    "title": parts[1],
                    "author": parts[2],
                    "blurb": parts[3],
                    "url": parts[4]
                })
    except FileNotFoundError:
        print("\nresources.txt not found.\n")
    return items

def show_all_resources():
    header("All Money-Saving Resources")
    res = read_resources()
    if not res:
        return
    for i, r in enumerate(res, 1):
        print(f"{i}. [{r['category']}] {r['title']} — {r['author']}")
        if r['blurb']:
            print(f"   {r['blurb']}")
        if r['url']:
            print(f"   Link/Note: {r['url']}")
        print()
    print(f"(Total: {len(res)})\n")

def show_by_category():
    header("Resources by Category")
    res = read_resources()
    if not res:
        return
    cat = input("Enter category (books/web/yt/etc.): ").strip().lower()
    filt = [r for r in res if r["category"].lower() == cat]
    if not filt:
        print("\nNo resources under this category.\n")
        return
    for i, r in enumerate(filt, 1):
        print(f"{i}. {r['title']} — {r['author']}")
        if r['blurb']:
            print(f"   {r['blurb']}")
        if r['url']:
            print(f"   Link/Note: {r['url']}")
        print()
    print(f"(Total: {len(filt)})\n")

def add_resource():
    ensure_data_dir()
    header("Add Resource")
    cat = input("Category: ").strip()
    title = input("Title: ").strip()
    author = input("Author/Site: ").strip()
    blurb = input("Short blurb: ").strip()
    url = input("URL/Note: ").strip()

    with open(DATA_FILE, "a", encoding="utf-8") as f:
        f.write(f"{cat}|{title}|{author}|{blurb}|{url}\n")

    print("\nResource added successfully!\n")

def tips_menu():
    while True:
        print("\n===  PocketPilot — Money-Saving Resources ===")
        print("1. Show all resources")
        print("2. Show resources by category")
        print("3. Add a resource")
        print("4. Back to main menu")

        ch = input("Choose (1-4): ").strip()

        if ch == "1":
            show_all_resources()
        elif ch == "2":
            show_by_category()
        elif ch == "3":
            add_resource()
        elif ch == "4":
            break
        else:
            print("Invalid option. Enter 1–4.")

if __name__ == "__main__":
    tips_menu()

