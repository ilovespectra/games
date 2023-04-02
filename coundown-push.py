# Install nfty on ios, android, or desktop
# You'll want to create your own topic to subscribe to, 
# they're public so you'll get these if you subscribe to heliumdenver
#
# I'm getting a lot of push notifications on 'heliumdenver', and this is good!
# It means folks are using this. But do keep that in mind, and be sure to modify 
# your subscription here in the code to match what you'd like your subscription 
# to be called when you're setting it up in the ntfy app!

import requests
import time

def send_notification(message):
    headers = {
        'Title': 'HeliumDenver',
        'Priority': 'urgent',
        'Tags': 'balloon'
    }
    data = message.replace('+', ' ')
    response = requests.post('https://ntfy.sh/heliumdenver', headers=headers, data=data) # modify your subscripton here 
    print(response.text)

countdown_date =  time.mktime(time.strptime('April 18, 2023 10:00:00', '%B %d, %Y %H:%M:%S'))

while True:
    now = time.time()
    remaining_time = int(countdown_date - now)

    if remaining_time <= 0:
        message = 'The Helium x Solana migration has begun!'
        send_notification(message)
        break
    elif remaining_time > 86400:
        # Send notification 24 hours before event
        message = f'Just {int(remaining_time/86400)} days until the Solana migration!'
    elif remaining_time > 43200:
        # Send notification 12 hours before event
        message = 'Just 12 hours until the Solana migration!'
    elif remaining_time > 21600:
        # Send notification 6 hours before event
        message = 'Just 6 hours until the Solana migration!'
    elif remaining_time > 10800:
        # Send notification 3 hours before event
        message = 'Just 3 hours until the Solana migration!'
    elif remaining_time > 7200:
        # Send notification 2 hours before event
        message = 'Just 2 hours until the Solana migration!'
    elif remaining_time > 3600:
        # Send notification 1 hour before event
        message = 'Just 1 hour until the Solana migration!'
    else:
        # Send notification every 10 minutes in the last hour
        message = 'The Solana migration is happening now!'
    send_notification(message)
    time.sleep(600) # wait for 10 minutes before sending the next notification
