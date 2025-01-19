from backend.transaction_handler import TransactionHandler

def main():
    transaction_handler = TransactionHandler()

    while True:
        print("\n1. Add Transaction")
        print("2. View Transactions")
        print("3. Remove Transaction")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            amount = float(input("Enter amount(in Euros): "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            transaction_handler.add_transaction(amount, category, description)
        elif choice == '2':
            print("\nCurrent transactions:")
            transactions = transaction_handler.view_transactions()
            for i, transaction in enumerate(transactions):
                print(f"{i}. Amount: {transaction['amount']} | Category: {transaction['category']} | Description: {transaction['description']}")
        elif choice == '3':
            try:
                index = int(input("Enter the index of the transaction to remove: "))
                transaction_handler.remove_transaction(index)
            except ValueError:
                print("Invalid input. Please enter a valid index.")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
