from plotly import graph_objects as go
import plotly.io as pio
import json

with open("Bagmati_survey.geojson") as file:
    geojson_data = json.load(file)

#Create figure object
fig = go.Figure(
    go.Choroplethmapbox(
        geojson = geojson_data, #Assign geojson file
        featureidkey = "properties.NAME_3", #Assign feature key
        locations = ["Bhaktapur","Dhading","Kathmandu","Kavrepalanchok","Lalitpur","Nuwakot","Rasuwa","Sindhupalchok","Dolakha","Ramechhap","Sindhuli","Chitawan","Makwanpur"], #Assign location data
        z = [0,0,1,0,1,1,0,1,1,0,0,1,0], #Assign information data
        # z = [0,0,4,0,1,1,0,2,1,0,0,1,0], #Assign information data
        zauto = True,
        # colorscale='viridis',
        colorscale = [[0, 'lightgrey'], [1, 'DarkBlue']],
        # showscale = True,
        showscale = False,
        # hovertext= ["Bhaktapur","Dhading","Kathmandu","Kavrepalanchok","Lalitpur","Nuwakot","Rasuwa","Sindhupalchok","Dolakha","Ramechhap","Sindhuli","Chitawan","Makwanpur"]
    )
)

#Update layout
fig.update_layout(
    mapbox_style = "white-bg", #Decide a style for the map
    mapbox_zoom = 10, #Zoom in scale
    mapbox_center = {"lat": 27.7172, "lon": 85.3240}, #Center location of the map
)

fig.show()

width = 1000
height = 800
scale = 10
pio.write_image(fig,'New.png',format = 'png', width=width, height=height, scale=scale )