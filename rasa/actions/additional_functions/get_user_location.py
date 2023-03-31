import requests

def get_user_location():
        # Set up the API URL and request headers
        # Get complete geolocation for the calling machine's IP address
        url = "http://ipwho.is/"
        geolocation = requests.get(url=url)
        geolocation = geolocation.json()
        return {'country': geolocation['country'], 'city': geolocation['city']}
        # return geolocation