from shapely.geometry import asShape, mapping


def poly_point_simplify(features, min_area):
    for feature in features:
        geom = asShape(feature['geometry'])
        if geom.area < min_area:
            newgeom = geom.centroid
            feature['geometry'] = mapping(newgeom)
        yield feature
