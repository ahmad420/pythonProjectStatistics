import pandas as pd
from tabulate import tabulate
import colorama

colorama.init()


def create_dummy_data():
    # Dummy data as a list of dictionaries
    data = [
        {
            "productID": "P001",
            "name": "Product 1",
            "description": "This is product 1",
            "category": "Category A",
            "manufacturer": "Manufacturer X",
            "price": 10.99,
            "quantity": 100,
            "unitOfMeasurement": "pcs"
        },
        {
            "productID": "P002",
            "name": "Product 2",
            "description": "This is product 2",
            "category": "Category B",
            "manufacturer": "Manufacturer Y",
            "price": 24.99,
            "quantity": 50,
            "unitOfMeasurement": "pcs"
        },
        {
            "productID": "P003",
            "name": "Product 3",
            "description": "This is product 3",
            "category": "Category A",
            "manufacturer": "Manufacturer Z",
            "price": 7.49,
            "quantity": 200,
            "unitOfMeasurement": "pcs"
        },
        {
            "productID": "P004",
            "name": "Product 4",
            "description": "This is product 4",
            "category": "Category C",
            "manufacturer": "Manufacturer X",
            "price": 14.95,
            "quantity": 75,
            "unitOfMeasurement": "pcs"
        },
        {
            "productID": "P005",
            "name": "Product 5",
            "description": "This is product 5",
            "category": "Category B",
            "manufacturer": "Manufacturer Z",
            "price": 19.99,
            "quantity": 120,
            "unitOfMeasurement": "pcs"
        }
    ]

    # Create DataFrame from the data
    df = pd.DataFrame(data)

    return df


def create_suppliers_data():
    # Dummy data for suppliers as a list of dictionaries
    suppliers_data = [
        {
            "supplierID": "S001",
            "name": "Supplier 1",
            "contactPerson": "John Doe",
            "email": "john.doe@supplier1.com",
            "phone": "+1234567890",
            "address": "123 Main Street, City A"
        },
        {
            "supplierID": "S002",
            "name": "Supplier 2",
            "contactPerson": "Jane Smith",
            "email": "jane.smith@supplier2.com",
            "phone": "+9876543210",
            "address": "456 Oak Avenue, City B"
        },
        {
            "supplierID": "S003",
            "name": "Supplier 3",
            "contactPerson": "Michael Johnson",
            "email": "michael.johnson@supplier3.com",
            "phone": "+4443332221",
            "address": "789 Elm Road, City C"
        }
    ]

    # Create DataFrame for suppliers
    suppliers_df = pd.DataFrame(suppliers_data)

    return suppliers_df


def create_warehouses_data():
    # Dummy data for warehouses as a list of dictionaries
    warehouses_data = [
        {
            "warehouseID": "W001",
            "name": "Warehouse 1",
            "location": "City A",
            "capacity": 1000,
            "manager": "John Smith"
        },
        {
            "warehouseID": "W002",
            "name": "Warehouse 2",
            "location": "City B",
            "capacity": 1500,
            "manager": "Jane Doe"
        },
        {
            "warehouseID": "W003",
            "name": "Warehouse 3",
            "location": "City C",
            "capacity": 800,
            "manager": "Michael Johnson"
        },
        {
            "warehouseID": "W004",
            "name": "Warehouse 4",
            "location": "City D",
            "capacity": 1200,
            "manager": "Emily Brown"
        },
        {
            "warehouseID": "W005",
            "name": "Warehouse 5",
            "location": "City E",
            "capacity": 2000,
            "manager": "Robert Green"
        }
    ]

    # Create DataFrame for warehouses
    warehouses_df = pd.DataFrame(warehouses_data)

    return warehouses_df


def create_stocks_data():
    # Dummy data for stocks as a list of dictionaries
    stocks_data = [
        {
            "stockID": "ST001",
            "productID": "P001",
            "warehouseID": "W001",
            "quantity": 100,
            "minStockLevel": 50,
            "reorderQuantity": 30
        },
        {
            "stockID": "ST002",
            "productID": "P002",
            "warehouseID": "W001",
            "quantity": 80,
            "minStockLevel": 40,
            "reorderQuantity": 20
        },
        {
            "stockID": "ST003",
            "productID": "P001",
            "warehouseID": "W002",
            "quantity": 120,
            "minStockLevel": 60,
            "reorderQuantity": 40
        },
        {
            "stockID": "ST004",
            "productID": "P003",
            "warehouseID": "W003",
            "quantity": 60,
            "minStockLevel": 30,
            "reorderQuantity": 25
        },
        {
            "stockID": "ST005",
            "productID": "P004",
            "warehouseID": "W003",
            "quantity": 150,
            "minStockLevel": 75,
            "reorderQuantity": 50
        }
    ]

    # Create DataFrame for stocks
    stocks_df = pd.DataFrame(stocks_data)

    return stocks_df


def create_shelves_data():
    # Dummy data for shelves as a list of dictionaries
    shelves_data = [
        {
            "shelfID": "SH001",
            "warehouseID": "W001",
            "capacity": 200,
            "currentCapacity": 100,
            "description": "Shelf 1 in Warehouse 1"
        },
        {
            "shelfID": "SH002",
            "warehouseID": "W001",
            "capacity": 150,
            "currentCapacity": 80,
            "description": "Shelf 2 in Warehouse 1"
        },
        {
            "shelfID": "SH003",
            "warehouseID": "W002",
            "capacity": 300,
            "currentCapacity": 200,
            "description": "Shelf 1 in Warehouse 2"
        },
        {
            "shelfID": "SH004",
            "warehouseID": "W002",
            "capacity": 250,
            "currentCapacity": 150,
            "description": "Shelf 2 in Warehouse 2"
        },
        {
            "shelfID": "SH005",
            "warehouseID": "W003",
            "capacity": 180,
            "currentCapacity": 120,
            "description": "Shelf 1 in Warehouse 3"
        }
    ]

    # Create DataFrame for shelves
    shelves_df = pd.DataFrame(shelves_data)

    return shelves_df


# Call the functions to create the DataFrames
dummy_table_df = create_dummy_data()
suppliers_table_df = create_suppliers_data()
warehouses_table_df = create_warehouses_data()
stocks_table_df = create_stocks_data()
shelves_table_df = create_shelves_data()


# Function to style the tables
def style_tables(df):
    # Apply custom styling to the DataFrame
    return df.style \
        .set_table_styles([{
        'selector': 'tr:hover',
        'props': [('background-color', 'lightyellow')]
    }, {
        'selector': 'thead th',
        'props': [('background-color', 'lightblue'), ('color', 'black'), ('font-weight', 'bold')]
    }, {
        'selector': 'th.index_name',
        'props': [('color', 'red')]
    }, {
        'selector': 'td',
        'props': [('text-align', 'center')]
    }])


# Call the functions to create the DataFrames
dummy_table_df = create_dummy_data()
suppliers_table_df = create_suppliers_data()
warehouses_table_df = create_warehouses_data()
stocks_table_df = create_stocks_data()
shelves_table_df = create_shelves_data()


# Function to format and style the DataFrame using tabulate
def style_tables(df):
    # Convert the DataFrame to a tabular format using tabulate
    tabular_data = tabulate(df, headers='keys', tablefmt='grid')

    return tabular_data


# Style and display each DataFrame with colors
def display_colored_table(dataframe):
    try:
        from colorama import init, Fore, Style
        init()  # Initialize colorama

        # Convert the DataFrame to a tabular format using tabulate with ANSI escape codes for colors
        tabular_data = tabulate(dataframe, headers='keys', tablefmt='grid')

        # Apply color to the tabular data
        colored_data = ''
        for line in tabular_data.split('\n'):
            if line.startswith('+'):  # Skip the horizontal lines
                colored_data += f"{Fore.CYAN}{line}{Style.RESET_ALL}\n"
            elif line.startswith('|'):
                colored_data += f"{Fore.BLUE}{line}{Style.RESET_ALL}\n"
            else:
                colored_data += f"{Fore.YELLOW}{line}{Style.RESET_ALL}\n"

        print(colored_data)

    except ImportError:
        # If colorama is not installed, display the table without colors
        print(style_tables(dataframe))


# Main menu function
def main_menu():
    print("===== Main Menu =====")
    print("1. Display Dummy Table")
    print("2. Display Suppliers Table")
    print("3. Display Warehouses Table")
    print("4. Display Stocks Table")
    print("5. Display Shelves Table")
    print("0. Exit")


# Main program loop
while True:
    main_menu()
    choice = input("Enter your choice (0-5): ")

    if choice == "1":
        print("\nStyled Dummy Table:")
        display_colored_table(dummy_table_df)
    elif choice == "2":
        print("\nStyled Suppliers Table:")
        display_colored_table(suppliers_table_df)
    elif choice == "3":
        print("\nStyled Warehouses Table:")
        display_colored_table(warehouses_table_df)
    elif choice == "4":
        print("\nStyled Stocks Table:")
        display_colored_table(stocks_table_df)
    elif choice == "5":
        print("\nStyled Shelves Table:")
        display_colored_table(shelves_table_df)
    elif choice == "0":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice! Please select a valid option (0-5).")
