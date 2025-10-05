import requests

def get_weather(city):
    api_key = "YOUR_REAL_API_KEY"  # replace with your actual API key
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    print("Request URL:", response.url)
    print("Response Text:", response.text)

    if response.status_code == 200:
        data = response.json()
        print(f"Weather in {city}:\n")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Condition: {data['weather'][0]['description'].capitalize()}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        print("City not found or error fetching data.")

get_weather("Lagos,NG")
