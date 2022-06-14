import open3d as o3d
from matplotlib import pyplot as plt

def visualize_3d_scene(input_dem_path, input_rgb_path):

	print("Reading given datasets..............")
	color_raw = o3d.io.read_image(input_rgb_path)
	depth_raw = o3d.io.read_image(input_dem_path)
	rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(color_raw, depth_raw)
	print(rgbd_image.dimension)

	plt.subplot(1, 2, 1)
	plt.title('3D scene')
	plt.imshow(rgbd_image.color)
	plt.subplot(1, 2, 2)
	plt.title('3D depth image')
	plt.imshow(rgbd_image.depth)
	plt.show()

	pcd = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd_image, o3d.camera.PinholeCameraIntrinsic(o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault))

	# Flip it, otherwise the pointcloud will be upside down
	pcd = pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])


	o3d.visualization.draw_geometries([pcd])#zoom=0.5)

if __name__ =='__main__':
	#input_dem_path = "C:/Users/sarat/OneDrive/Documents/data/3D projection data/dsm-alma-resize.png" #.png

	#input_rgb_path = "C:/Users/sarat/OneDrive/Documents/data/3D projection data/ortho-alma-resize.png" #.jpg

	input_dem_path = "C:/Users/sarat/OneDrive/Documents/data/3D projection data/rgbd_dataset_freiburg1_xyz/rgbd_dataset_freiburg1_xyz/depth/test_depthimage.png" #.png

	input_rgb_path = "C:/Users/sarat/OneDrive/Documents/data/3D projection data/rgbd_dataset_freiburg1_xyz/rgbd_dataset_freiburg1_xzy/rgb/test_rgbimage.png" #.jpg


	visualize_3d_scene(input_dem_path, input_rgb_path)



