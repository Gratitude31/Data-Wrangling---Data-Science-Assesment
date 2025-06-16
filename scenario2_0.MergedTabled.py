import pandas as pd

df_address = pd.read_csv(
    r'C:\Users\Administrator\Documents\0. Data Science\Data Wrangling - Data Science Assesment\Scenario 1\Scenario 2\messy_dummy_addresses.csv')


valid_cities = [
    'Quezon City', 'Makati', 'Cebu City', 'Davao City',
    'Pasig', 'Manila', 'Taguig', 'Baguio', 'Iloilo City', 'Cagayan de Oro'
]


def extract_city(address):
    for city in valid_cities:
        if city in address:
            return city
    return None


df_address['City'] = df_address['Full Address'].apply(extract_city)

df_income = pd.read_csv(
    r'C:\Users\Administrator\Documents\0. Data Science\Data Wrangling - Data Science Assesment\Scenario 1\average_household_income.csv'
)

df_merged = pd.merge(df_address, df_income, on='City', how='left')


def categorize_income(income):
    if income < 35000:
        return 'Low'
    elif 35000 <= income < 60000:
        return 'Middle'
    else:
        return 'High'


df_merged['Income Category'] = df_merged['Average Monthly Income (PHP)'].apply(
    categorize_income)

df_merged.to_csv(
    r"C:\Users\Administrator\Documents\0. Data Science\Data Wrangling - Data Science Assesment\Scenario 1\Scenario 2\merged_address_income_data.csv",
    index=False
)
