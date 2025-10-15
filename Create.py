import pickle
import os
from py_compile import main

def create_laptop():
    print("\n==============================")
    print("   ADD NEW LAPTOP TO INVENTORY")
    print("==============================\n")
    
    def laptop_id_input():
        laptop_id = input("Enter laptop ID: ")
        # Max length + Not empty check
        if laptop_id=="" or len(laptop_id)>8:
            print("Laptop ID cannot be empty and must be less than 8 characters.")
            return laptop_id_input()
        return laptop_id

    def brand_input():
        brand = input("Enter brand: ")
        # Max length + Not empty check
        if brand=="" or len(brand)>20:
            print("Brand cannot be empty and must be less than 20 characters.")
            return brand_input()
        return brand

    def model_input():
        model = input("Enter model: ")
        # Max length + Not empty check
        if model=="" or len(model)>30:
            print("Model cannot be empty and must be less than 30 characters.")
            return model_input()
        return model

    def processor_input():
        processor = input("Enter processor: ")
        # Max length + Not empty check
        if processor=="" or len(processor)>30:
            print("Processor cannot be empty and must be less than 30 characters.")
            return processor_input()
        return processor

    def ram_input():
        try:
            ram_gb = int(input("Enter RAM size (GB): "))
            if ram_gb <= 0 or ram_gb > 999:
                print("RAM size must be a positive integer and less than 1000.")
                return ram_input()
            return ram_gb
        except ValueError:
            print("Invalid input! Please enter a whole number (e.g., 8, 16, 32).")
            return ram_input()
    

    def storage_input():
        try:
            storage_gb = int(input("Enter storage size (GB): "))
            if storage_gb <= 0 or storage_gb > 9999:
                print("Storage size must be a positive integer and less than 10000.")
                return storage_input()
            return storage_gb
        except ValueError:
            print("Invalid input! Please enter a whole number (e.g., 512, 1024, 2048).")
            return storage_input()

    def os_input():
        os_choice = input("Is this a MacOS laptop? (y/n): ").lower()
        is_macos = os_choice == 'y' or os_choice == 'yes'
        # Boolean Not Null Check
        if os_choice == "":
            print("Operating system choice cannot be empty.")
            return os_input()
        return is_macos

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
        "is_macos": is_macos,
        "ram_gb": ram_gb,
        "storage-size_gb": storage_gb
    }
    
    # Load existing data or create new structure
    pickle_path = 'inventory.pkl'
    if os.path.exists(pickle_path):
        with open(pickle_path, 'rb') as f:
            data = pickle.load(f)
    else:
        data = {"laptops": []}
    
    # Check if laptop ID already exists
    existing_ids = [laptop_item.get('id') for laptop_item in data["laptops"]]
    if laptop_id in existing_ids:
        print(f"\nError: A laptop with ID '{laptop_id}' already exists!")
        print("Please choose a different ID.\n")
    
    # Add the new laptop
    data["laptops"].append(laptop)
    with open(pickle_path, 'wb') as f:
        pickle.dump(data, f)
    print(f"\nLaptop '{brand} {model}' with ID '{laptop_id}' added successfully!")
    print("Operation completed.\n")

    return main()