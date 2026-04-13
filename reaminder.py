import os
from datetime import datetime, timedelta

# Configuration: Update these with your actual due dates
RENT_DUE_DAY = 1  # 1st of the month
BILL_DUE_DAY = 15 # 15th of the month

def check_dates():
    today = datetime.now()
    # Logic: Look 5 days into the future
    target_date = today + timedelta(days=5)
    
    events = []
    if target_date.day == RENT_DUE_DAY:
        events.append("Rent is due in 5 days!")
    if target_date.day == BILL_DUE_DAY:
        events.append("Current Bill is due in 5 days!")

    if events:
        message = " | ".join(events)
        send_notification(message)
    else:
        print("No reminders for today.")

def send_notification(msg):
    # For now, we print it. 
    # Later, you can add Twilio or Telegram code here.
    print(f"TRIGGERED: {msg}")

if __name__ == "__main__":
    check_dates()