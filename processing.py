import pandas as pd
import requests
import logging


def fetch_wikipedia_image(title):
    """Fetch the first image from Wikipedia for a given title."""
    logger = logging.getLogger(__name__)
    url = f'https://en.wikipedia.org/api/rest_v1/page/summary/{title}'
    try:
        response = requests.get(url, verify=False)  # Disable SSL verification
        if response.status_code == 200:
            data = response.json()
            if 'thumbnail' in data and 'source' in data['thumbnail']:
                logger.info(f"Fetched image for {title}")
                return data['thumbnail']['source']
        #logger.warning(f"No image found for {title}")
    except requests.exceptions.RequestException as e:
        #logger.warning(f"Error fetching Wikipedia image for {title}", exc_info=True)
        pass
    return None


def flatten_data(data):
    logger = logging.getLogger(__name__)
    records = []
    try:
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
        logger.info("Data flattened successfully.")
        return records
    except Exception as e:
        logger.error("Error flattening data", exc_info=True)
        raise


def load_data_to_dataframe(data):
    logger = logging.getLogger(__name__)
    try:
        records = flatten_data(data)
        df = pd.DataFrame(records)
        logger.info("Data loaded into DataFrame successfully.")
        return df
    except Exception as e:
        logger.error("Error loading data into DataFrame", exc_info=True)
        raise
