# Input: Vehicle type and number of hours
vehicle_type = input("Enter the type of vehicle (c for car, b for bus, t for truck, y for cycle/bike): ").lower()
hours = int(input("Enter the number of hours parked: "))

# Calculate parking charges based on vehicle type
if vehicle_type == 'b' or vehicle_type == 't':
    charge_per_hour = 20
    total_charge = charge_per_hour * hours
    vehicle_name = "Bus/Truck"
    
elif vehicle_type == 'c':
    charge_per_hour = 10
    total_charge = charge_per_hour * hours
    vehicle_name = "Car"

elif vehicle_type == 'y':
    charge_per_hour = 5
    total_charge = charge_per_hour * hours
    vehicle_name = "Cycle/Bike"
    
else:
    print("Invalid vehicle type.")
    total_charge = None

# Output the total parking charge
if total_charge is not None:
    print(f"Vehicle: {vehicle_name}")
    print(f"Number of hours: {hours}")
    print(f"Parking charges: Rs. {total_charge}")
