import pandas as pd
from tabulate import tabulate
import colorama
import matplotlib.pyplot as plt

colorama.init()


def create_dummy_data():
    # Dummy data as a list of dictionaries
    data = [
        {
            "productID": "P001",
            "name": "Smartwatch",
            "description": "High-tech smartwatch with fitness tracking",
            "category": "Electronics",
            "manufacturer": "Brand A",
            "price": 159.99,
            "quantity": 50,
            "unitOfMeasurement": "pcs"
        },
        {
            "productID": "P002",
            "name": "Wireless Headphones",
            "description": "Premium wireless headphones with noise cancellation",
            "category": "Electronics",
            "manufacturer": "Brand B",
            "price": 249.99,
            "quantity": 100,
            "unitOfMeasurement": "pcs"
        },
        {
            "productID": "P003",
            "name": "Digital Camera",
            "description": "Professional-grade digital camera with 4K video recording",
            "category": "Electronics",
            "manufacturer": "Brand C",
            "price": 899.95,
            "quantity": 200,
            "unitOfMeasurement": "pcs"
        },
        {
            "productID": "P004",
            "name": "Gaming Laptop",
            "description": "Powerful gaming laptop with RGB lighting",
            "category": "Electronics",
            "manufacturer": "Brand D",
            "price": 1799.99,
            "quantity": 75,
            "unitOfMeasurement": "pcs"
        },
        {
            "productID": "P005",
            "name": "4K UHD TV",
            "description": "Large 4K UHD TV with smart features",
            "category": "Electronics",
            "manufacturer": "Brand E",
            "price": 999.99,
            "quantity": 120,
            "unitOfMeasurement": "pcs"
        },
        {
            "productID": "P006",
            "name": "Leather Handbag",
            "description": "Stylish leather handbag for women",
            "category": "Fashion",
            "manufacturer": "Brand F",
            "price": 149.50,
            "quantity": 80,
            "unitOfMeasurement": "pcs"
        },
        {
            "productID": "P007",
            "name": "Men's Dress Shoes",
            "description": "Elegant men's dress shoes for formal occasions",
            "category": "Fashion",
            "manufacturer": "Brand G",
            "price": 99.95,
            "quantity": 150,
            "unitOfMeasurement": "pcs"
        },
        {
            "productID": "P008",
            "name": "Designer Watch",
            "description": "Luxury designer watch with automatic movement",
            "category": "Fashion",
            "manufacturer": "Brand H",
            "price": 499.75,
            "quantity": 90,
            "unitOfMeasurement": "pcs"
        },
        {
            "productID": "P009",
            "name": "Women's Sneakers",
            "description": "Comfortable women's sneakers for casual wear",
            "category": "Fashion",
            "manufacturer": "Brand I",
            "price": 89.99,
            "quantity": 110,
            "unitOfMeasurement": "pcs"
        },
        {
            "productID": "P010",
            "name": "Denim Jeans",
            "description": "Classic denim jeans for men",
            "category": "Fashion",
            "manufacturer": "Brand J",
            "price": 59.50,
            "quantity": 70,
            "unitOfMeasurement": "pcs"
        },
        {
            "productID": "P011",
            "name": "Coffee Maker",
            "description": "Automatic coffee maker with built-in grinder",
            "category": "Home & Kitchen",
            "manufacturer": "Brand K",
            "price": 129.99,
            "quantity": 90,
            "unitOfMeasurement": "pcs"
        },
        {
            "productID": "P012",
            "name": "Air Fryer",
            "description": "Compact air fryer for healthy cooking",
            "category": "Home & Kitchen",
            "manufacturer": "Brand L",
            "price": 79.99,
            "quantity": 130,
            "unitOfMeasurement": "pcs"
        },
        {
            "productID": "P013",
            "name": "Robot Vacuum Cleaner",
            "description": "Smart robot vacuum cleaner with mapping technology",
            "category": "Home & Kitchen",
            "manufacturer": "Brand M",
            "price": 299.95,
            "quantity": 180,
            "unitOfMeasurement": "pcs"
        },
        {
            "productID": "P014",
            "name": "Memory Foam Pillow",
            "description": "Orthopedic memory foam pillow for better sleep",
            "category": "Home & Kitchen",
            "manufacturer": "Brand N",
            "price": 49.75,
            "quantity": 70,
            "unitOfMeasurement": "pcs"
        },
        {
            "productID": "P015",
            "name": "Essential Oil Diffuser",
            "description": "Aroma diffuser with LED lighting and timer",
            "category": "Home & Kitchen",
            "manufacturer": "Brand O",
            "price": 39.99,
            "quantity": 160,
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
            "name": "Central Warehouse",
            "location": "New York",
            "capacity": 5000,
            "manager": "John Smith",
            "staff_count": 12,
            "products": ["Electronics", "Home Appliances", "Toys"],
            "annual_revenue": 12000000,
            "is_owned": True
        },
        {
            "warehouseID": "W002",
            "name": "North Warehouse",
            "location": "Chicago",
            "capacity": 4000,
            "manager": "Jane Doe",
            "staff_count": 8,
            "products": ["Clothing", "Footwear", "Accessories"],
            "annual_revenue": 8000000,
            "is_owned": True
        },
        {
            "warehouseID": "W003",
            "name": "South Warehouse",
            "location": "Miami",
            "capacity": 3500,
            "manager": "Michael Johnson",
            "staff_count": 10,
            "products": ["Beauty", "Health", "Personal Care"],
            "annual_revenue": 6000000,
            "is_owned": True
        },
        {
            "warehouseID": "W004",
            "name": "East Warehouse",
            "location": "Atlanta",
            "capacity": 3000,
            "manager": "Emily Brown",
            "staff_count": 6,
            "products": ["Food", "Beverages", "Snacks"],
            "annual_revenue": 5000000,
            "is_owned": True
        },
        {
            "warehouseID": "W005",
            "name": "West Warehouse",
            "location": "Los Angeles",
            "capacity": 4500,
            "manager": "Robert Green",
            "staff_count": 14,
            "products": ["Furniture", "Home Decor", "Office Supplies"],
            "annual_revenue": 10000000,
            "is_owned": True
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
            "reorderQuantity": 30,
            "lastUpdated": "2023-07-24 10:15:00",
            "supplier": "ABC Suppliers",
            "unitPrice": 25.50
        },
        {
            "stockID": "ST002",
            "productID": "P002",
            "warehouseID": "W001",
            "quantity": 80,
            "minStockLevel": 40,
            "reorderQuantity": 20,
            "lastUpdated": "2023-07-24 09:30:00",
            "supplier": "XYZ Distributors",
            "unitPrice": 12.75
        },
        {
            "stockID": "ST003",
            "productID": "P001",
            "warehouseID": "W002",
            "quantity": 120,
            "minStockLevel": 60,
            "reorderQuantity": 40,
            "lastUpdated": "2023-07-24 11:45:00",
            "supplier": "LMN Traders",
            "unitPrice": 28.90
        },
        {
            "stockID": "ST004",
            "productID": "P003",
            "warehouseID": "W003",
            "quantity": 60,
            "minStockLevel": 30,
            "reorderQuantity": 25,
            "lastUpdated": "2023-07-24 12:30:00",
            "supplier": "DEF Wholesalers",
            "unitPrice": 19.99
        },
        {
            "stockID": "ST005",
            "productID": "P004",
            "warehouseID": "W003",
            "quantity": 150,
            "minStockLevel": 75,
            "reorderQuantity": 50,
            "lastUpdated": "2023-07-24 13:15:00",
            "supplier": "GHI Retailers",
            "unitPrice": 35.60
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
            "description": "Electronics Shelf in Warehouse 1, Section A"
        },
        {
            "shelfID": "SH002",
            "warehouseID": "W001",
            "capacity": 150,
            "currentCapacity": 80,
            "description": "Home Appliances Shelf in Warehouse 1, Section B"
        },
        {
            "shelfID": "SH003",
            "warehouseID": "W002",
            "capacity": 300,
            "currentCapacity": 200,
            "description": "Clothing Shelf in Warehouse 2, Section A"
        },
        {
            "shelfID": "SH004",
            "warehouseID": "W002",
            "capacity": 250,
            "currentCapacity": 150,
            "description": "Footwear Shelf in Warehouse 2, Section B"
        },
        {
            "shelfID": "SH005",
            "warehouseID": "W003",
            "capacity": 400,
            "currentCapacity": 120,
            "description": "Accessories Shelf in Warehouse 3, Section A"
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


def create_product_prices_bar_chart(df):
    plt.figure(figsize=(10, 6))
    plt.bar(df['name'], df['price'], color='skyblue')
    plt.xlabel('Product Name')
    plt.ylabel('Price ($)')
    plt.title('Product Prices')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


def create_product_prices_bar_chart(df):
    plt.figure(figsize=(10, 6))
    plt.bar(df['name'], df['price'], color='skyblue')
    plt.xlabel('Product Name')
    plt.ylabel('Price ($)')
    plt.title('Product Prices')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


# Function to create a line chart for product quantities
def create_product_quantities_line_chart(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df['name'], df['quantity'], marker='o', color='green', linestyle='-', linewidth=2)
    plt.xlabel('Product Name')
    plt.ylabel('Quantity')
    plt.title('Product Quantities')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


# Function to create a pie chart for product categories
def create_product_categories_pie_chart(df):
    plt.figure(figsize=(8, 8))
    plt.pie(df['category'].value_counts(), labels=df['category'].unique(), autopct='%1.1f%%', startangle=90,
            colors=['gold', 'lightcoral', 'lightskyblue', 'lightgreen'])
    plt.title('Product Categories')
    plt.axis('equal')
    plt.tight_layout()
    plt.show()


# Function to create a bar chart for supplier contact persons
def create_supplier_contact_persons_bar_chart(df):
    plt.figure(figsize=(10, 6))
    plt.bar(df['name'], df['contactPerson'], color='orange')
    plt.xlabel('Supplier Name')
    plt.ylabel('Contact Person')
    plt.title('Supplier Contact Persons')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


# Function to create a bar chart for warehouse capacities
def create_warehouse_capacities_bar_chart(df):
    plt.figure(figsize=(10, 6))
    plt.bar(df['name'], df['capacity'], color='purple')
    plt.xlabel('Warehouse Name')
    plt.ylabel('Capacity')
    plt.title('Warehouse Capacities')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


# Function to create a pie chart for warehouse locations
def create_warehouse_locations_pie_chart(df):
    plt.figure(figsize=(8, 8))
    plt.pie(df['location'].value_counts(), labels=df['location'].unique(), autopct='%1.1f%%', startangle=90,
            colors=['gold', 'lightcoral', 'lightskyblue', 'lightgreen', 'lightpink'])
    plt.title('Warehouse Locations')
    plt.axis('equal')
    plt.tight_layout()
    plt.show()


# Function to create a bar chart for stock quantities
def create_stock_quantities_bar_chart(df):
    plt.figure(figsize=(10, 6))
    plt.bar(df['productID'], df['quantity'], color='teal')
    plt.xlabel('Product ID')
    plt.ylabel('Quantity')
    plt.title('Stock Quantities')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


# Function to create a line chart for shelf capacities
def create_shelf_capacities_line_chart(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df['shelfID'], df['capacity'], marker='o', color='red', linestyle='-', linewidth=2)
    plt.xlabel('Shelf ID')
    plt.ylabel('Capacity')
    plt.title('Shelf Capacities')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


# Function to create a pie chart for shelf descriptions
def create_shelf_descriptions_pie_chart(df):
    plt.figure(figsize=(8, 8))
    plt.pie(df['description'].value_counts(), labels=df['description'].unique(), autopct='%1.1f%%', startangle=90,
            colors=['gold', 'lightcoral', 'lightskyblue', 'lightgreen', 'lightpink'])
    plt.title('Shelf Descriptions')
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

    # Main graph menu
def graph_menu():
        print("\nGraphs Menu:")
        print("1. Product Prices Bar Chart")
        print("2. Product Quantities Line Chart")
        print("3. Product Categories Pie Chart")
        print("4. Supplier Contact Persons Bar Chart")
        print("5. Warehouse Capacities Bar Chart")
        print("6. Warehouse Locations Pie Chart")
        print("7. Stock Quantities Bar Chart")
        print("8. Shelf Capacities Line Chart")
        print("9. Shelf Descriptions Pie Chart")
        print("0. Back to Main Menu")


# Main menu function
def main_menu():
    print("===== Main Menu =====")
    print("1. Display Dummy Table")
    print("2. Display Suppliers Table")
    print("3. Display Warehouses Table")
    print("4. Display Stocks Table")
    print("5. Display Shelves Table")
    print("6. Display graphs menu Table")
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
    elif choice == "6":
        # Go to the graphs menu
        while True:
            graph_menu()
            graph_choice = input("Enter your choice (0-9): ")

            if graph_choice == "1":
                create_product_prices_bar_chart(dummy_table_df)
            elif graph_choice == "2":
                create_product_quantities_line_chart(dummy_table_df)
            elif graph_choice == "3":
                create_product_categories_pie_chart(dummy_table_df)
            elif graph_choice == "4":
                create_supplier_contact_persons_bar_chart(suppliers_table_df)
            elif graph_choice == "5":
                create_warehouse_capacities_bar_chart(warehouses_table_df)
            elif graph_choice == "6":
                create_warehouse_locations_pie_chart(warehouses_table_df)
            elif graph_choice == "7":
                create_stock_quantities_bar_chart(stocks_table_df)
            elif graph_choice == "8":
                create_shelf_capacities_line_chart(shelves_table_df)
            elif graph_choice == "9":
                create_shelf_descriptions_pie_chart(shelves_table_df)
            elif graph_choice == "0":
                break
            else:
                print("Invalid choice! Please select a valid option (0-9).")

    elif choice == "0":
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice! Please select a valid option (0-6).")