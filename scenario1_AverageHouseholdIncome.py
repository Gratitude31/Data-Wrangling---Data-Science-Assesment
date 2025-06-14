import pandas as pd

# Define income data per city
income_data = {
    'Quezon City': 50000,
    'Makati': 80000,
    'Cebu City': 40000,
    'Davao City': 35000,
    'Pasig': 60000,
    'Manila': 70000,
    'Taguig': 75000,
    'Baguio': 30000,
    'Iloilo City': 32000,
    'Cagayan de Oro': 36000
}

df_income = pd.DataFrame(
    [{'City': city, 'Average Monthly Income (PHP)': income}
     for city, income in income_data.items()]
)

df_income.to_csv("average_household_income.csv", index=False)
