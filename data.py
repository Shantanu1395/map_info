import logging

def get_data():
    logger = logging.getLogger(__name__)
    try:
        data = {
            'Asia': {
                'Saudi Arabia': {
                    'Projects': [
                        {
                            'Name': 'NEOM (including The Line)',
                            'Budget': 500,  # in billion dollars
                            'ETA': 2030,
                            'Latitude': 28.5,
                            'Longitude': 35.0,
                            'Color': 'blue',
                            'Radius': 15,
                            'Image': []  # No additional images, will fetch from Wikipedia
                        },
                        {
                            'Name': 'King Abdullah Economic City (KAEC)',
                            'Budget': 100,  # in billion dollars
                            'ETA': 2035,
                            'Latitude': 22.35,
                            'Longitude': 39.05,
                            'Color': 'blue',
                            'Radius': 10,
                            'Image': ['https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.constructionweekonline.com%2Fbusiness%2Fsaudi-arabia-kaec-signs-significant-agreement-for-29000-sqm-luxury-resort&psig=AOvVaw2QvdFjGf-nnxM9pMk3se4e&ust=1724790888531000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCMDY3vTAk4gDFQAAAAAdAAAAABAE']  # Custom image link
                        }
                    ],
                    'Temples': [
                        {
                            'Name': 'Al-Masjid an-Nabawi',
                            'Latitude': 24.467,
                            'Longitude': 39.6,
                            'Color': 'purple',
                            'Radius': 8,
                            'Image': []  # No additional images, will fetch from Wikipedia
                        }
                    ],
                    'Historic Places': [
                        {
                            'Name': 'Mada\'in Saleh',
                            'Latitude': 26.796,
                            'Longitude': 37.961,
                            'Color': 'orange',
                            'Radius': 8,
                            'Image': ['https://www.constructionweekonline.com/cloud/2023/06/12/King-Abdullah-Economic-City.jpg']  # No additional images, will fetch from Wikipedia
                        }
                    ]
                },
                'South Korea': {
                    'Projects': [
                        {
                            'Name': 'Sejong Smart City',
                            'Budget': 30,  # in billion dollars
                            'ETA': 2030,
                            'Latitude': 36.5,
                            'Longitude': 127.25,
                            'Color': 'blue',
                            'Radius': 10,
                            'Image': []  # No additional images, will fetch from Wikipedia
                        },
                        {
                            'Name': 'Songdo International Business District',
                            'Budget': 40,  # in billion dollars
                            'ETA': 2022,
                            'Latitude': 37.38,
                            'Longitude': 126.63,
                            'Color': 'blue',
                            'Radius': 10,
                            'Image': ['https://example.com/songdo.jpg']  # Custom image link
                        }
                    ],
                    'Historic Places': [
                        {
                            'Name': 'Gyeongbokgung Palace',
                            'Latitude': 37.579,
                            'Longitude': 126.977,
                            'Color': 'orange',
                            'Radius': 8,
                            'Image': []  # No additional images, will fetch from Wikipedia
                        }
                    ]
                }
            }
        }
        logger.info("Data fetched successfully.")
        return data
    except Exception as e:
        logger.error("Error fetching data", exc_info=True)
        raise
