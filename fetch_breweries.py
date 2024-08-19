import requests

class Brewery:
    def __init__(self, name, state, city, brewery_type, website_url):
        self.name = name
        self.state = state
        self.city = city
        self.brewery_type = brewery_type
        self.website_url = website_url

class BreweryFetcher:
    def __init__(self, url):
        self.url = url

    def fetch_breweries(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to fetch data")
            return []

def list_breweries_by_state(breweries, states):
        breweries_by_state = {state: [] for state in states}
        for brewery in breweries:
            if brewery['state'] in states:
                breweries_by_state[brewery['state']].append(Brewery(
                    brewery['name'],
                    brewery['state'],
                    brewery['city'],
                    brewery['brewery_type'],
                    brewery['website_url']
                ))
        return breweries_by_state

def count_breweries_by_state(breweries_by_state):
    return {state: len(breweries) for state, breweries in breweries_by_state.items()}

def count_brewery_types_by_city(breweries_by_state):
    brewery_types_by_city = {}
    for state, breweries in breweries_by_state.items():
        for brewery in breweries:
            if brewery.city not in brewery_types_by_city:
                brewery_types_by_city[brewery.city] = {}
            if brewery.brewery_type not in brewery_types_by_city[brewery.city]:
                brewery_types_by_city[brewery.city][brewery.brewery_type] = 0
            brewery_types_by_city[brewery.city][brewery.brewery_type] += 1
    return brewery_types_by_city

def count_breweries_with_websites(breweries_by_state):
    breweries_with_websites = {state: 0 for state in breweries_by_state}
    for state, breweries in breweries_by_state.items():
        for brewery in breweries:
            if brewery.website_url:
                breweries_with_websites[state] += 1
    return breweries_with_websites

def main():
    url = "https://api.openbrewerydb.org/v1/breweries"
    states = ["Alaska", "Maine", "New York"]
    fetcher = BreweryFetcher(url)
    breweries_data = fetcher.fetch_breweries()
    breweries_by_state = list_breweries_by_state(breweries_data, states)

    # 1. List the names of all breweries present in the states of Alaska, Maine, and New York
    for state, breweries in breweries_by_state.items():
        print(f"Breweries in {state}:")
        for brewery in breweries:
            print(f" - {brewery.name}")
        print()

    # 2. Count of breweries in each of the states mentioned above
    breweries_count = count_breweries_by_state(breweries_by_state)
    print("Count of breweries in each state:")
    for state, count in breweries_count.items():
        print(f"{state}: {count}")
    print()

    # 3. Count the number of types of breweries present in individual cities of the states mentioned above
    brewery_types_by_city = count_brewery_types_by_city(breweries_by_state)
    print("Count of brewery types in individual cities:")
    for city, types in brewery_types_by_city.items():
        print(f"{city}:")
        for brewery_type, count in types.items():
            print(f" - {brewery_type}: {count}")
        print()

    # 4. Count and list how many breweries have websites in the states of Alaska, Maine, and New York
    breweries_with_websites = count_breweries_with_websites(breweries_by_state)
    print("Count of breweries with websites in each state:")
    for state, count in breweries_with_websites.items():
        print(f"{state}: {count}")

if __name__ == "__main__":
    main()
