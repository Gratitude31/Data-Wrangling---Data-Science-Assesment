import random
from faker import Faker
import pandas as pd

fake = Faker()

# added notes only

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

formats = [
    "{house} {street}, {city} {postal} {province}",
    "{city}, {province}, {house} {street}, {postal}",
    "{house} {street} {postal} {city}",
    "{province} - {city} - {house} {street}",
    "{house} {street}, {postal}, {province}, {city}"
]

data = []

for i in range(50):
    city = random.choice(list(city_postal.keys()))
    postal = city_postal[city]
    province = city_province[city]
    street = fake.street_name()
    house = random.randint(1, 999)

    format_choice = random.choice(formats)
    address = format_choice.format(
        house=house,
        street=street,
        city=city,
        postal=postal,
        province=province
    )

    data.append({'Address ID': i + 1, 'Full Address': address})

df = pd.DataFrame(data)
df.to_csv("messy_dummy_addresses.csv", index=False)
