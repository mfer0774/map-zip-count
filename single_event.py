import pandas as pd
import folium
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from time import sleep

# load the data
data_path = 'data.csv'  # update the path if needed
data = pd.read_csv(data_path)

# initialize Nominatim Geocoder
geolocator = Nominatim(user_agent="7875tolfkjdkajjfakdsj")

# function to geocode using Nominatim
def geocode(zip_code):
    try:
        location = geolocator.geocode(zip_code + ", USA")
        if location:
            return location.latitude, location.longitude
        else:
            return None, None
    except GeocoderTimedOut:
        return geocode(zip_code)

# add a sleep between geocoding calls to avoid hitting the request limit
def geocode_with_delay(zip_code):
    sleep(1)  # sleep for 1 second
    return geocode(zip_code)

# geocode each zip code
data[['latitude', 'longitude']] = data['zipCode'].apply(geocode_with_delay).apply(pd.Series)

# drop rows where geocoding failed (if any)
data = data.dropna(subset=['latitude', 'longitude'])

#TODO: add log for any dropped rows

# create the map
map = folium.Map(location=[39.8283, -98.5795], zoom_start=4)  # Center of the U.S.

# add markers to the map
for idx, row in data.iterrows():
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=row['Ticket_Count'] * 0.1,  # adjust this factor to scale circle sizes
        color='blue',
        fill=True,
        fill_color='blue',
        popup=f"Zip: {row['zipCode']}, Tickets: {row['Ticket_Count']}"
    ).add_to(map)

# save or show the map
map.save('ticket_sales_map.html')  # saves the map to an HTML file

# map  # uncomment if running in a Jupyter environment to display the map inline

print("map has been created and saved as 'ticket_sales_map.html'")
