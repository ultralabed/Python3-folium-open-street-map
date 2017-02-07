import folium
import pandas

df=pandas.read_csv("assets/Volcanoes-USA.txt")

map=folium.Map(location=[df["LAT"].mean(), df["LON"].mean()], zoom_start=6, tiles='Stamen Terrain')

def color(elev):
    minimum=int(min(df["ELEV"]))
    step=int((max(df["ELEV"])-min(df["ELEV"]))/3)
    if elev in range(minimum, step):
        col='green'
    elif elev in range(minimum+step, minimum+step*2):
        col='orange'
    else:
        col='red'
    return col

for lat, lon, name, elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
    map.add_children(folium.Marker(location=[lat, lon], popup=name, icon=folium.Icon(color=color(elev), icon_color='green')))

map.save(outfile='usa_volcanoes_map.html')
