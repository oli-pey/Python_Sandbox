import pickle
import os

def create_laptop():

    print("\n==============================")
    print("   ADD NEW LAPTOP TO INVENTORY")
    print("==============================\n")
    
    
    pickle_path = 'data/inventory.pkl'

    # Load existing data or create new structure
    if os.path.exists(pickle_path):
        with open(pickle_path, 'rb') as f:
            data = pickle.load(f)
    else:
        data = {"laptops": []}
    
    #Read out all Laptop IDS since these are unique and cannot be duplicate values
    existing_ids = [laptop_item.get('id') for laptop_item in data["laptops"]]
    
    
    
    def laptop_id_input():
        while True:
            laptop_id = input("Enter laptop ID: ")
            if not laptop_id:
                print("Laptop ID cannot be empty.")
            elif not laptop_id.isdigit():
                print("Laptop ID must be numeric.")
            elif len(laptop_id) != 4:
                print("Laptop ID must be exactly 4 digits.")
            elif laptop_id in existing_ids:
                print(f"Laptop ID '{laptop_id}' already exists. Please choose another.")
            else:
                return laptop_id


        
    def brand_input():
        allowed_brands = ["Dell", "HP", "Lenovo", "Asus", "Acer", "Apple"]
        while True:
            brand = input("Enter a laptop manufacturer: ").strip().capitalize()
            if not brand:
                print("Brand cannot be empty.")
            elif brand not in allowed_brands:
                print(f"Invalid brand. Allowed brands: {', '.join(allowed_brands)}")
            else:
                return brand


    def model_input():
        while True:
            model = input("Enter the model of the laptop: ").strip()
            if not model:
                print("Model cannot be empty.")
            elif len(model) > 25:
                print("Length of model is too long (max 25 characters).")
            else:
                return model

    
    def processor_input():
        valid_processors = [
        "Intel Core i3", "Intel Core i5", "Intel Core i7", "Intel Core i9",
        "AMD Ryzen 3", "AMD Ryzen 5", "AMD Ryzen 7", "AMD Ryzen 9",
        "Apple M1", "Apple M2", "Apple M3"
    ]
        while True:
            print(f"Heres a list of Processors {', '.join(valid_processors)}")
            processor = input("Enter processor: " ).strip()
            if processor in valid_processors:
                return processor
            else:
                print(f"Invalid processor. Choose from: {', '.join(valid_processors)}")



    def ram_input():
        while True:
            try:
                ram_gb = int(input("Enter RAM in GB: "))
                if ram_gb < 8 or ram_gb > 256:
                    print("RAM must be between 8GB and 256GB.")
                elif ram_gb % 8 != 0:
                    print("RAM must be a multiple of 8GB.")
                else:
                    return ram_gb
            except ValueError:
                print("Please enter a numeric value.")


        
    def storage_input():
        while True:
            try:
                storage_gb = int(input("Enter storage in GB: "))
                if storage_gb < 256 or storage_gb > 2048:
                    print("Storage must be between 256GB and 2048GB.")
                elif storage_gb % 256 != 0:
                    print("Storage must be a multiple of 256GB.")
                else:
                    return storage_gb
            except ValueError:
                print("Please enter a numeric value.")
    
    def os_input():
        while True:
            os_name = input("Enter OS (Windows/macOS): ").strip().lower()
            if os_name == "macos":
                return 1
            elif os_name == "windows":
                return 0
            else:
                print("Invalid input. Enter 'Windows' or 'macOS'.")
        

    # Create laptop dictionary
    laptop_id = laptop_id_input()
    brand = brand_input()
    model = model_input()
    processor = processor_input()
    ram_gb = ram_input()
    storage_gb = storage_input()
    is_macos = os_input()

    laptop = {
        "id": laptop_id,
        "brand": brand,
        "model": model,
        "processor": processor,
        "ram_gb": ram_gb,
        "storage_gb": storage_gb,
        "is_macos": is_macos,
    }
    
    
    # Add the new laptop
    data["laptops"].append(laptop)
    with open(pickle_path, 'wb') as f:
        pickle.dump(data, f)
    print(f"\nLaptop '{brand} {model}' with ID '{laptop_id}' added successfully!")
    print("Operation completed.\n")

     