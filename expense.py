import json
from datetime import datetime


def load_expense():
    try:
        with open("expenses.json","r") as file:
           return json.load(file)
    except FileNotFoundError:
        return []

   
expense = load_expense()



def menu():
    print("-"*15)
    print("EXPENSE TRACKER")
    print("-"*15)

    print("1.Add Expense.")
    print("2.Show Expense.")
    print("3.Total Expense.")
    print("4.Highest Expense.")
    print("5.Lowest Expense.")
    print("6.Average Expense.")
    print("7.Delete Expense.")
    print("8.Sort Expense.")
    print("9.Exit.")

    print("-"*15)
    



def add_expnese():
    name_exp = input("Enter the Name of product: ")
    des_exp = input("Enter the Description of product:")

    while True:
        try:
            amount_exp = int(input("Enter the Amount of product: "))
            break     # exit the nearest loop which is while True here
        except ValueError:
                print("Only numbers accpeted!")

    while True:
        try:
            date_exp = input("Enter date (DD-MM-YYYY): ")
            date_exp = datetime.strptime(date_exp, "%d-%m-%Y")
            date_exp = date_exp.strftime("%d-%m-%Y") 

            
            break
        except ValueError:
             print("Enter date in DD-MM-YYYY format") 

    product_details = {
        "Name of product" : name_exp,
        "Description of product" : des_exp,
        "Amount of product" : amount_exp,
        "Date of expense" : date_exp
    }      

    expense.append(product_details)  
    save_expense()

    print("="*15)
      



def show_exp():
    if if_not():
        return
    
    for exp in expense:
        print(f"Product name: {exp['Name of product']}")          
        print(f"Product description: {exp['Description of product']}")          
        print(f"Product amount: {exp['Amount of product']}")          
        print(f"Expense date: {exp['Date of expense']}")
          

        print("="*15) 




def total_expense():
    if if_not():    #  here there is if condition as well as we are calling the function
        return   # only run if if_not() is true, if block only runs when it is true and never on false
    
    total  = 0
    for exp in expense:
        total = total + exp['Amount of product'] 

    print(f"Total expense is: {total}.")  




def high_expense():
    if if_not():
        return
    
    highest_expense = 0
    highest_name = ""
    highest_descrip = ""
    highest__date = ""

    for exp in expense:
        if exp['Amount of product']> highest_expense:
            highest_expense = exp['Amount of product'] 
            highest_name = exp['Name of product']
            highest_descrip = exp['Description of product']
            highest__date = exp['Date of expense']

    print(f"Highest Expense: {highest_expense}")        
    print(f"Expense Name: {highest_name}")        
    print(f"Description: {highest_descrip}")        
    print(f"Date: {highest__date.strftime('%d-%m-%Y')}")  





def low_expense():
    if if_not():
            return
    
    lowest_expense = float('inf')
    lowest__name = ""
    lowest_descrip = ""
    lowest__date = ""

    for exp in expense:
        if exp['Amount of product'] < lowest_expense:
            lowest_expense = exp['Amount of product'] 
            lowest_name = exp['Name of product']
            lowest_descrip = exp['Description of product']
            lowest_date = exp['Date of expense']

    print(f"Lowest Expense: {lowest_expense}")        
    print(f"Expense Name: {lowest_name}")        
    print(f"Description: {lowest_descrip}")        
    print(f"Date: {lowest_date.strftime('%d-%m-%Y')}")  





def average_expense():
    if if_not():
                return
    total = 0

    for exp in expense:
        total = total + exp['Amount of product']

    average = total / len(expense)

    print(f"Average Expense: {average}")





def sorted_expense():
    if if_not():
        return

    sort_expenses = sorted(expense,key=lambda exp : exp['Date of expense'], reverse=True)

    for exp1 in sort_expenses:
        print(f"Expense date: {exp1['Date of expense'].strftime('%d-%m-%Y')}")
        print(f"Product name: {exp1['Name of product']}")
        print(f"Product description: {exp1['Description of product']}")
        print(f"Product amount: {exp1['Amount of product']}")
        
        print("=" * 15)





def save_expense():
    
    with open("expenses.json","w") as file:
        json.dump(expense,file)




def delete_expense():  #this module is how a senior dev would code this function.
    if not expense:
        print("No Expense Entered Yet.")
        return

    print("\nSelect the expense to delete:")

    for index, exp in enumerate(expense, start=1):  #here start =1 is just to show to the user, the pyhton ndex still remains same i.e i=0
        print(f"{index}. {exp['Name of product']} - ₹{exp['Amount of product']}")

    while True:
        try:
            choice = int(input("Enter expense number: "))

            if 1 <= choice <= len(expense):
                deleted = expense.pop(choice - 1)  # if user enter 1 which is 1.Apple ,but in list the index for first item is 0.Apple  ,so to match that we do -1 , then user enter 1, 1-1 = 0 ,pyhton deletes first item in list at index 0 which user wants to delete,but it appears to user as 1.Apple. Remember !!! Python Index Remains Unchanged, start = 1 is just a visual clarity to users and not inedx starting from 1.
                save_expense()
                print(f"{deleted['Name of product']} deleted successfully.")
                return

            print("Invalid expense number.")

        except ValueError:
            print("Please enter a number.")





def exit_expense():
    exit()            
         
 
          
def if_not():       # better to not do this in senior project,just do the one in advance_expense(file)            
    if not expense:
        print("No Expense Entered Yet.")
        return True                      
    return False 



while True:
    menu()
    while True:
        try:
            choice = int(input("Enter your choice : "))
            if choice in (1,2,3,4,5,6,7,8,9):
                break
            else:
                print("Enter number from above mentioned list only.")
                continue
        except ValueError:
            print("Invalid input.")
             
    
    if choice == 1:
        print("Calling add expense...")
        add_expnese()
    elif choice == 2:
        show_exp()
    elif choice == 3:
        total_expense()
    elif choice == 4:
        high_expense()
    elif choice == 5:
        low_expense()
    elif choice == 6:
        average_expense()
    elif choice == 7:
        delete_expense()
    elif choice == 8:
        sorted_expense()
    elif choice == 9:
        exit_expense()    
