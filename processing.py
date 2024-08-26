import pandas as pd
import requests

def fetch_wikipedia_image(title):
    """Fetch the first image from Wikipedia for a given title."""
    url = f'https://en.wikipedia.org/api/rest_v1/page/summary/{title}'
    try:
        response = requests.get(url)  # Use certifi for SSL verification
        if response.status_code == 200:
            data = response.json()
            if 'thumbnail' in data and 'source' in data['thumbnail']:
                return data['thumbnail']['source']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Wikipedia image: {e}")
    return None


def flatten_data(data):
    records = []
    for continent, countries in data.items():
        for country, types in countries.items():
            for type_, items in types.items():
                for item in items:
                    images = item.get('Image', [])

                    # Fetch Wikipedia image if needed
                    if not images:
                        wikipedia_image = fetch_wikipedia_image(item['Name'])
                        if wikipedia_image:
                            images.append(wikipedia_image)

                    record = {
                        'Continent': continent,
                        'Country': country,
                        'Type': type_,
                        'Name': item['Name'],
                        'Latitude': item.get('Latitude'),
                        'Longitude': item.get('Longitude'),
                        'Budget': item.get('Budget'),
                        'ETA': item.get('ETA'),
                        'Color': item.get('Color'),
                        'Radius': item.get('Radius'),
                        'Images': images  # Note: 'Images' is now a list
                    }
                    records.append(record)
    return records


def load_data_to_dataframe(data):
    records = flatten_data(data)
    df = pd.DataFrame(records)
    return df
