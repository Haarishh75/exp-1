# A simple Hot Wheels Garage Manager
garage = []

def add_car(name, year, series):
    car = {"Name": name, "Year": year, "Series": series}
    garage.append(car)
    print(f"Added {name} to your garage!")

def show_garage():
    print("\n--- My Hot Wheels Collection ---")
    for car in garage:
        print(f"[{car['Year']}] {car['Name']} - {car['Series']}")

# Program Execution
add_car("Twin Mill", 1969, "Original 16")
add_car("Bone Shaker", 2006, "First Editions")
show_garage()
