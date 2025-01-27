![WhatsApp Image 2025-01-20 at 00 54 20](https://github.com/user-attachments/assets/c6f47f78-a165-4ab5-ac6f-6b6bf4ce66ee)
# Money Map 

Money Map is a budget tracker designed to help users manage their expenses and savings. This application is entirely written in Python and integrates Figma UI assets with Pillow and Tkinter to create an intuitive, user-friendly interface. The primary goal is to provide a simple yet powerful tool for users to categorize transactions, set budgets, and view financial summaries.

## Key Features
- **Categorization of transactions**: Easily categorize income and expenses.
- **Budget creation and management**: Set up budgets and track spending.
- **Financial summary reports and visualizations**: View financial summaries with pie charts and other visualizations.
- **File-based storage**: Uses JSON for storing data.
- **User-friendly interface**: Integrated with Figma UI assets, enhanced with Pillow and Tkinter.
- **Income functionality**: Supports better handling of expenses and budgeting by tracking income.

## Technical Details

### Platform
- **Operating System**: Windows 10/11 (32/64-bit)
- **Programming Language**: Python 3.9 or higher recommended
- **UI Framework**: Tkinter (Frontend) integrated with Figma UI assets (exported via Pillow)

### Libraries & Tools
- **Tkinter**: For frontend development.
- **Pillow**: To enhance Figma UI assets for a polished look.
- **Matplotlib**: Integrated for generating financial report visualizations like pie charts.
- **JSON**: For file-based data storage.

### Overview
The platform leverages Python's simplicity and robust ecosystem to create an efficient, user-friendly experience. Tkinter is used for the native UI, while Figma design assets are seamlessly integrated via Pillow, ensuring a visually appealing and functional interface tailored for personal budgeting.

## Project Structure

- **backend/**: Contains core backend modules:
  - `budget_handler.py`: Manages the creation, update, and deletion of budgets.
  - `transactions_handler.py`: Handles income and expense transactions.
  - `user_storage.py`: Provides functionality to store and retrieve user-related data.
  - `report_generator.py`: Generates financial summaries and visualizations, leveraging Matplotlib.

- **frontend/**: Includes the user interface assets:
  - **assets/**: Stores UI design assets exported from Figma.
  - `assets.py`: Integrates and manages the use of these assets in the Tkinter-based application.

- **userdata/**: Stores user data in JSON format:
  - `income.json`: Contains user income data.
  - `budgets.json`: Maintains user budget information for tracking expenses.
  - `transactions.json`: Logs all user transactions, both income and expenses.

- `Main.py`: The entry point of the application, responsible for initializing and launching the program.
- `LICENSE`: Contains the terms and conditions under the MIT License, allowing open-source use and distribution.
- `README.md`: Provides an overview, instructions, and details about the project for users and contributors.

## Installation and Usage

1. Clone the repository or download the source code.

2. Ensure Python is installed on your system.

3. Install required libraries using:

    ```bash
    pip install matplotlib pillow
    ```

4. Run the application:

    ```bash
    python main.py
    ```

Once the application is launched, the interface allows you to input and manage income, expenses, and transactions, providing a clear overview of your financial data. You can easily track budgets, view financial summaries, and visualize your spending. Additionally, the application supports adding and removing data as needed, ensuring seamless management of your finances.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
