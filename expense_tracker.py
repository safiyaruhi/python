#expense_tracker
expenses=[]
def add_expense():
    expense_name=input("expense name:")
    amount=float(input("amount:"))
    category=input("category")

    expense = {
        "name":expense_name,
        "amount":amount,
        "category":category
    }
    expenses.append(expense)
    print("Expense added succesfully!")
def view_expenses():
    if not expenses:
        print("No expenses recorded yet")
    else:
        print("\n------ALL EXPENSES------")
        for expense in expenses:
            print(
                expense["name"],
                "-Rs.",expense["amount"],
                "-",expense["category"]
            )
def total_expenses():
    total=0
    for expense in expenses:
        total +=expense["amount"]
    print("Total expenses: Rs.",total)

def category_summary():
    if len(expenses)==0:
        print("no expenses added yet.")
        return
    summary = {}
    for expense in expenses:
        category= expense["category"]
        amount = expense["amount"]

        if category in summary:
            summary[category]+=amount
        else:
            summary[category]=amount

    print("\ncategory summary:")
    for category,amount in summary.items():
        print(category,";Rs",amount)  
print("========EXPENSE TRACKER========")

while True:
    print("1. ADD EXPENSE\n2.VIEW EXPENSES\n3.VIEW TOTAL EXPENSES\n4.CATEGORY SUMMARY\n5.EXIT")
    choice=(input("enter your choice:"))
    if(choice=='1'):
        add_expense()
    elif choice=='2':
        view_expenses()
    elif choice=='3':
        total_expenses()
    elif choice=='4':
        category_summary()
    elif choice=='5':
        print("thankyou for using expense tracker!")
        break
    else:
        print("invalid choice.Please try again")

