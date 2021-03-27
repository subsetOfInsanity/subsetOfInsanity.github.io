import geopandas as gp

gdf = gp.read_file("pubs.geojson")
#gdf.set_crs('epsg:4326')
gdf['centroid'] = gdf.centroid
gdf = gdf.set_geometry('centroid', drop=True)
with open('centroids.geojson', 'w') as centroid_file:
    centroid_file.write(gdf.to_json(na='drop'))
#gdf.to_file("centroids.geojson", driver="GeoJSON")


