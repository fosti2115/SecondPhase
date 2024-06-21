import requests

# Przykładowy Google API Key - użyj go do testowania swojego narzędzia do skanowania secretów
API_KEY = 'AIzaSyD-vbf32de9Abc5_examplekey_ZZZaa-QRsQ'

def get_geocode(address):
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == "__main__":
    address = "1600 Amphitheatre Parkway, Mountain View, CA"
    result = get_geocode(address)
    if result:
        print(result)
    else:
        print("Error fetching geocode data")
