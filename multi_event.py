import folium

#TODO: import data

# assumes 'latitude', 'longitude', and 'Ticket_Count' columns
def create_map(data1, data2, output_html='ticket_sales_map.html'):
    # Create the map centered on the average coordinates
    map = folium.Map(location=[data1['latitude'].mean(), data1['longitude'].mean()], zoom_start=4)

    # Function to add markers to the map
    def add_markers(data, map_object, color):
        for idx, row in data.iterrows():
            folium.CircleMarker(
                location=[row['latitude'], row['longitude']],
                radius=row['Ticket_Count'] * 0.1,  # Adjust this factor as needed
                color=color,
                fill=True,
                fill_color=color,
                popup=f"Zip: {row['zipCode']}, Tickets: {row['Ticket_Count']}"
            ).add_to(map_object)

    # Add markers for the first dataset in blue
    add_markers(data1, map, 'blue')

    # Add markers for the second dataset in red
    add_markers(data2, map, 'red')

    # Save the map to an HTML file
    map.save(output_html)
    print(f"Map has been created and saved as '{output_html}'")

# Example usage:
# create_map(data1, data2, 'ticket_sales_map.html')
