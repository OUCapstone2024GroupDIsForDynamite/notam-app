from utilities.GeoUtilities import GeoUtilities
from objects.Coordinate import Coordinate

phnl = [ 21.3178172, -157.9202275 ]
kbos = [ 42.3629444, -71.0063889 ]

phnl_coords = Coordinate( phnl[0], phnl[1] )
kbos_coords = Coordinate( kbos[0], kbos[1] )


geo_utils = GeoUtilities()

coords = geo_utils.build_flight_path( phnl_coords, kbos_coords )

print( coords )

for coord in coords:
	print( f"{coord.latitude}, {coord.longitude}" )

