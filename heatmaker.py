import os, sys

import pandas as pd
from folium import Map
from folium.plugins import HeatMap

def read_file(file, enc = 'latin1'):
    return pd.read_csv(file, encoding=enc)

def create_map(df, start_location, zoom_factor = 8):
    #df             - contains langitude and latitude values for each DataPoint
    #start_location - contains [lat,long]
    return Map(location=start_location, zoom_start=zoom_factor, ).add_child(
        HeatMap(
            list(zip(df.latitude.values, df.longitude.values)),
            min_opacity=0.2,
            radius=17,
            blur=15,
            max_zoom=1,
        )
    )

def save(map, path):
    map.save(path, 'w+')

if __name__ == '__main__':
    if len(sys.argv) > 2:
        if (sys.argv[1] == '-p'):
            csv_path = sys.argv[2]
    else:
        print("Missing path argunment! -p 'path'")
        quit(-1)
    print("reading data.")
    map_data = read_file(csv_path)
    print("creating map.")
    map = create_map(map_data, [49.4076800, 8.6907900])
    save(map, os.path.join('results', 'heatmap.html'))
    print("Done!")
