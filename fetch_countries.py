import requests

class CountryData:
    def __init__(self, url):
        self.url = url

    # get the data from api
    def fetch_data(self):
        response = requests.get(self.url)
        return response.json()

    # display the countries info
    def display_country_info(self, data):
        for country in data:
            try:
                print(f"Country: {country['name']['common']}")
                print(f"Currencies: {list(country['currencies'].keys())}")
                print(f"Currency Symbols: {[country['currencies'][currency]['symbol'] for currency in country['currencies']]}")
                print()
            except:
                pass
    

    # display the countries with dollar
    def display_dollar_countries(self, data):
        for country in data:
            try:
                if 'USD' in country['currencies']:
                    print(f"Country: {country['name']['common']}")
            except:
                pass

    # display the euro currency countriess
    def display_euro_countries(self, data):
        for country in data:
            try:
                if 'EUR' in country['currencies']:
                    print(f"Country: {country['name']['common']}")
            except:
                pass


country_url = 'https://restcountries.com/v3.1/all'
country_data = CountryData(country_url)
data = country_data.fetch_data()

country_data.display_country_info(data)
print("\nCountries with USD as currency:")
country_data.display_dollar_countries(data)
print("\nCountries with EUR as currency:")
country_data.display_euro_countries(data)


