import os
import numpy as np


gcp_file = "C:/Users/sarat/OneDrive/Documents/data/053668288010_01_P001_PAN/053668288010_01_P001_PAN/GCP_lat,lon,alt.csv"

img = "C:/Users/sarat/OneDrive/Documents/data/053668288010_01_P001_PAN/053668288010_01_P001_PAN/11JUL20154515-P2AS-053668288010_01_P001.tif"

epsg = "4326"

def translation(gcp_file, img, epsg):
    """ returns the best translation matrix via GCPs """

    # initial translation matrix
    mch_opn = np.loadtxt(gcp_file)
    print(mch_opn.ndim)
    trm = [1, 0, 0, 0, 1, 0]

    gdaltransform(img_nme, rpc, )

    if mch_opn.ndim == 2:

        # back transform ground coordinate system to image via RPC. note: EPSG demonstrates GCPs coordinate system
        X, Y, Z = mch_opn[:, 0].tolist(), mch_opn[:, 1].tolist(), mch_opn[:, 2].tolist()
        
        xd, yd = rpc_transform(img_nme, epsg, X, Y, Z)
        xt, yt = mch_opn[:, 3], mch_opn[:, 4]

        # estimate the best translation parameters
        dx = np.average(xt - np.array(xd))  
        dy = np.average(yt - np.array(yd))

        # generate translation matrix
        trm = [1, 0, dx.tolist(), 0, 1, dy.tolist()]
    return trm

translation(gcp_file, img, epsg)