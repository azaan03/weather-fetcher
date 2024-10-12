import requests

# Get the city name from user input
city_name = input("Enter the City Name: ")

# API key for OpenWeatherMap
api_key = "27662fe2c73819ab1ecf3f03281f73a9"

# Construct the API URL
base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

# Send a request to the OpenWeatherMap API
response = requests.get(base_url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Extract and display relevant information
    print('Today\'s weather is:', data['weather'][0]['description'])
    print('Current temperature:', data['main']['temp'], '°C')
    print('But feels like:', data['main']['feels_like'], '°C')
else:
    # Handle errors
    print("Error:", response.status_code, response.reason)
