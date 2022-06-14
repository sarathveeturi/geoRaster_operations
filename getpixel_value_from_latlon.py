from osgeo import gdal 
import geopandas as gpd
import rasterio

gcp_file = r'C:/Users/sarat/OneDrive/Documents/data/Vancouver_39372/test_data/imagepoints_GCP_vancouver.shp'

image_file = r'C:/Users/sarat/OneDrive/Documents/data/Vancouver_39372/test_data/vancouver_MSImage_EPSG3157.tif'

def getpixelvalue_from_latlong(shapeFile, imageFile):
	shp_file = gpd.read_file(gcp_file)

	raster_file = rasterio.open(image_file)

	for point in shp_file.geometry:

		for i in range(0,shp_file.geometry.count()):
			#print(i)

			x = shp_file.iloc[i].geometry.centroid.x

			y = shp_file.iloc[i].geometry.centroid.y

			row, col = raster_file.index(x,y)
			#print(x, y)

			print("Pixel coordinates of point ({x}, {y}):".format(x=x, y=y), row, col)
	
		if i == shp_file.geometry.count()-1:
			break


getpixelvalue_from_latlong(gcp_file, image_file)
