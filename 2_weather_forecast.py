class WeatherDataFetcher:
    def __init__(self):
        self.weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70}
        }

    def fetch_weather_data(self, city):
        # Simulated function to fetch weather data for a given city
        print(f"Fetching weather data for {city}...")
        return self.weather_data.get(city, {})


class DataParser:
    def parse_weather_data(self, data):
        # Function to parse weather data
        if not data:
            return "Weather data not available"
        city = data.get("city", "Unknown City")
        temperature = data.get("temperature", "N/A")
        condition = data.get("condition", "N/A")
        humidity = data.get("humidity", "N/A")
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"


class UserInterface:
    def __init__(self):
        self.weather_fetcher = WeatherDataFetcher()
        self.data_parser = DataParser()

    def get_detailed_forecast(self, city):
        # Function to provide a detailed weather forecast for a city
        data = self.weather_fetcher.fetch_weather_data(city)
        return self.data_parser.parse_weather_data(data)

    def display_weather(self, city):
        # Function to display the basic weather forecast for a city
        data = self.weather_fetcher.fetch_weather_data(city)
        if not data:
            return f"Weather data not available for {city}"
        else:
            return self.data_parser.parse_weather_data(data)

    def run(self):
        while True:
            city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
            if city.lower() == 'exit':
                break
            detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
            if detailed == 'yes':
                forecast = self.get_detailed_forecast(city)
            else:
                forecast = self.display_weather(city)
            print(forecast)


if __name__ == "__main__":
    interface = UserInterface()
    interface.run()




#   I keep getting "Weather in Unknown City: 60 degrees, Cloudy, Humidity: 65%" but idk why it keeps doing unknown city instead of displaying the actual city name :(