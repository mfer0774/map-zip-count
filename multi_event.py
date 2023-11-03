import folium

#TODO: import data

radius_scale = 0.1 # adjust this to scale circle size

# assumes 'latitude', 'longitude', and 'Ticket_Count' columns
def create_map(data1, data2, output_html='ticket_sales_map.html'):
    # create the map centered on the average coordinates
    map = folium.Map(location=[data1['latitude'].mean(), data1['longitude'].mean()], zoom_start=4)

    # function to add markers to the map
    def add_markers(data, map_object, color):
        for idx, row in data.iterrows():
            folium.CircleMarker(
                location=[row['latitude'], row['longitude']],
                radius=row['Ticket_Count'] * radius_scale,  
                color=color,
                fill=True,
                fill_color=color,
                popup=f"Zip: {row['zipCode']}, Tickets: {row['Ticket_Count']}"
            ).add_to(map_object)

    # add markers for the first dataset in blue
    add_markers(data1, map, 'blue')

    # add markers for the second dataset in red
    add_markers(data2, map, 'red')

    # save the map to an HTML file
    map.save(output_html)
    print(f"Map has been created and saved as '{output_html}'")

create_map(data1, data2, 'ticket_sales_map.html')
