# Install nfty on ios, android, or desktop
#
# You'll want to create your own topic to subscribe to.
# They're public, so you'll get a notification every time this file 
# is cloned/deployed if you subscribe to 'heliumdenver'
#
# I'm getting a lot of push notifications on 'heliumdenver', and this is good!
# It means folks are using this. But do keep that in mind, and be sure to modify 
# your subscription here in the code to match what you'd like your subscription 
# to be called when you're setting it up in the ntfy app!
#
# Anyone who subscribes to 'heliumdenver' will get a push notification 
# everytime someone clones and runs this script! 

import requests
import time

def send_notification(message):
    headers = {
        'Title': 'HeliumDenver',
        'Priority': 'urgent',
        'Tags': 'balloon'
    }
    data = message.replace('+', ' ')
    response = requests.post('https://ntfy.sh/heliumdenver', headers=headers, data=data)
    print(response.text)

countdown_date = time.mktime(time.strptime('April 18, 2023 10:00:00', '%B %d, %Y %H:%M:%S'))

last_reminder = None

while True:
    now = time.time()
    remaining_time = int(countdown_date - now)

    if remaining_time <= 0:
        message = 'The Helium x Solana migration has begun!'
        send_notification(message)
        break
    elif remaining_time > 86400:
        # Send notification 24 hours before event, but only once a day
        if last_reminder is None or (now - last_reminder) >= 86400:
            message = f'Just {int(remaining_time/86400)} days until the Solana migration!'
            send_notification(message)
            last_reminder = now
    elif remaining_time > 43200:
        message = 'Just 12 hours until the Solana migration!'
    elif remaining_time > 21600:
        message = 'Just 6 hours until the Solana migration!'
    elif remaining_time > 10800:
        message = 'Just 3 hours until the Solana migration!'
    elif remaining_time > 7200:
        message = 'Just 2 hours until the Solana migration!'
    elif remaining_time > 3600:
        message = 'Just 1 hour until the Solana migration!'
    elif remaining_time > 0:
        # Send notification every 10 minutes in the last hour
        if last_reminder is None or (now - last_reminder) >= 600:
            message = f'Only {int(remaining_time/60)} minutes until the Solana migration!'
            send_notification(message)
            last_reminder = now
    else:
        # The event has already started, so break out of the loop
        break

    time.sleep(60) # wait for 1 minute before checking again



