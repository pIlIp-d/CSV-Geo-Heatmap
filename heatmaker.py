# -*- coding: utf-8 -*-
# ==================================================================
#   csv geo heatmap - a tool for converting csv to html heatmap  
#
#   Copyright 2022 Philip Dell - https://github.com/pIlIp-d
#   MIT License
# ==================================================================

import os, sys
import argparse

import pandas as pd
from folium import Map
from folium.plugins import HeatMap

def read_file(file, enc):
    return pd.read_csv(file, encoding=enc)

def create_map(df, start_location, zoom_factor):
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
    all_args = argparse.ArgumentParser(prog='Heatmaker', usage='%(prog)s [options]', description='Converts .csv with latitude and longitude columns into geo-heatmap.')
    all_args.add_argument("-p", "--path", required=True, help="path to csv file")
    all_args.add_argument("-e", "--encoding", required=False, default='latin1')
    all_args.add_argument("-z", "--zoom_at_start", required=False, type=int, default=8)
    args = vars(all_args.parse_args())
    print("reading data.")
    map_data = read_file(args['path'],args['encoding'])
    print("creating map.")
    map = create_map(map_data, [49.4076800, 8.6907900], args['zoom_at_start'])
    save(map, 'heatmap.html')
    print("Done!")
