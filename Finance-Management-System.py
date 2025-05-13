import csv

class Transaction:
 def __init__(self, date , amount , type , category):  # Constructor to initialize variables
        self.date = date
        self.amount = float(amount)                           # Amount of the transaction
        if self.amount < 0:
         raise ValueError("Amount cannot be negative.")
        self.type = type                               # Type of transaction
        if self.type not in ["income" ,"expense"]:
         raise ValueError("Invalid type of transaction.")
        self.category = category                       # Category of the transaction

 def displayInfo(self):                                 # Display transaction details
    print(f"Date of the transaction: {self.date}")
    print(f"Amount of the transaction: {self.amount}")
    print(f"Type of the transaction: {self.type}")
    print(f"Category of the transaction: {self.category}\n")


class FinanceManager:
 def __init__(self):
        self.transactions = [ ] # List to store transactions

 def addTransaction(self, transaction):
    self.transactions.append(transaction)
    print("Transaction added successfully.")

 def generateReport(self):    # Generate and display a financial report
  total_income = sum(
     transaction.amount for transaction in self.transactions if transaction.type == "income")
  total_expenses = sum(
     transaction.amount for transaction in self.transactions if transaction.type == "expense")
  savings = total_income - total_expenses

  print("\n--- Financial Summary Report ---")
  print(f"Total Income: {total_income}")
  print(f"Total Expenses: {total_expenses}")
  print(f"Savings: {savings}\n")
 
 def filterByCategory(self, category):
    filteredTransactions = [transaction for transaction in self.transactions if transaction.category == category ]
    if not filteredTransactions:
            print(f"No transactions found for category: {category}")
    else:
        for transaction in filteredTransactions:
            transaction.displayInfo()
    return filteredTransactions

# Save all transactions to a file
 def saveToFile(self, filename):
   try:
      with open(filename, 'w', newline='') as file:
         writer = csv.writer(file) # Write header
         writer.writerow(["Date", "Amount", "Type", "Category"]) # Write transactions
         for transaction in self.transactions:
            writer.writerow([transaction.date, transaction.amount, transaction.type, transaction.category])
            print(f"Transactions successfully saved to {filename}.")
   except Exception as e:
            print(f"Error saving to file: {e}")

# Load transactions from a file
 def loadFromFile(self, filename):
   try:
      with open(filename, 'r') as file:
         reader = csv.DictReader(file)
         for row in reader:
            self.addTransaction(Transaction(row['Date'], row['Amount'], row['Type'], row['Category']))
            print(f"Transactions successfully loaded from {filename}.")
   except FileNotFoundError:
      ("File not found. Please provide a valid filename.")
   except Exception as e:
      print(f"Error loading from file: {e}")

   except FileNotFoundError:
      print(f"File '{filename}' not found. Please provide a valid filename.")
   except ValueError as e:
       print(f"Error in file data: {e}")
   except Exception as e:
       print(f"Unexpected error while loading from file: {e}")

 def getTopExpenses(self, n):
      try:
         expenses = sorted(
            [t for t in self.transactions if t.type == "expense"],
            key=lambda x: x.amount, reverse=True)
         top_expenses = expenses[:n]
         if not top_expenses:
            print(f"No expenses found.")
            return []
         print(f"\n--- Top {n} Expenses ---")
         for expense in top_expenses:
            expense.displayInfo()
         return top_expenses
      except Exception as e:
         print(f"Error: {e}")

 def getCategorySummary(self):
      try:
         if not self.transactions:
            raise ValueError("No transactions available to summarize.")
         summary = {}
         for transaction in self.transactions:
            if transaction.category not in summary:
               summary[transaction.category] = {"income": 0, "expense": 0}
            summary[transaction.category][transaction.type] += transaction.amount
            
            print("\n--- Category Summary ---")
            for category, totals in summary.items():
               print(f"Category: {category}")
               print(f"  Total Income: {totals['income']}")
               print(f"  Total Expenses: {totals['expense']}\n")
            return summary
      except Exception as e:
         print(f"Error: {e}")


def main():
   fm = FinanceManager()  # Create an instance of FinanceManager
   
   while True:
        # Display the menu
        print("\nWelcome to the Personal Finance Management System.")
        print("1. Add Transaction")
        print("2. Generate Report")
        print("3. Filter by Category")
        print("4. Save to File")
        print("5. Load from File")
        print("6. Get Top Expenses")
        print("7. Get Category Summary")
        print("8. Exit")
        
        try:
            # Get user choice
            choice = int(input("Select an option: "))

            if choice == 1:
                # Add a new transaction
                print("Enter transaction details:")
                date = input("Date (YYYY-MM-DD): ")
                amount = input("Amount: ")
                type = input("Type (income/expense): ").lower()
                category = input("Category: ")
                try:
                    fm.addTransaction(Transaction(date, amount, type, category))
                except ValueError as e:
                    print(f"Error adding transaction: {e}")

            elif choice == 2:
                # Generate financial report
                fm.generateReport()

            elif choice == 3:
                # Filter transactions by category
                category = input("Enter category to filter by: ")
                fm.filterByCategory(category)

            elif choice == 4:
                # Save transactions to a file
                filename = input("Enter filename to save transactions (e.g., transactions.csv): ")
                fm.saveToFile(filename)

            elif choice == 5:
                # Load transactions from a file
                filename = input("Enter filename to load transactions (e.g., transactions.csv): ")
                fm.loadFromFile(filename)

            elif choice == 6:
                # Get top n expenses
                try:
                    n = int(input("Enter the number of top expenses to display: "))
                    fm.getTopExpenses(n)
                except ValueError:
                    print("Please enter a valid number.")

            elif choice == 7:
                # Get category summary
                fm.getCategorySummary()

            elif choice == 8:
                # Exit the program
                print("Exiting the system. Goodbye!")
                break

            else:
                print("Invalid choice. Please select a valid option.")

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 8.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Run the program
if __name__ == "__main__":
    main()


#For some reason i cant run the program properly in Visual studio code.
#But when i try to run it in Python launcher(in terminal),
#it runs properly and running with all properties. 