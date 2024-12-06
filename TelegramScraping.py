import csv
from telethon import TelegramClient
import asyncio

# Replace with your own API ID and API Hash
api_id = '21371851'  # API ID from your configuration
api_hash = '2919605a4a10532744215edebefc5a46'  # API Hash from your configuration

# Create the Telegram client
client = TelegramClient('session_name', api_id, api_hash)

# Define the channel name and the CSV file name
channel_name = 'stockmarketupdates4'  # Replace with the actual channel name
csv_filename = 'telegram_channel_messages3.csv'

async def main():
    # Start the client
    await client.start()

    # Get the channel entity (channel or group name)
    entity = await client.get_entity(channel_name)

    # Open the CSV file for writing
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Message_ID', 'Sender_ID', 'Date', 'Message_Text'])  # Write the header
        
        # Get the messages from the channel
        async for message in client.iter_messages(entity):
            # Write each message's data into the CSV
            writer.writerow([message.id, message.sender_id, message.date, message.text])

    print(f"Messages from '{channel_name}' have been saved to {csv_filename}")

# Run the client
asyncio.run(main())
