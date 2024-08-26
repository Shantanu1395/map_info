import folium
import matplotlib.pyplot as plt


def create_map(df):
    # Create a base map
    m = folium.Map(location=[20, 0], zoom_start=2)

    # Add markers to the map
    for i, row in df.iterrows():
        # Prepare the HTML content for the popup, including multiple images
        image_tags = ''.join(
            [f'<img src="{img}" alt="Image" style="width:150px;height:auto;"><br>' for img in row['Images']])
        popup_content = f"""
        <strong>{row['Name']}</strong><br>
        Continent: {row['Continent']}<br>
        Country: {row['Country']}<br>
        Type: {row['Type']}<br>
        Budget: {row['Budget']} billion USD<br>
        ETA: {row['ETA']}<br>
        {image_tags}
        """

        folium.CircleMarker(
            location=(row['Latitude'], row['Longitude']),
            radius=row['Radius'],  # Use radius from data
            color=row['Color'],  # Use color from data
            fill=True,
            fill_opacity=0.6,
            popup=folium.Popup(popup_content, max_width=250)
        ).add_to(m)

    return m


def save_map(m, filename='locations_map.html'):
    m.save(filename)


def create_svg_chart(df):
    # Filter the data to get only the projects
    df_projects = df[df['Type'] == 'Projects']

    # Aggregate the data by continent and country
    budget_by_continent = df_projects.groupby(['Continent', 'Country'])['Budget'].sum().sort_values(ascending=False)

    # Create a bar chart
    fig, ax = plt.subplots(figsize=(10, 6))
    budget_by_continent.plot(kind='bar', color='skyblue', ax=ax)

    # Add titles and labels
    ax.set_title('Project Budgets by Continent and Country')
    ax.set_xlabel('Continent, Country')
    ax.set_ylabel('Budget (in billion USD)')

    return fig


def save_svg_chart(fig, filename='project_budgets.svg'):
    fig.savefig(filename, format='svg')
