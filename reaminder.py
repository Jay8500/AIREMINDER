import requests
import os

def send_notification(msg):
    # It's better to keep these in GitHub Secrets (Settings > Secrets)
    # But for a quick test, you can paste them here
    phone = "+918500913198" # Your number with country code
    apikey = "123456"       # The key from CallMeBot
    
    # Create the special URL
    url = f"https://api.callmebot.com/whatsapp.php?phone={phone}&text={msg}&apikey={apikey}"
    
    # This 'pings' the URL which sends the WhatsApp
    response = requests.get(url)
    
    if response.status_code == 200:
        print("WhatsApp sent successfully!")
    else:
        print(f"Error: {response.text}")