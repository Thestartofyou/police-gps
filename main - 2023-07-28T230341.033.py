import requests
from geopy.geocoders import Nominatim

# Replace 'YOUR_API_KEY' with the actual API key obtained from the API provider
API_KEY = 'YOUR_API_KEY'
API_ENDPOINT = 'https://api.example.com/police_stations'  # Replace with the API URL

def get_police_stations(latitude, longitude):
    params = {
        'lat': latitude,
        'lon': longitude,
        'api_key': API_KEY,
    }

    response = requests.get(API_ENDPOINT, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch data - Status Code {response.status_code}")
        return None

def main():
    # Get current GPS location
    geolocator = Nominatim(user_agent="police_call_tracker")
    location = geolocator.geocode("Your Current Location")

    if location:
        latitude, longitude = location.latitude, location.longitude
        print(f"Your current GPS location: Latitude={latitude}, Longitude={longitude}")

        # Fetch nearby police stations
        police_stations = get_police_stations(latitude, longitude)

        if police_stations:
            print("Nearby Police Stations:")
            for station in police_stations:
                print(station['name'], station['address'])
        else:
            print("No police stations found nearby.")
    else:
        print("Unable to fetch your current GPS location.")

if __name__ == "__main__":
    main()
