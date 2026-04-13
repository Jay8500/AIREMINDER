import requests
from datetime import datetime, timedelta

def send_notification(msg):
    # YOUR DETAILS
    phone = "+91 8500913198" 
    apikey = "XXXXXX" # Put your REAL apikey here from WhatsApp
    
    url = f"https://api.callmebot.com/whatsapp.php?phone={phone}&text={msg}&apikey={apikey}"
    response = requests.get(url)
    
    if response.status_code == 200:
        print("WhatsApp sent successfully!")
    else:
        print(f"Error: {response.text}")

def check_dates():
    today = datetime.now()
    # Logic: Look 5 days into the future
    target_date = today + timedelta(days=5)
    
    # TODAY IS APRIL 13th, so TARGET_DATE IS APRIL 18th
    # To test it NOW, change RENT_DUE_DAY to 18
    RENT_DUE_DAY = 18 
    BILL_DUE_DAY = 15 

    if target_date.day == RENT_DUE_DAY:
        send_notification("REMINDER: Your House Rent is due in 5 days!")
    elif target_date.day == BILL_DUE_DAY:
        send_notification("REMINDER: Your Current Bill is due in 5 days!")
    else:
        print(f"Checked for date {target_date.day}. No reminders needed today.")

if __name__ == "__main__":
    print("Bot is starting up...")
    check_dates()