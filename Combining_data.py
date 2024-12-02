import pandas as pd

# Load the two CSV files
file1 = 'telegram_channel_messages1.csv'  # Replace with your first file name
file2 = 'telegram_channel_messages.csv'  # Replace with your second file name

df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# Combine the two DataFrames
combined_df = pd.concat([df1, df2], ignore_index=True)


# Save the combined dataset to a new CSV file
combined_df.to_csv('combined_telegram_data.csv', index=False)
print("Combined dataset saved as 'combined_telegram_data.csv'")
