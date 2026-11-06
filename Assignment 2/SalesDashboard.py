
import pandas as pd
import time

def load_csv(filepath):
    print(f"Loading CSV file from: {filepath}")
    start_time = time.time()

    try:
        df = pd.read_csv(filepath, engine='pyarrow', on_bad_lines='skip')
        end_time = time.time()
        load_time = end_time - start_time

        df = df.fillna(0)

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

def display_initial_rows(data):
    """Ask the user how many initial rows to show."""
    while True:
        response = input(
            f"\nHow many rows would you like to see? "
            f"(1-{len(data)}, 'all', or Enter to skip): "
        ).strip().lower()

        if response == "":
            print("Preview skipped.")
            return

        if response == "all":
            print(data.to_string(index=False))
            return

        try:
            num_rows = int(response)
        except ValueError:
            print("Invalid input. Please enter a number or 'all'.")
            continue

        if num_rows < 1 or num_rows > len(data):
            print(f"Please enter a number between 1 and {len(data)}.")
            continue

        print(data.head(num_rows))
        return


def not_ready(data):
    print("This function is not ready yet.")


def exit_program(data=None):
    print("Exiting the program. Goodbye!")
    raise SystemExit(0)



menu_options = (
    ("Show the first n rows of sales data", display_initial_rows),
    ("Total sales by region and order_type", not_ready),
    ("Average sales by region with average sales by state and sale type", not_ready),
    ("Sales by customer type and order type by state", not_ready),
    ("Total sales quantity and price by region and product", not_ready),
    ("Total sales quantity and price by customer type", not_ready),
    ("Max and min sales price by category", not_ready),
    ("Number of unique employees by region", not_ready),
    ("Create a custom pivot table", not_ready),
    ("Exit", exit_program),
)



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


csv_file = "sales_data.csv"
sales_data = load_csv(csv_file)

if sales_data is not None:
    while True:
        selection = display_menu()
        _, action = menu_options[selection]
        action(sales_data)
