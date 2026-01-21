import pandas as pd

# Load funnel data
df = pd.read_csv("funnel_data.csv")

# Total users
total_users = len(df)

# Converted users
converted_users = df['Converted'].sum()

# Conversion rate
conversion_rate = (converted_users / total_users) * 100

print(f"Total Users: {total_users}")
print(f"Converted Users: {converted_users}")
print(f"Conversion Rate: {conversion_rate:.2f}%")

# Drop-off users
drop_off = total_users - converted_users
print(f"Drop-off Users: {drop_off}")
