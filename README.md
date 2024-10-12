# Weather Fetcher

## Description
This is a simple command-line application that retrieves current weather information for a specified city using the OpenWeatherMap API. Users can enter the name of the city, and the application will display the weather description, current temperature, and how it feels.

## Features
- Fetches weather data from OpenWeatherMap API
- Displays current weather conditions and temperature
- User-friendly command-line interface

## Requirements
- Python 3.x
- `requests` library

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/azaan03/weather-fetcher.git
   cd weather-fetcher
   ```

2. Install the required libraries:
   ```bash
   pip install requests
   ```

3. Replace the API key in the code with your own from OpenWeatherMap:
   ```python
   api_key = "YOUR_API_KEY"  # Replace with your actual API key
   ```

## Usage
1. Run the script:
   ```bash
   python weather.py
   ```

2. Enter the city name when prompted. The application will display:
   - Today's weather description
   - Current temperature
   - Feels like temperature

## Example Output
```
Enter the City Name: London
Today's weather is: clear sky
Current temperature: 15 °C
But feels like: 14 °C
```

## Error Handling
If the city name is not found or there’s an issue with the API request, an error message will be displayed with the status code.

## License
This project is licensed under the MIT License.
