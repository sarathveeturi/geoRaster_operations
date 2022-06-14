import laspy as lp
import numpy as np
import open3d as o3d

point_cloud_path = "C:/Users/sarat/OneDrive/Documents/data/3D projection data/2010_Haiti_Lidar.las"

def visualizePC(point_cloud_path):
	point_cloud = lp.read(point_cloud_path) #mode = "r")


	points = np.vstack((point_cloud.x, point_cloud.y, point_cloud.z)).transpose()
	#colors = np.vstack((point_cloud.red, point_cloud.green, point_cloud.blue)).transpose()

	pcd = o3d.geometry.PointCloud()
	pcd.points = o3d.utility.Vector3dVector(points)

	#pcd.colors = o3d.utility.Vector3dVector(colors/65535)
	#pcd.normals = o3d.utility.Vector3dVector(normals)

	o3d.visualization.draw_geometries([pcd])


visualizePC(point_cloud_path)