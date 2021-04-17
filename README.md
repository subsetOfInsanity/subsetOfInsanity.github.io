# subsetOfInsanity.github.io
Demo of map for help in house hunting by showing proximity to useful things Mapbox and OpenStreetmap Overpass API.

## User Docs:

Any coloured area is within 500 meters of a useful shop.  Using the dialogs you can change this radius, or change to display another layer showing one of:
- Shops
- Pubs
- Rail Stations
- Parks


### Shops layer
Any coloured area is within 500 meters of a useful shop.  Only counting these shops for these purposes:
 - Sainsbury
 - Tesco
 - Co-op
 - Budgens
 - Waitrose
 - M&S Foodhall
 - Aldi
 - Lidl
 - Asda

### Parks layer
Includes all named public parks.

## Features on deck:
1. [DONE]Extend to all locations using dynamic fetching of OSM data.
1. Add loading notification for user while fetching and unioning data.
1. Parks layer. - Need to filter to useful parks.  Public, above a certain size?
1. Showing details of things counted for circles
1. Re-center by location, url, etc.
1. Use routes api to show walking time radius from a specified location.
1. Allow custom filtering - mod the Overpass ql query


## Dev Notes

Currently working to make the browser fetch data directly from Overpass API based on bounds of the Mapbox map.  Then we apply a buffer to the objects returned using Turf JS.  Then we union all the buffered objects, and display it as a fill layer.

Here are some issues to watch out for:
 - If we use a circle approach then the [opacity is cumulative](https://github.com/mapbox/mapbox-gl-js/issues/4090), so we do the union and fill layer approach instead.
 - There might be a better way to fetch the data more like hitting a tiling server or rendering as a layer style.  Right now it uses setData on moveend causing some latency when panning.  
 - It might be better to display the data as a [tweaked heatmap](https://gist.github.com/orangemug/8f4936833138864ac02e97595a5ff576)
 - Zooming out too far puts too much strain on the data-fetching causing timeouts and overloading the overpass API.
 - Zooming out too far puts too much strain on the Union operations causing browser to hang.
