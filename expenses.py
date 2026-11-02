from datetime import date
import json


def add_expense():
    try:
        amount = float(input("Enter amount: ₹").strip())
        if not amount > 0:
            print("Invalid amount...")
            return

    except ValueError:
        print("Please enter a number.")
        return

    category = input("Enter category: ").strip().title()
    
    if not category:
        print("Invalid category.")
        return
    
    expenses.append({"category":category, "amount": amount, "date": date.today().isoformat()}
                    )
    save_expenses()
    

def view_expenses():
      if not expenses:
        print("No expenses yet!")
        return
      for index, item in enumerate(expenses, start=1):
          print(f"{index}. {item['date']} | {item['category']} | ₹{item['amount']:.2f}")


def view_summary():
    total_spent = 0
    per_category = {}

    if not expenses:
        print("No expenses yet!")
        return
    for expense in expenses:
        total_spent += expense["amount"]
        per_category[expense["category"]] = per_category.get(expense["category"], 0) + expense["amount"]
    
    print(f"Total spent: ₹{total_spent:.2f}")

    for category , amount in per_category.items():
        print(f"{category} | ₹{amount:.2f}")


def save_expenses():
    with open("expenses.json", "w") as f:
        json.dump(expenses, f)

    print("expenses saved successfully!")


def load_expenses():
    try:
        with open("expenses.json", "r") as f:
            return json.load(f)
        
    except FileNotFoundError:
        print("expenses.json not found. Initialising an empty expenses list.")
        return []
    except json.JSONDecodeError:
        print("expenses.json is corrupted or empty. Initialising an empty expenses list.")
        return []


def filter_expenses():
    category = input("Enter category: ").strip().title()

    found = []
    total = 0
    
    for expense in expenses:
        if expense["category"] == category:
            total += expense["amount"]
            found.append(expense)

    if not found:
                print(f"No expenses found for {category}.")
                return
    
    for index, item in enumerate(found, start=1):
        print(f"{index}. {item['date']} | {item['category']} | ₹{item['amount']:.2f}")
    print(f"Total for {category}: ₹{total:.2f}")



expenses = load_expenses()

while True:
    print("1. Add expense.")
    print("2. View expense.")
    print("3. View summary.")
    print("4. Filter by category.")
    print("5. Exit.")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("==========================")
        add_expense()
        print("==========================")

    elif choice == "2":
        print("==========================")
        view_expenses()
        print("==========================")
    
    elif choice == "3":
        print("==========================")
        view_summary()
        print("==========================")

    elif choice == "4":
        print("==========================")
        filter_expenses()
        print("==========================")

    elif choice == "5":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice")

    print()