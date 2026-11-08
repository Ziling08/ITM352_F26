# Ziling He
# Date: Nov. 4, 2026
# Assignment 2: Sales Dashboard


import pandas as pd
import time

# Load the sales data before showing the dashboard menu.
# Check if the file has the columns needed for the analysis.
def load_csv(filepath):
    # Read the CSV file and show how long it takes.
    print(f"Loading CSV file from: {filepath}")
    start_time = time.time()

    try:
        df = pd.read_csv(filepath, engine='pyarrow', on_bad_lines='error')
        end_time = time.time()
        load_time = end_time - start_time
        
        # Replace missing values with 0.
        df = df.fillna(0)

        # Check if the columns needed for the sales analysis exist.
        required_columns = [
             "sales_region", "order_type", "customer_state",
            "customer_type", "product_category", "produce_name",
            "quantity", "unit_price", "employee_id"
        ]

        missing_columns = []

        for col in required_columns:
            if col not in df.columns:
                missing_columns.append(col)

        if missing_columns:
            print("Missing required columns:", missing_columns)
            print("Some analytics may not work.")
        else:
            print("All required columns are available.")

        print(f"CSV file loaded successfully in {load_time:.2f} seconds.")
        print(f"Number of rows: {len(df)}")
        print("Available columns:")
        print(df.columns.tolist())

        return df

    except Exception as e:
        print("Error reading the CSV file:", e)
        return None
    
# Let users preview the sales data before running an analysis.
# Users can choose a number of rows, all rows, or skip the preview.
def display_initial_rows(data):
    """Ask the user how many initial rows to show."""
    while True:
        response = input(
            f"\nHow many rows would you like to see? "
            f"(1-{len(data)}, 'all', or Enter to skip): "
        ).strip().lower()

        # Press Enter to skip, or type all to see everything.
        if response == "":
            print("Preview skipped.")
            return

        if response == "all":
            print(data.to_string(index=False))
            export_to_excel(data)
            return
        # Make sure the row number is a valid number.
        try:
            num_rows = int(response)
        except ValueError:
            print("Invalid input. Please enter a number or 'all'.")
            continue

        if num_rows < 1 or num_rows > len(data):
            print(f"Please enter a number between 1 and {len(data)}.")
            continue

        result = data.head(num_rows)
        print(result)
        export_to_excel(result)
        return

def exit_program(data=None):
    print("Exiting the program. Goodbye!")
    raise SystemExit(0)


# These functions use pivot tables to analyze sales by region,
# customer type, product, and other categories.
# Sales amount is calculated using quantity * unit_price.
# AI Usage: I used ChatGPT to help me debug this function and fix errors with input validation.
def show_total_sales_by_region(data):
    """Show total sales by region and order type."""

    required = ["sales_region", "order_type", "quantity", "unit_price"]

    missing = []
    for col in required:
        if col not in data.columns:
            missing.append(col)

    if missing:
        print("Cannot perform this analysis. Missing columns:", missing)
        return


    sales = data.copy()
    sales["sales"] = sales["quantity"] * sales["unit_price"]

    pivot_table = pd.pivot_table(
        sales,
        index="sales_region",
        columns="order_type",
        values="sales",
        aggfunc="sum",
        fill_value=0
    )

    print("\nTotal sales by region and order type:")
    print(pivot_table.round(2))

    export_to_excel(pivot_table)


def show_average_sales_by_region(data):
    """Show average sales by region, state, and order type."""
    # Use mean to find the average sales for each group.
    required = ["sales_region", "customer_state", "order_type",
                "quantity", "unit_price"]

    missing = []
    for col in required:
        if col not in data.columns:
            missing.append(col)

    if missing:
        print("Cannot perform this analysis. Missing columns:", missing)
        return


    sales = data.copy()
    sales["sales"] = sales["quantity"] * sales["unit_price"]

    pivot_table = pd.pivot_table(
        sales,
        index="sales_region",
        columns=["customer_state", "order_type"],
        values="sales",
        aggfunc="mean",
        fill_value=0
    )

    print("\nAverage sales by region, state, and order type:")
    print(pivot_table.round(2))
    export_to_excel(pivot_table)

# Group the sales by state, customer type, and order type.
def show_sales_by_customer_type(data):
    """Show sales by state, customer type, and order type."""

    required = ["customer_state", "customer_type", "order_type",
                "quantity", "unit_price"]

    missing = []
    for col in required:
        if col not in data.columns:
            missing.append(col)

    if missing:
        print("Cannot perform this analysis. Missing columns:", missing)
        return


    sales = data.copy()
    sales["sales"] = sales["quantity"] * sales["unit_price"]

    pivot_table = pd.pivot_table(
        sales,
        index=["customer_state", "customer_type", "order_type"],
        values="sales",
        aggfunc="sum",
        fill_value=0
    )

    print("\nSales by customer type and order type by state:")
    print(pivot_table.round(2))
    export_to_excel(pivot_table)

def show_sales_by_product(data):
    """Show total quantity and sales by region and product."""
    # Add the quantity and sales for each product.
    required = ["sales_region", "produce_name", "quantity", "unit_price"]

    missing = []
    for col in required:
        if col not in data.columns:
            missing.append(col)

    if missing:
        print("Cannot perform this analysis. Missing columns:", missing)
        return


    sales = data.copy()
    sales["sales"] = sales["quantity"] * sales["unit_price"]

    pivot_table = pd.pivot_table(
        sales,
        index=["sales_region", "produce_name"],
        values=["quantity", "sales"],
        aggfunc="sum",
        fill_value=0
    )

    print("\nTotal sales quantity and price by region and product:")
    print(pivot_table.round(2))
    export_to_excel(pivot_table)

def show_sales_by_customer(data):
    """Show total quantity and sales by order and customer type."""
    # Compare order types and customer types.
    required = ["order_type", "customer_type", "quantity", "unit_price"]

    missing = []
    for col in required:
        if col not in data.columns:
            missing.append(col)

    if missing:
        print("Cannot perform this analysis. Missing columns:", missing)
        return


    sales = data.copy()
    sales["sales"] = sales["quantity"] * sales["unit_price"]

    pivot_table = pd.pivot_table(
        sales,
        index=["order_type", "customer_type"],
        values=["quantity", "sales"],
        aggfunc="sum",
        fill_value=0
    )

    print("\nTotal sales quantity and price by customer type:")
    print(pivot_table.round(2))
    export_to_excel(pivot_table)

def show_max_min_sales(data):
    """Show maximum and minimum sales by product category."""
    # Find the largest and smallest sales amounts.
    required = ["product_category", "quantity", "unit_price"]

    missing = []
    for col in required:
        if col not in data.columns:
            missing.append(col)

    if missing:
        print("Cannot perform this analysis. Missing columns:", missing)
        return

    sales = data.copy()
    sales["sales"] = sales["quantity"] * sales["unit_price"]

    pivot_table = pd.pivot_table(
        sales,
        index="product_category",
        values="sales",
        aggfunc=["max", "min"]
    )

    print("\nMax and min sales price by category:")
    print(pivot_table.round(2))
    export_to_excel(pivot_table)

# AI Usage (ChatGPT):
# Prompt summary: How can I count unique employees in each sales region using Pandas?
# ChatGPT helped me use nunique.
def show_employees_by_region(data):
    """Show the number of unique employees by sales region."""
    # nunique counts each employee only once in a region.
    required = ["sales_region", "employee_id"]

    missing = []
    for col in required:
        if col not in data.columns:
            missing.append(col)

    if missing:
        print("Cannot perform this analysis. Missing columns:", missing)
        return


    pivot_table = pd.pivot_table(
        data,
        index="sales_region",
        values="employee_id",
        aggfunc="nunique"
    )

    print("\nNumber of unique employees by region:")
    print(pivot_table)
    export_to_excel(pivot_table)

# This function is used by the custom pivot table.
# It lets users select fields and checks for invalid inputs.
# ChatGPT helped me with input validation so users can select more than one option and avoid invalid inputs.
def get_user_selection(options, prompt, required=False, single=False):
    """Ask the user to select options."""

    while True:
        print(prompt)

        for i, option in enumerate(options):
            print(f"{i+1}. {option}")

        choice = input("Enter the number(s) of your choice(s), separated by commas: ").strip()

        if not choice:
            if required:
                print("A selection is required.")
                continue
            return []
        # Change the numbers entered by the user into a list.
        try:
            indexes = [int(i) for i in choice.split(',')]
        except ValueError:
            print("Invalid input. Please enter numbers separated by commas.")
            continue

        if any(i < 1 or i > len(options) for i in indexes):
            print(f"Each number must be between 1 and {len(options)}.")
            continue

        selected = list(dict.fromkeys(options[i - 1] for i in indexes))

        if single and len(selected) != 1:
            print("Please select exactly one option.")
            continue

        return selected

# Let users create their own analysis instead of only
# using the predefined pivot tables in the menu.
# Prompt summary: How can I create a custom pivot table where users choose rows, columns, values, and functions?
# I asked ChatGPT how to let users choose rows, columns, values, and functions for a custom pivot table.
# I tested different combinations to check the results.
def generate_custom_pivot_table(data):
    """Allow the user to create a custom pivot table."""
    # Let the user pick rows, columns, and values.
    row_options = list(data.columns)
    rows = get_user_selection(
        row_options, "\nSelect rows (required):", required=True
    )

    col_options = [col for col in row_options if col not in rows]
    cols = get_user_selection(
        col_options, "\nSelect columns (optional, Enter to skip):"
    )

    value_options = list(data.select_dtypes(include=['number']).columns)

    if not value_options:
        print("No numeric columns available.")
        return
    
    values = get_user_selection(
        value_options, "\nSelect values to aggregate:",
        required=True
    )
    # The user can choose more than one calculation
    agg_options = ['sum', 'mean', 'count']
    agg_func = get_user_selection(
        agg_options, "\nSelect aggregation function:",
        required=True
    )
    # Try creating the pivot table and show an error if it fails.
    try:
        pivot_table = pd.pivot_table(
            data,
            index=rows,
            columns=cols if cols else None,
            values=values,
            aggfunc=agg_func,
            fill_value=0
        )

    except Exception as e:
        print("Could not create the pivot table:", e)
        return

    print("\nCustom pivot table:")
    print(pivot_table.round(2))
    export_to_excel(pivot_table)



# Individual Requirement 1: Export results to Excel
# This allows users to save analysis results for later use.
# Prompt summary: How can I ask users if they want to export a pivot table to Excel and choose a filename?
# ChatGPT helped me add the Excel export option and handle invalid inputs and empty filenames.
def export_to_excel(result):
    """Ask the user if they want to export results to Excel."""

    while True:
        choice = input("Would you like to export to Excel? (y/n): ").strip().lower()
        # Save the table only if the user enters y.
        if choice == "y" or choice == "n":
            break
        else:
            print("Invalid input. Please enter y or n.")

    if choice == "y":
        filename = input("Enter Excel filename: ").strip()

        if not filename:
            print("Filename cannot be empty.")
            return

        if not filename.endswith(".xlsx"):
            filename += ".xlsx"

        try:
            result.to_excel(filename)
            print(f"File exported successfully: {filename}")
        except Exception as e:
            print("Error exporting file:", e)

    else:
        print("Export skipped.")



# Connect each menu option to a function.
# This allows users to choose different analyses from one menu.
menu_options = (
    ("Show the first n rows of sales data", display_initial_rows),
    ("Total sales by region and order_type", show_total_sales_by_region),
    ("Average sales by region with average sales by state and sale type", show_average_sales_by_region),
    ("Sales by customer type and order type by state", show_sales_by_customer_type),
    ("Total sales quantity and price by region and product", show_sales_by_product),
    ("Total sales quantity and price by customer type", show_sales_by_customer),
    ("Max and min sales price by category", show_max_min_sales),
    ("Number of unique employees by region", show_employees_by_region),
    ("Create a custom pivot table", generate_custom_pivot_table),
    ("Exit", exit_program),
)


# Show the main menu after the CSV file is loaded.
# Keep asking until the user enters a valid menu number.
def display_menu():
    """Show the menu and return a valid selection as an index into menu_options."""
    while True:
        print("\nSales Data Menu")
        for number, (description, _) in enumerate(menu_options, start=1):
            print(f"  {number}. {description}")

        choice = input(f"Select an option (1-{len(menu_options)}): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(menu_options):
            return int(choice) - 1
        print(f"Invalid selection '{choice}'. Please enter a number from 1 to {len(menu_options)}.")


# Individual Requirement 3: Choose a CSV dataset.
# Users can select the full dataset or the smaller test dataset.
# Prompt summary: How can I let users choose between sales_data.csv and sales_data_test.csv before loading?
# ChatGPT helped me add an option to choose between two CSV files.
def choose_dataset():
    """Allow the user to select a CSV file."""
    # The user can use the full file or the smaller test file.


    while True:
        print("\nSelect a dataset:")
        print("1. sales_data.csv")
        print("2. sales_data_test.csv")

        choice = input("Enter your choice (1-2): ").strip()

        if choice == "1":
            return "sales_data.csv"
        elif choice == "2":
            return "sales_data_test.csv"
        else:
            print("Invalid selection. Please enter 1 or 2.")

# Start the program by choosing and loading a dataset.
csv_file = choose_dataset()
sales_data = load_csv(csv_file)

# Keep showing the menu until the user chooses Exit.
if sales_data is not None:
    while True:
        selection = display_menu()
        _, action = menu_options[selection]
        action(sales_data) 