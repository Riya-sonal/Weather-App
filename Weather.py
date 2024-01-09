import requests

def get_weather(api_key, city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

        data = response.json()

        if response.status_code == 200:
            print(f"\nCurrent Weather in {city}:")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Description: {data['weather'][0]['description']}")
            print(f"Humidity: {data['main']['humidity']}%")
            print(f"Wind Speed: {data['wind']['speed']} m/s")
        else:
            print(f"Error: {data['message']}")

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    api_key = 'Your_api_key'
    
    # Input the city for which you want to fetch the weather
    city = input("Enter the city: ")

    get_weather(api_key, city)
