I tested my program in the VS Code Terminal. I used sales_data.csv and sales_data_test.csv to check if the menu, pivot tables, and Excel export worked. I also tried some wrong inputs to see if the program would show an error message.

# I tried entering a wrong dataset number and then loaded the test dataset:
Select a dataset:
1. sales_data.csv
2. sales_data_test.csv
Enter your choice (1-2): 3
Invalid selection. Please enter 1 or 2.

Select a dataset:
1. sales_data.csv
2. sales_data_test.csv
Enter your choice (1-2): 2
Loading CSV file from: sales_data_test.csv
All required columns are available.
CSV file loaded successfully in 0.02 seconds.
Number of rows: 10
Available columns:
['order_number', 'employee_id', 'employee_name', 'job_title', 'sales_region', 'order_date', 'order_type', 'customer_type', 'customer_name', 'customer_state', 'product_category', 'product_number', 'produce_name', 'quantity', 'unit_price']

# I also tested a wrong menu number:
Sales Data Menu
  1. Show the first n rows of sales data
  2. Total sales by region and order_type
  3. Average sales by region with average sales by state and sale type
  4. Sales by customer type and order type by state
  5. Total sales quantity and price by region and product
  6. Total sales quantity and price by customer type
  7. Max and min sales price by category
  8. Number of unique employees by region
  9. Create a custom pivot table
  10. Exit
Select an option (1-10): 11
Invalid selection '11'. Please enter a number from 1 to 10.

# I tested the full dataset and different row inputs:
Select a dataset:
1. sales_data.csv
2. sales_data_test.csv
Enter your choice (1-2): 1
Loading CSV file from: sales_data.csv
All required columns are available.
CSV file loaded successfully in 0.02 seconds.
Number of rows: 5130
Available columns:
['order_number', 'employee_id', 'employee_name', 'job_title', 'sales_region', 'order_date', 'order_type', 'customer_type', 'customer_name', 'customer_state', 'product_category', 'product_number', 'produce_name', 'quantity', 'unit_price']

Select an option (1-10): 1

How many rows would you like to see? (1-5130, 'all', or Enter to skip): 6000
Please enter a number between 1 and 5130.

How many rows would you like to see? (1-5130, 'all', or Enter to skip): abc
Invalid input. Please enter a number or 'all'.

How many rows would you like to see? (1-5130, 'all', or Enter to skip): 
Preview skipped.
I tested the custom pivot table inputs:
Select rows (required):
1. order_number
2. employee_id
3. employee_name
4. job_title
5. sales_region
6. order_date
7. order_type
8. customer_type
9. customer_name
10. customer_state
11. product_category
12. product_number
13. produce_name
14. quantity
15. unit_price
Enter the number(s) of your choice(s), separated by commas: 99
Each number must be between 1 and 15.

Enter the number(s) of your choice(s), separated by commas: 
A selection is required.

Enter the number(s) of your choice(s), separated by commas: 1,abc
Invalid input. Please enter numbers separated by commas.

# I also tried a combination that could not make a pivot table. The program showed an error and went back to the menu:
Enter the number(s) of your choice(s), separated by commas: 10

Select columns (optional, Enter to skip):
1. order_number
2. employee_id
3. employee_name
4. job_title
5. sales_region
6. order_date
7. order_type
8. customer_type
9. customer_name
10. product_category
11. product_number
12. produce_name
13. quantity
14. unit_price
Enter the number(s) of your choice(s), separated by commas: 1

Select values to aggregate:
1. order_number
2. employee_id
3. quantity
4. unit_price
Enter the number(s) of your choice(s), separated by commas: 1

Select aggregation function:
1. sum
2. mean
3. count
Enter the number(s) of your choice(s), separated by commas: 1
Could not create the pivot table: Grouper for 'order_number' not 1-dimensional

# Here is a custom pivot table that worked, using sales_region, quantity, unit_price, sum and mean:
Select rows (required): 5
Select columns (optional, Enter to skip):
Select values to aggregate: 3,4
Select aggregation function: 1,2

Custom pivot table:
                    sum                mean
               quantity unit_price quantity unit_price
sales_region
Central East       2307   60290.25     3.31      86.50
N Central East     2731   67495.65     3.28      81.12
N Central West      176    4744.76     2.51      67.78
Northeast          1936   52869.29     3.21      87.53
Northwest           748   18947.12     3.25      82.38
S Central East     3107   81948.44     3.30      87.09
S Central West      979   28926.61     2.96      87.39
Southeast          2244   56107.04     3.23      80.85
Southwest          2295   58663.06     3.14      80.25

# I selected each sales analysis from the menu:
Select an option (1-10): 2

Total sales by region and order type:
order_type         Retail  Wholesale
sales_region                        
Central East    102613.51  149137.89
N Central East  117451.69  152446.42
N Central West   10006.42    1731.50
Northeast        84078.95  127423.36
Northwest        34565.62   33240.12
S Central East  130742.32  208945.73
S Central West   54681.80   51051.03
Southeast        96310.12  127554.60
Southwest       104743.52  121977.20
Would you like to export to Excel? (y/n): n
Export skipped.
Select an option (1-10): 3

Average sales by region, state, and order type:
customer_state Alabama           Alaska            ...           Wisconsin           Wyoming
order_type      Retail Wholesale Retail Wholesale  ... Wholesale    Retail Wholesale  Retail
sales_region                                       ...                                      
Central East      0.00      0.00    0.0      0.00  ...   1771.71      0.00      0.00    0.00
N Central East    0.00      0.00    0.0      0.00  ...      0.00    167.19   1412.21    0.00
N Central West    0.00      0.00    0.0      0.00  ...      0.00      0.00      0.00   36.74
Northeast         0.00      0.00    0.0      0.00  ...      0.00      0.00      0.00    0.00
Northwest         0.00      0.00  153.0    799.83  ...      0.00      0.00      0.00    0.00
S Central East    0.00      0.00    0.0      0.00  ...      0.00      0.00      0.00    0.00
S Central West    0.00      0.00    0.0      0.00  ...      0.00      0.00      0.00    0.00
Southeast       143.72    762.73    0.0      0.00  ...      0.00      0.00      0.00    0.00
Southwest         0.00      0.00    0.0      0.00  ...      0.00      0.00      0.00    0.00

[9 rows x 88 columns]
Would you like to export to Excel? (y/n): n
Export skipped.
Select an option (1-10): 4

Sales by customer type and order type by state:
                                            sales
customer_state customer_type order_type          
Alabama        Business      Retail       1088.00
                             Wholesale    8389.99
               Individual    Retail      14434.00
Alaska         Business      Retail        886.00
                             Wholesale    2399.50
...                                           ...
West Virginia  Business      Wholesale   12402.00
               Individual    Retail       5410.47
Wisconsin      Business      Wholesale   22595.43
               Individual    Retail       7356.31
Wyoming        Individual    Retail         73.47

[114 rows x 1 columns]
Would you like to export to Excel? (y/n): n
Export skipped.
Select an option (1-10): 5

Total sales quantity and price by region and product:
                                                 quantity     sales
sales_region produce_name                                          
Central East Assorted Olive Bar Soap - 6 pk            17    510.00
             Assorted Olive Oil Bar Soap - 3 pk        20    290.00
             Basil EVOO Gift Basket                    28   2100.00
             Basil Extra Virgin Olive Oil              23    598.00
             Basil Extra Virgin Olive Oil 12pk        120  28080.00
...                                                   ...       ...
Southwest    Vanilla and Olive Oil Bar Soap            22    131.78
             Vanilla and Olive Oil Bar Soap 3pk        20    290.00
             Vanilla and Olive Oil Body Soap           28    208.60
             Vanilla and Olive Oil Candle              47    328.53
             Vanilla and Olive Oil Lotion              24    239.76

[576 rows x 2 columns]
Would you like to export to Excel? (y/n): n
Export skipped.
Select an option (1-10): 6

Total sales quantity and price by customer type:
                          quantity      sales
order_type customer_type                     
Retail     Business            375   28574.37
           Individual        10641  706619.58
Wholesale  Business           5507  973507.85
Would you like to export to Excel? (y/n): n
Export skipped.
Select an option (1-10): 7

Max and min sales price by category:
                     max    min
                   sales  sales
product_category               
Bath products      300.0   5.99
Gift Basket       1150.0  19.50
Olive Oil         3276.0  16.75
Would you like to export to Excel? (y/n): n
Export skipped.
Select an option (1-10): 8

Number of unique employees by region:
                employee_id
sales_region               
Central East              6
N Central East            6
N Central West            1
Northeast                 4
Northwest                 4
S Central East            6
S Central West            5
Southeast                 6
Southwest                 6
Would you like to export to Excel? (y/n): n
Export skipped.

# I tested exporting and not exporting Excel files:
Would you like to export to Excel? (y/n): y
Enter Excel filename: sales_by_region.xlsx
File exported successfully: sales_by_region.xlsx

Would you like to export to Excel? (y/n): n
Export skipped.

# I also tested invalid export inputs:
Would you like to export to Excel? (y/n): abc
Invalid input. Please enter y or n.
Would you like to export to Excel? (y/n): n
Export skipped.

Would you like to export to Excel? (y/n): y
Enter Excel filename: 
Filename cannot be empty.

# I tested a missing CSV file:
Select a dataset:
1. sales_data.csv
2. sales_data_test.csv
Enter your choice (1-2): 1
Loading CSV file from: 10missing_file.csv
Error reading the CSV file: [Errno 2] No such file or directory: '10missing_file.csv'

# I tested a missing employee_id column:
- I temporarily removed the employee_id column from the DataFrame to test how the program handles missing columns.
Enter your choice (1-2): 1
Loading CSV file from: sales_data.csv
All required columns are available.
CSV file loaded successfully in 0.02 seconds.
Number of rows: 5130
Available columns:
['order_number', 'employee_id', 'employee_name', 'job_title', 'sales_region', 'order_date', 'order_type', 'customer_type', 'customer_name', 'customer_state', 'product_category', 'product_number', 'produce_name', 'quantity', 'unit_price']
Cannot perform this analysis. Missing columns: ['employee_id']

Sales Data Menu

# I tested exit:
Sales Data Menu
  1. Show the first n rows of sales data
  2. Total sales by region and order_type
  3. Average sales by region with average sales by state and sale type
  4. Sales by customer type and order type by state
  5. Total sales quantity and price by region and product
  6. Total sales quantity and price by customer type
  7. Max and min sales price by category
  8. Number of unique employees by region
  9. Create a custom pivot table
  10. Exit
Select an option (1-10): 10
Exiting the program. Goodbye!

# 
I also tested the custom pivot table using sales_region as rows, order_type as columns, quantity as values, and sum as the function. The program displayed the results correctly. 
Sales Data Menu
  1. Show the first n rows of sales data
  2. Total sales by region and order_type
  3. Average sales by region with average sales by state and sale type
  4. Sales by customer type and order type by state
  5. Total sales quantity and price by region and product
  6. Total sales quantity and price by customer type
  7. Max and min sales price by category
  8. Number of unique employees by region
  9. Create a custom pivot table
  10. Exit
Select an option (1-10): 9

Select rows (required):
1. order_number
2. employee_id
3. employee_name
4. job_title
5. sales_region
6. order_date
7. order_type
8. customer_type
9. customer_name
10. customer_state
11. product_category
12. product_number
13. produce_name
14. quantity
15. unit_price
Enter the number(s) of your choice(s), separated by commas: 5

Select columns (optional, Enter to skip):
1. order_number
2. employee_id
3. employee_name
4. job_title
5. order_date
6. order_type
7. customer_type
8. customer_name
9. customer_state
10. product_category
11. product_number
12. produce_name
13. quantity
14. unit_price
Enter the number(s) of your choice(s), separated by commas: 6

Select values to aggregate:
1. order_number
2. employee_id
3. quantity
4. unit_price
Enter the number(s) of your choice(s), separated by commas: 3

Select aggregation function:
1. sum
2. mean
3. count
Enter the number(s) of your choice(s), separated by commas: 1

Custom pivot table:
                    sum          
               quantity          
order_type       Retail Wholesale
sales_region                     
Central East       1475       832
N Central East     1805       926
N Central West      158        18
Northeast          1263       673
Northwest           508       240
S Central East     1990      1117
S Central West      701       278
Southeast          1510       734
Southwest          1606       689
Would you like to export to Excel? (y/n): n
Export skipped.


# I tested the custom pivot table with two values (quantity and unit_price) and two functions (sum and mean). The program displayed all four results.

Sales Data Menu
  1. Show the first n rows of sales data
  2. Total sales by region and order_type
  3. Average sales by region with average sales by state and sale type
  4. Sales by customer type and order type by state
  5. Total sales quantity and price by region and product
  6. Total sales quantity and price by customer type
  7. Max and min sales price by category
  8. Number of unique employees by region
  9. Create a custom pivot table
  10. Exit
Select an option (1-10): 9

Select rows (required):
1. order_number
2. employee_id
3. employee_name
4. job_title
5. sales_region
6. order_date
7. order_type
8. customer_type
9. customer_name
10. customer_state
11. product_category
12. product_number
13. produce_name
14. quantity
15. unit_price
Enter the number(s) of your choice(s), separated by commas: 5

Select columns (optional, Enter to skip):
1. order_number
2. employee_id
3. employee_name
4. job_title
5. order_date
6. order_type
7. customer_type
8. customer_name
9. customer_state
10. product_category
11. product_number
12. produce_name
13. quantity
14. unit_price
Enter the number(s) of your choice(s), separated by commas: 

Select values to aggregate:
1. order_number
2. employee_id
3. quantity
4. unit_price
Enter the number(s) of your choice(s), separated by commas: 3,4

Select aggregation function:
1. sum
2. mean
3. count
Enter the number(s) of your choice(s), separated by commas: 1,2

Custom pivot table:
                    sum                mean           
               quantity unit_price quantity unit_price
sales_region                                          
Central East       2307   60290.25     3.31      86.50
N Central East     2731   67495.65     3.28      81.12
N Central West      176    4744.76     2.51      67.78
Northeast          1936   52869.29     3.21      87.53
Northwest           748   18947.12     3.25      82.38
S Central East     3107   81948.44     3.30      87.09
S Central West      979   28926.61     2.96      87.39
Southeast          2244   56107.04     3.23      80.85
Southwest          2295   58663.06     3.14      80.25

# I tested the count function in the custom pivot table. It showed the number of records for each sales region, and the total was 5,130.
Sales Data Menu
  1. Show the first n rows of sales data
  2. Total sales by region and order_type
  3. Average sales by region with average sales by state and sale type
  4. Sales by customer type and order type by state
  5. Total sales quantity and price by region and product
  6. Total sales quantity and price by customer type
  7. Max and min sales price by category
  8. Number of unique employees by region
  9. Create a custom pivot table
  10. Exit
Select an option (1-10): 9

Select rows (required):
1. order_number
2. employee_id
3. employee_name
4. job_title
5. sales_region
6. order_date
7. order_type
8. customer_type
9. customer_name
10. customer_state
11. product_category
12. product_number
13. produce_name
14. quantity
15. unit_price
Enter the number(s) of your choice(s), separated by commas: 5

Select columns (optional, Enter to skip):
1. order_number
2. employee_id
3. employee_name
4. job_title
5. order_date
6. order_type
7. customer_type
8. customer_name
9. customer_state
10. product_category
11. product_number
12. produce_name
13. quantity
14. unit_price
Enter the number(s) of your choice(s), separated by commas: 

Select values to aggregate:
1. order_number
2. employee_id
3. quantity
4. unit_price
Enter the number(s) of your choice(s), separated by commas: 3

Select aggregation function:
1. sum
2. mean
3. count
Enter the number(s) of your choice(s), separated by commas: 3

Custom pivot table:
                  count
               quantity
sales_region           
Central East        697
N Central East      832
N Central West       70
Northeast           604
Northwest           230
S Central East      941
S Central West      331
Southeast           694
Southwest           731


# I tested the "all" option using the 10-row test dataset. The program displayed all 10 rows correctly. I also tested "n" to skip exporting to Excel. 
Select a dataset:
1. sales_data.csv
2. sales_data_test.csv
Enter your choice (1-2): 2
Loading CSV file from: sales_data_test.csv
All required columns are available.
CSV file loaded successfully in 0.02 seconds.
Number of rows: 10
Available columns:
['order_number', 'employee_id', 'employee_name', 'job_title', 'sales_region', 'order_date', 'order_type', 'customer_type', 'customer_name', 'customer_state', 'product_category', 'product_number', 'produce_name', 'quantity', 'unit_price']

Sales Data Menu
  1. Show the first n rows of sales data
  2. Total sales by region and order_type
  3. Average sales by region with average sales by state and sale type
  4. Sales by customer type and order type by state
  5. Total sales quantity and price by region and product
  6. Total sales quantity and price by customer type
  7. Max and min sales price by category
  8. Number of unique employees by region
  9. Create a custom pivot table
  10. Exit
Select an option (1-10): 1

How many rows would you like to see? (1-10, 'all', or Enter to skip): all
 order_number  employee_id   employee_name              job_title   sales_region order_date order_type customer_type      customer_name customer_state product_category product_number                         produce_name  quantity  unit_price
      1102935    900019019 Alexandra Kundt Senior Sales Associate S Central East     9/2/19     Retail    Individual     Skipton Fealty       Arkansas        Olive Oil          OO206     Chili Extra Virgin Olive Oil 2pk         3       45.00
      1102976    900019019 Alexandra Kundt Senior Sales Associate S Central East 15/02/2019     Retail    Individual    Lanni D'Ambrogi       Missouri      Gift Basket          GB301 Scented Olive Oil Candle Gift Basket         1       19.50
      1102988    900019019 Alexandra Kundt Senior Sales Associate S Central East 16/02/2019     Retail    Individual            Far Pow    Mississippi        Olive Oil          OO302         Chili Extra Virgin Olive Oil         4       26.00
      1103012    900019019 Alexandra Kundt Senior Sales Associate S Central East 19/02/2019  Wholesale      Business          Swift Inc          Texas        Olive Oil          OO125   Garlic Extra Virgin Olive Oil 12pk         4      234.00
      1103031    900019019 Alexandra Kundt Senior Sales Associate S Central East 22/02/2019     Retail    Individual Carmine Priestnall          Texas        Olive Oil          OO128    Chili Extra Virgin Olive Oil 12pk         3      234.00
      1103106    900019019 Alexandra Kundt Senior Sales Associate S Central East     9/3/19     Retail    Individual        Tann Angear       Oklahoma    Bath products          BP502         Vanilla and Olive Oil Candle         2        6.99
      1103113    900019019 Alexandra Kundt Senior Sales Associate S Central East    11/3/19  Wholesale      Business        Hilll Group          Texas        Olive Oil          OO206     Chili Extra Virgin Olive Oil 2pk         5       45.00
      1103172    900019019 Alexandra Kundt Senior Sales Associate S Central East 18/03/2019     Retail    Individual        Devlin Nock          Texas        Olive Oil          OO204     Lemon Extra Virgin Olive Oil 2pk         4       45.00
      1103175    900019019 Alexandra Kundt Senior Sales Associate S Central East 19/03/2019     Retail    Individual  Jerrilyn Doubrava       Missouri        Olive Oil          OO307      Rosemary Extra Virgin Olive Oil         3       26.00
      1103240    900019019 Alexandra Kundt Senior Sales Associate S Central East 29/03/2019     Retail    Individual     Skipton Fealty       Arkansas        Olive Oil          OO207     Basil Extra Virgin Olive Oil 2pk         2       45.00
Would you like to export to Excel? (y/n): n
Export skipped.

Sales Data Menu
  1. Show the first n rows of sales data
  2. Total sales by region and order_type
  3. Average sales by region with average sales by state and sale type
  4. Sales by customer type and order type by state
  5. Total sales quantity and price by region and product
  6. Total sales quantity and price by customer type
  7. Max and min sales price by category
  8. Number of unique employees by region
  9. Create a custom pivot table
  10. Exit
Select an option (1-10): 