1. Overview
This program is a text-based sales dashboard built with Python and Pandas. It lets users explore sales data and create pivot tables to analyze sales by region, product, customer type, and employees.

The dashboard includes some predefined sales analyses and a custom pivot table option. Users can also choose between two CSV datasets and export results to Excel files.

# How to Run the Program
1. Make sure Python is installed on your computer.
2. Install the required libraries: Pandas, PyArrow, and OpenPyXL.
3. Put SalesDashboard.py, sales_data.csv, and sales_data_test.csv in the same folder.
4. Open the folder in VS Code.
5. Open the Terminal and run:  python3 SalesDashboard.py
6. Choose which dataset to load:
    - Enter 1 for the full sales dataset.
    - Enter 2 for the 10-row test dataset.
7. After the data is loaded, the program will show the Sales Data Menu. Enter a number from 1 to 10 to select an option.

# Menu Options and Examples
The dashboard has 10 menu options:

1. Show the first n rows of sales data: Shows the number of rows entered by the user. Users can also type all to see all rows, or press Enter to skip.

2. Total sales by region and order type: Shows total sales for Retail and Wholesale orders in each sales region.

3. Average sales by region, state, and order type: Calculates average sales for each region, state, and order type.

4. Sales by customer type and order type by state: Shows total sales grouped by state, customer type, and order type.

5. Total sales quantity and price by region and product: Shows the total quantity sold and total sales amount for each product in each region.

6. Total sales quantity and price by customer type: Shows total quantity and sales grouped by order type and customer type.

7. Max and min sales price by category: Shows the highest and lowest sales amounts for each product category.

8. Number of unique employees by region: Counts the number of different employees in each sales region.

9. Create a custom pivot table: Lets users choose their own rows, columns, values, and aggregation functions.

10. Exit: Closes the program.

Example 1: Display Sales Data
    Select option 1 and enter 5 to display the first five rows of sales data.

Example 2: Create a Custom Pivot Table
    Select option 9 and choose:

    Rows: sales_region

    Columns: Press Enter to skip

    Values: quantity and unit_price

    Aggregation functions: sum and mean

    The program will create a pivot table showing the total and average quantity and unit price for each sales region.

Example 3: Export Results to Excel
    After viewing an analysis, the program asks if the user wants to export the results.

    Enter y and provide a filename such as sales_report.xlsx. The Excel file will be saved in the current working folder.

    Enter n to skip exporting and return to the main menu.

# Error Handling
The program includes error handling to prevent common problems.

1. Invalid menu selection: If the user enters an invalid menu number, the program shows an error message and asks again.

2. Invalid row input: If the user enters a number greater than the available rows, or enters text instead of a number, the program asks for a valid input.

3. Missing CSV file: If the selected CSV file cannot be loaded, the program shows an error message and exits.

4. Missing columns: The program checks for required columns and shows a warning if any are missing. The predefined analysis functions also check for the columns they need.

5. Invalid pivot table selection: If the user enters an invalid number or leaves a required selection empty, the program asks again.

6. Excel export errors: The program checks for an empty filename and handles errors when saving Excel files. It also asks again if the user enters something other than y or n.

These checks make the dashboard easier to use and help prevent common errors.