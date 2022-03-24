# CSV-Geo-Heatmap
Create an html geographical heatmap from a csv.

## Dependency
Install all required packages 
`pip3 install argparse, pandas, folium`

## Usage

* csv file has a column for longitude and latitude
* run with path to csv `heatmaker.py -p path.csv`
* open heatmap.html in browser of your choice

### Options

```
required arguments:
    -p PATH, --path PATH  path to csv file
optional arguments:
  -e ENCODING, --encoding ENCODING                  default='latin-1'
  -z ZOOM_AT_START, --zoom_at_start ZOOM_AT_START   default=8
```
