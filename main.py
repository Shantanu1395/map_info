import logging
from data import get_data
from processing import load_data_to_dataframe
from visualizing import create_map, save_map, create_svg_chart, save_svg_chart

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)


def main():
    logger = logging.getLogger(__name__)
    try:
        # Get data
        logger.info("Fetching data...")
        data = get_data()

        # Process data into a DataFrame
        logger.info("Processing data into DataFrame...")
        df = load_data_to_dataframe(data)

        # Create a map
        logger.info("Creating map...")
        map_ = create_map(df)

        # Save the map to the output directory
        logger.info("Saving map...")
        save_map(map_, 'output/mega_projects_map.html')

        # Create and save an SVG chart
        logger.info("Creating and saving SVG chart...")
        fig = create_svg_chart(df)
        save_svg_chart(fig, 'output/project_budgets.svg')

        logger.info("Process completed successfully.")
    except Exception as e:
        logger.error("An error occurred", exc_info=True)


if __name__ == '__main__':
    main()
