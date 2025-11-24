# **PocketPilot**

PocketPilot is a small Python project I made to help with basic money-related tasks that students usually deal with. Things like splitting bills after going out, checking when subscriptions are about to renew, keeping track of small debts among friends, and having a list of useful money-saving resources. The idea was to build something simple, practical, and easy to run in the console without using any advanced Python concepts.

---

## **Overview**

The project is fully console-based. When you run `main.py`, it shows a menu where you can pick what you want to do. Each feature is handled in a separate Python file so the code stays organised and easier to understand. All the data is saved in simple text or CSV files inside a `data/` folder.

---

## **Features**

1. **Bill Splitter**

   * Splits a total amount equally among names you enter
   * Shows the date and time
   * Saves a basic log in `bills.csv`

2. **Subscription Manager**

   * Add subscriptions with renewal dates
   * List all active subscriptions
   * Show upcoming renewals within a chosen number of days
   * Cancel subscriptions
   * Stored in `subscriptions.txt`

3. **Debt / Lend Tracker**

   * Add entries for who owes whom
   * List open or all debts
   * Clear debts
   * Search by name
   * Stored in `debts.csv`

4. **Money-Saving Resources**

   * Shows a list of books, websites, and videos
   * Can filter by category
   * Can add custom resources
   * Stored in `resources.txt`

---

## **Technologies / Tools Used**

* Python 3
* VS Code or PyCharm
* Simple text file and CSV storage
* No external libraries needed

---

## **How to Install and Run**

1. Install Python 3 on your system
2. Download or clone the project folder
3. Open the folder in VS Code, PyCharm, or terminal
4. Make sure the folder structure is intact (especially the `data/` folder)
5. Run the program with:

```
python main.py
```

Everything works in the terminal.

---

## **Testing the Project**

Here are some quick tests to check the program:

* Try splitting a bill, for example total = 900 between 3 people
* Add a subscription and list it
* Add a debt between two names and then clear it
* View all money-saving resources and try adding one

During testing, check that the files inside the `data/` folder get updated.

---

## **Project Structure**

```
pocketpilot/
    main.py
    bills.py
    subs.py
    debts.py
    tips.py
    statement.md
    README.md
    data/
        resources.txt
        subscriptions.txt
        debts.csv
        bills.csv
```


## **Author**

Aviraj Singh Thakur
VIT
PocketPilot – VITyarthi Project
