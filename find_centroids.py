import argparse
import geopandas as gp


def main():

    all_args = argparse.ArgumentParser()

    all_args.add_argument("-i", "--inFile", required=True,  help="geojson file of arbitrary geometry exported from Overpass")
    all_args.add_argument("-o", "--outFile", required=True, help="geojson file containing centroids of the above geometry")
    args = vars(all_args.parse_args())
    inFile = args['inFile']
    outFile = args['outFile']

    gdf = gp.read_file(inFile)
    #gdf.set_crs('epsg:4326')
    gdf['centroid'] = gdf.centroid
    gdf = gdf.set_geometry('centroid', drop=True)
    with open(outFile, 'w') as centroid_file:
        centroid_file.write(gdf.to_json(na='drop'))
    #gdf.to_file("centroids.geojson", driver="GeoJSON")

if __name__ == "__main__":
    main()
