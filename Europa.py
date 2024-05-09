# Europa.py - Script containing Europa's unique characteristics

# Define constants for Europa's characteristics (values are approximate)
radius_km = 1560  # Radius of Europa in kilometers
mass_kg = 4.8e22   # Mass of Europa in kilograms
surface_temperature_k = 102  # Average surface temperature of Europa in Kelvin
orbital_period_days = 3.55  # Orbital period of Europa around Jupiter in days
orbital_distance_km = 671100  # Semi-major axis of Europa's orbit around Jupiter in kilometers
surface_features = ["cracks", "ridges", "chaotic terrain"]  # Surface features on Europa

# Function to print Europa's characteristics
def print_europa_characteristics():
    print("Europa's Characteristics:")
    print(f"- Radius: {radius_km} km")
    print(f"- Mass: {mass_kg:.2e} kg")
    print(f"- Surface Temperature: {surface_temperature_k} K")
    print(f"- Orbital Period: {orbital_period_days} days")
    print(f"- Orbital Distance: {orbital_distance_km} km")
    print("- Surface Features:", ", ".join(surface_features))

# Main function to demonstrate usage
if __name__ == "__main__":
    print_europa_characteristics()
