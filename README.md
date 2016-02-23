# poly-point-simplify

Replace geometries smaller than a certain area with points

```
$ cat collection.geojson | geojson-summary
177 multipolygons

$ poly-point-simplify --min-area 2 collection.geojson | geojson-summary
24 points and 153 multipolygons
```
