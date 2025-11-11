import pickle

#import time

def display_inventory():
    with open('data/inventory.pkl', 'rb') as f:
        data = pickle.load(f)
    laptops = data.get('laptops', [])
    
    
    # Print header
    print(f"{'ID':<4} {'Brand':<10} {'Model':<25} {'Processor':<25} {'RAM':<10} {'Storage':<12} {'OS':<8}")
    print("-" * 100)
   
    # Print each laptop's details with a slight delay
    for laptop in laptops:
        print(
        f"{laptop.get('id',''):<4} "
        f"{laptop.get('brand',''):<10} "
        f"{laptop.get('model',''):<25} "
        f"{laptop.get('processor',''):<25} "
        f"{f'{laptop.get('ram_gb','')} GB' if laptop.get('ram_gb') else '':<10} "
        f"{f'{laptop.get('storage_gb','')} GB' if laptop.get('storage_gb') else '':<12} "
        f"{'MacOS' if laptop.get('is_macos', False) else 'Windows':<8}"
        )