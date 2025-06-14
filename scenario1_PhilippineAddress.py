import random
from faker import Faker
import pandas as pd

fake = Faker()

# Sample Philippine cities and zip codes
city_postal = {
    'Quezon City': '1100',
    'Makati': '1226',
    'Cebu City': '6000',
    'Davao City': '8000',
    'Pasig': '1600',
    'Manila': '1000',
    'Taguig': '1630',
    'Baguio': '2600',
    'Iloilo City': '5000',
    'Cagayan de Oro': '9000',
}
cities = list(city_postal.keys())

# Province area mapping
city_province = {
    'Quezon City': 'Metro Manila',
    'Makati': 'Metro Manila',
    'Pasig': 'Metro Manila',
    'Cebu City': 'Visayas',
    'Davao City': 'Mindanao',
    'Manila': 'Metro Manila',
    'Taguig': 'Metro Manila',
    'Baguio': 'Luzon',
    'Iloilo City': 'Visayas',
    'Cagayan de Oro': 'Mindanao',
}

num_entries = 50
address_data = []

for i in range(1, num_entries + 1):
    house_number = random.randint(1, 999)
    street_name = fake.street_name()
    city = random.choice(cities)
    province = city_province[city]
    postal_code = city_postal[city]
    country = "Philippines"

    # Format full address in one line
    # Guidelines from Philippine Postal Corporation
    full_address = f"{house_number} {street_name} St., {city}, {province}, {postal_code}, {country}"

    address_data.append({
        'Address ID': i,
        'Full Address': full_address,
        'City': city,
        'Province/Area': province,
        'Postal Code': postal_code
    })

df = pd.DataFrame(address_data)
df.to_csv('dummy_addresses_with_province.csv', index=False)
