import configparser
import pandas as pd
import pymongo as pymongo
from tabulate import tabulate
import colorama
import matplotlib.pyplot as plt
from termcolor import colored

colorama.init()

# Initialize the configparser object
config = configparser.ConfigParser()

# Load the configuration file
config.read('config.ini')

# Get the MongoDB URI from the configuration
DB_URI = config.get('Database', 'DB_URI')


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
def create_shelf_capacities_bar_chart(df):
    plt.figure(figsize=(10, 6))
    plt.bar(df['shelfID'], df['capacity'], color='purple', label='Shelf Capacity')
    plt.bar(df['shelfID'], df['currentCapacity'], color='orange', label='Current Capacity')
    plt.xlabel('Shelf ID')
    plt.ylabel('Capacity')
    plt.title('Shelf Capacity vs Current Capacity')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


# *************************
def insert_data_to_collection(uri, database_name, collection_name, data):
    """
    Inserts data into an existing collection in MongoDB.

    Parameters:
        uri (str): The MongoDB URI with the correct scheme (e.g., 'mongodb://').
        database_name (str): The name of the MongoDB database.
        collection_name (str): The name of the collection to which data will be added.
        data (dict or list): The data to be inserted. It can be a single document (dict)
                             or a list of documents (list of dicts).

    Returns:
        None
    """
    try:
        # Connect to the MongoDB database
        client = pymongo.MongoClient(uri)
        db = client[database_name]

        # Select the collection
        collection = db[collection_name]

        # Insert data into the collection
        if isinstance(data, list):
            # If data is a list, insert multiple documents
            collection.insert_many(data)
        elif isinstance(data, dict):
            # If data is a dictionary, insert a single document
            collection.insert_one(data)
        else:
            raise ValueError("Invalid data format. Data must be a dict or a list of dicts.")

        print("Data inserted successfully.")
    except Exception as e:
        print("Error inserting data:", e)
    finally:
        # Close the database connection
        client.close()


def get_collections(database_uri, database_name):
    # Connect to the MongoDB server
    client = pymongo.MongoClient(database_uri)

    # Access the specified database
    db = client[database_name]

    # Get a list of all collections in the database
    collection_names = db.list_collection_names()

    # Create a list to hold the collection objects
    collections_list = []

    # Iterate through each collection
    for collection_name in collection_names:
        # Access the collection
        collection = db[collection_name]

        # Fetch all documents from the collection and convert them to a list
        documents = list(collection.find())

        # Create an object to represent the collection and its documents
        collection_object = {
            'collection_name': collection_name,
            'documents': documents
        }

        # Add the collection object to the list
        collections_list.append(collection_object)

    # Close the MongoDB connection
    client.close()

    return collections_list


def display_collection_names(uri, client, database_name):
    client = pymongo.MongoClient(uri)
    if client:
        # Access the database
        db = client[database_name]

        # Get the collection names and display them
        collection_names = db.list_collection_names()

        return collection_names


def display_array_as_table(array, headers=None, tablefmt="fancy_grid"):
    if not array:
        print("No data to display.")
        return
    colored_items = [colored(str(item), "blue", attrs=["bold"]) for item in array]
    row_str = " | " + " | ".join(f"{i + 1}: \033[1;36m{str(item)}\033[0m" for i, item in enumerate(array))
    print(row_str)


def get_collection_documents(collections_arrays, collection_name):
    products_documents = None

    if collections_arrays:
        for collection in collections_arrays:
            if collection['collection_name'] == collection_name:
                products_documents = collection['documents']
                break
    else:
        print("somthing went wrong")

    return products_documents


def fetch_collections(database_uri, database_name, collection_names):
    client = pymongo.MongoClient(database_uri)
    db = client[database_name]

    collections = {}
    for collection_name in collection_names:
        collections[collection_name] = list(db[collection_name].find())

    client.close()
    return collections


# *************************
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
def main():
    uri = config.get('Database', 'DB_URI')
    database_name = "PYTHON-DB"
    name = "ahmdaf"

    collection_names = display_collection_names(uri, name, database_name)
    collections = fetch_collections(uri, database_name, collection_names)

    # Convert the collections to DataFrames
    dummy_table_df = pd.DataFrame(collections["products"])
    suppliers_table_df = pd.DataFrame(collections["suppliers"])
    warehouses_table_df = pd.DataFrame(collections["warehouses"])
    stocks_table_df = pd.DataFrame(collections["stocks"])
    shelves_table_df = pd.DataFrame(collections[" shelves"])
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
                    create_shelf_capacities_bar_chart(shelves_table_df)
                elif graph_choice == "0":
                    break
                else:
                    print("Invalid choice! Please select a valid option (0-9).")

        elif choice == "0":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice! Please select a valid option (0-6).")


if __name__ == "__main__":
    main()
