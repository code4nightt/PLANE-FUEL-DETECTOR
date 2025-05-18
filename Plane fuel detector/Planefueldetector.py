def check_fuel_safety(distance_km, fuel_efficiency, available_fuel):
  required_fuel = distance_km / fuel_efficiency
  print(f"\nRequired fuel: {required_fuel:.2f} liters")
  print(f"Available fuel: {available_fuel:.2f} liters")

  if available_fuel >= required_fuel:
      print("✅ Fuel check passed. Engine can start. Safe to fly!")
      return True
  else:
      print("❌ Insufficient fuel. Engine LOCKED. Flight aborted for safety.")
      return False

# Input (you can change these)
destination_km = float(input("Enter destination distance (km): "))
efficiency = float(input("Enter plane fuel efficiency (km per liter): "))
available = float(input("Enter available fuel (liters): "))

# Run the check
check_fuel_safety(destination_km, efficiency, available)
