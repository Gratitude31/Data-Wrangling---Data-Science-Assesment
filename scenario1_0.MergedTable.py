import pandas as pd

df_address = pd.read_csv('dummy_addresses_with_province.csv')
df_income = pd.read_csv('average_household_income.csv')

df_address['City'] = df_address['Full Address'].apply(
    lambda x: x.split(',')[1].strip())

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

df_merged.to_csv('merged_address_income_data.csv', index=False)
