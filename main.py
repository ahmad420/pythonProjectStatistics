import configparser  # For read and write configuration files in INI format.
import multiprocessing  # For managing multiple processes
import pandas as pd  # For data manipulation and analysis
import pymongo as pymongo  # For interacting with MongoDB database.
from tabulate import tabulate  # For formatting tabular data.
import matplotlib.pyplot as plt  # For creating plots and charts.
import sys  # For system-specific functions and variables.
import time  # For time-related functions.
from tqdm import tqdm  # For creating progress bars in loops.
from colorama import Fore, Style

# Initialize the configparser object
config = configparser.ConfigParser()

# Load the configuration file
config.read('config.ini')

# Get the MongoDB URI from the configuration
DB_URI = config.get('Database', 'DB_URI')


# *************************
# MongoDB Data Handling Functions
# *************************
def get_collection_by_name(uri, collection_name, database_name):
    client = None
    try:
        client = pymongo.MongoClient(uri)
        database = client[database_name]
        collection = database[collection_name]

        # Get the total number of documents in the collection
        total_documents = collection.count_documents({})

        # Initialize tqdm with the total number of documents for the loading bar
        with tqdm(total=total_documents, desc="Loading collection data",
                  bar_format="{desc}: {percentage:.1f}%|{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining},"
                             " {rate_fmt}{postfix}]",
                  ncols=100, colour='green') as pbar:
            result = list(collection.find({}))
            pbar.update(len(result))

        return result
    except pymongo.errors.ConnectionFailure as e:
        raise e
    finally:
        client.close()


def insert_data_to_collection(uri, database_name, collection_name, data):
    client = None

    loading_duration = 5  # duration of the loading animation as needed
    loading_interval = 0.1  # interval between each frame update as needed

    # Start the loading animation process
    loading_process = multiprocessing.Process(target=loading, args=(loading_duration, loading_interval))
    loading_process.start()

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
        # Ensure that the loading animation process is terminated and joined, even if an exception occurs
        loading_process.terminate()
        loading_process.join()
        client.close()


def display_collection_names(uri, database_name):
    client = None

    loading_duration = 5  # Adjust the duration of the loading animation as needed
    loading_interval = 0.1  # Adjust the interval between each frame update as needed

    # Start the loading animation process
    loading_process = multiprocessing.Process(target=loading, args=(loading_duration, loading_interval))
    loading_process.start()

    try:
        client = pymongo.MongoClient(uri)
        if client:
            # Access the database
            db = client[database_name]

            # Get the collection names and display them
            collection_names = db.list_collection_names()

            return collection_names

    finally:
        # Ensure that the loading animation process is terminated and joined, even if an exception occurs
        loading_process.terminate()
        loading_process.join()
        client.close()


def get_collection_documents(collections_arrays, collection_name):
    products_documents = None

    if collections_arrays:
        for collection in collections_arrays:
            if collection['collection_name'] == collection_name:
                products_documents = collection['documents']
                break
    else:
        print_red("somthing went wrong")

    return products_documents


def fetch_collections(database_uri, database_name, collection_names):
    client = None
    loading_duration = 5  # Adjust the duration of the loading animation as needed
    loading_interval = 0.1  # Adjust the interval between each frame update as needed

    # Start the loading animation process
    loading_process = multiprocessing.Process(target=loading, args=(loading_duration, loading_interval))
    loading_process.start()

    try:
        client = pymongo.MongoClient(database_uri)
        db = client[database_name]

        collections = {}
        for collection_name in collection_names:
            collections[collection_name] = list(db[collection_name].find())
        print("\n")
        return collections

    finally:
        # Ensure that the loading animation process is terminated and joined, even if an exception occurs
        loading_process.terminate()
        loading_process.join()
        client.close()


def get_documents_by_collection(collections_dict, collection_name):
    for key, value in collections_dict.items():
        if key == collection_name:
            return value

    return None


def loading(duration=5, interval=0.1):
    frames = ['-', '\\', '|', '/']  # Animation frames
    total_frames = len(frames)
    num_frames = int(duration / interval)

    for i in range(num_frames):
        frame = frames[i % total_frames]
        sys.stdout.write(f'\rLoading data ... {frame}')
        sys.stdout.flush()
        time.sleep(interval)

    sys.stdout.write('\rLoading... Done!\n')
    sys.stdout.flush()


# *************************


# Function to format and style the DataFrame using tabulate
def display_array_as_table(array):
    if not array:
        print("No data to display.")
        return
    row_str = " | " + " | ".join(f"{i + 1}: \033[1;36m{str(item)}\033[0m" for i, item in enumerate(array))
    print(row_str)


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
        print(dataframe)


# Function to create a bar chart for product prices
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


def print_red(text):
    print(Fore.RED + text + Style.RESET_ALL)


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
    print("9. Shelf Descriptions bars Chart")
    print("0. Back to Main Menu")


# Main menu function
def main_menu():
    print("===== Main Menu =====")
    print("1. Display collections names")
    print("2. Display products Table by number")
    print("3. Display graphs menu Table")
    print("4. add items to DB(for testing )")
    print("5. refresh data (fetch from DB)")
    print("6. Exit")


def main():
    # get the database info from config file
    uri = config.get('Database', 'DB_URI')
    database_name = config.get('Database', 'DB_NAME')

    # try to fetch collection names and then try to fetch collections
    collection_names = display_collection_names(uri, database_name)
    collections = fetch_collections(uri, database_name, collection_names)

    # Create an empty dictionary to store the DataFrames
    data_frames = {}

    # Loop through each collection name and create the DataFrame
    for collection_name in collection_names:
        data_frames[collection_name] = pd.DataFrame(collections[collection_name])

    # Now, you can access the DataFrames dynamically using their collection names
    products_table_df = data_frames["products"]
    suppliers_table_df = data_frames["suppliers"]
    warehouses_table_df = data_frames["warehouses"]
    stocks_table_df = data_frames["stocks"]
    shelves_table_df = data_frames[" shelves"]

    while True:
        main_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            if collection_names:
                display_array_as_table(collection_names)
            else:
                print_red("Something went wrong with fetching collection names.")
        elif choice == "2":
            while True:
                print("\nStyled collections Tables:")
                if collection_names:
                    display_array_as_table(collection_names)
                    selected_index = int(input("Enter the number of the collection to view  the table and 0 to exit: "))
                    if selected_index == 0:
                        break
                    elif 1 <= selected_index <= len(collection_names):
                        collection_name = collection_names[selected_index - 1]
                        data = get_documents_by_collection(collections, collection_name)
                        display_colored_table(data)
                    else:
                        print_red("Invalid selection. Please try again.")
                else:
                    print_red("Something went wrong with fetching collection names.")
        elif choice == "3":
            # Go to the graphs menu
            while True:
                graph_menu()
                graph_choice = input("Enter your choice (0-9): ")

                if graph_choice == "1":
                    create_product_prices_bar_chart(products_table_df)
                elif graph_choice == "2":
                    create_product_quantities_line_chart(products_table_df)
                elif graph_choice == "3":
                    create_product_categories_pie_chart(products_table_df)
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
                    print_red("Invalid choice! Please select a valid option (0-9).")

        elif choice == "4":
            print("adding dummy items to DB ..")
            data = [
                {
                    "productID": "T004",
                    "name": "Product 2",
                    "description": "This is product 2",
                    "category": "Category B",
                    "manufacturer": "Manufacturer X",
                    "price": 10.99,
                    "quantity": 100,
                    "unitOfMeasurement": "pcs"
                }]
            insert_data_to_collection(uri, database_name, "products", data)

        elif choice == "5":
            print("fetching data from mongodb server .. ")
            collection_names = display_collection_names(uri, database_name)
            collections = fetch_collections(uri, database_name, collection_names)

        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print_red("Invalid choice! Please select a valid option (1-6).")


if __name__ == "__main__":
    main()
