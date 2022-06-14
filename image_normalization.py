import cv2
import rasterio

def normalization(src_path, dst_path, indexes=[0, 1, 2], alpha=1.0, beta=0.0):
    src = rasterio.open(fp=src_path)
    img = src.read()[indexes, :, :]
    
    with rasterio.Env():
        profile = src.profile
        print(profile)
        profile.update(
            dtype=rasterio.uint8,
            nodata=beta,
            count=3
        )
        #with rasterio.open(fp=dst_path, mode='w', **profile) as dst:
        #    dst.write(alpha * cv2.normalize(src=img, dst=None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX) + beta)

src_path = 'C:/Users/sarat/OneDrive/Documents/data/Sussex-data-layers-geogratis/airbus_Image/sussex_image.tif'
dst_path = 'C:/Users/sarat/OneDrive/Documents/data/Sussex-data-layers-geogratis/airbus_Image/2022 - 50 cm, Sussex, Pleiades_norm_aplha10.tif'

normalization(
    src_path=src_path,
    dst_path=dst_path, 
    indexes=[0, 1, 2], 
    alpha=10.0, 
    beta=0.0)