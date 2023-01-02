# Damn thing still doesn't work

import requests

# Your CoinMarketCap Pro API key
api_key = 'YOUR_API_KEY_HERE'

# A dictionary to store the tokens in the portfolio
portfolio = {}

while True:
  # Prompt the user to enter a token
  token = input("Enter a token (enter 'done' when finished): ")

  # If the user is finished, break out of the loop
  if token.lower() == 'done':
    break

  # Prompt the user to enter the quantity of the token
  quantity = int(input("Enter the quantity of " + token + ": "))

  # Add the token and quantity to the portfolio
  portfolio[token] = quantity

# Calculate the portfolio balance by fetching the all-time high prices of the tokens and multiplying them by the quantities
portfolio_balance = 0
for token, quantity in portfolio.items():
  # Send a request to the CoinMarketCap API to get the all-time high price of the token
  response = requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest',
                         params={'symbol': token, 'convert': 'USD'},
                         headers={'X-CMC_PRO_API_KEY': api_key})
    # Check if the API returned an error
  if 'data' not in response.json():
  # Get the all-time high price of the token from the response
  all_time_high_price = response.json()['data'][0]['all_time_high']['price']

  # Calculate the value of the token at its all-time high price
  token_value = quantity * all_time_high_price

  # Add the value of the token to the portfolio balance
  portfolio_balance += token_value

# Display the portfolio balance to the user
print("Portfolio balance: $" + str(portfolio_balance))
