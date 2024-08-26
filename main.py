# main.py
import os
from data import get_data
from processing import load_data_to_dataframe
from visualizing import create_map, save_map


def main():
    # Get data
    data = get_data()

    # Process data into a DataFrame
    df = load_data_to_dataframe(data)

    # Create a map
    map_ = create_map(df)

    # Define the output directory
    output_dir = 'output'

    # Create the directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the map to the output directory
    output_path = os.path.join(output_dir, 'mega_projects_map.html')
    save_map(map_, output_path)

if __name__ == '__main__':
    main()
