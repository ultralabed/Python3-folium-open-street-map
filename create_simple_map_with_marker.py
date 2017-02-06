import folium
map=folium.Map(location=[45.372, -121.697], zoom_start=12, tiles='Stamen Terrain')
map.simple_marker(location=[45.3288, -121.6625], popup='Mt. Hood Meadows', marker_color='red')
map.simple_marker(location=[45.3311, -121.7311], popup='Timberlake Lodge', marker_color='yellow')

map.create_map(path='simple_map_with_marker.html')
