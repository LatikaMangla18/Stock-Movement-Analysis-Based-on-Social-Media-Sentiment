import pandas as pd

# Load the two CSV files
file1 = 'telegram_channel_messages1.csv'  
file2 = 'telegram_channel_messages.csv'  
file3 = 'telegram_channel_messages2.csv'
file4 = 'telegram_channel_messages3.csv'

df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)
df3 = pd.read_csv(file3)
df4 = pd.read_csv(file4)

# Combine the two DataFrames
combined_df = pd.concat([df1, df2, df3, df4], ignore_index=True)
combined_df = pd.concat([df1, df2, df3, df4], ignore_index=True)


# Save the combined dataset to a new CSV file
combined_df.to_csv('combined_telegram_data.csv', index=False)
print("Combined dataset saved as 'combined_telegram_data.csv'")
