import os, sys
import pickle
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import scipy.spatial.distance as dist


def estimate_top_view_sigmas(pkl_file):
	''' call this on 'AMT_data/top/AMT15_csv.pkl'
	we estimate keypoint accuracy in terms of the Object Keypoint Similarity (OKS) after Ronchi and Perona 2017.
	The OKS between a detection theta-hat(p) and the annotation theta(p) of a person p is the average over the
	labeled parts in the ground-truth (v_i) of the Keypoint Similarity between corresponding keypoint pairs.
	
	From equation 1 in that paper, the Keypoint Similarity (ks) is defined as:
	ks(theta-hat(p), theta(p)) = exp( - ||theta-hat_(p) - theta(p)||^2_2 / (2*s^2*k^2)
	
	Where s is the area of the instance, measured in pixels, and k is a keypoint-specific standard deviation
	that estimates the degree of between-annotator variability in labeling that point.
	
	In the CoCo evaluation API, the value of k for annotations of human poses ranges from 0.025 to 0.107,
	with more reliably placed body parts (such as the eyes) having the lowest values of k.
	
	should return:
	array([0.03889304, 0.04519708, 0.04505679, 0.04170943, 0.06655941,
       0.0666152 , 0.04375891, 0.06663153, 0.08359647])
	'''
	
	with open(pkl_file,'rb') as fp:
		D = pickle.load(fp)

	area_vec = []
	X = []
	Y= []

	for j in range(9):
		x = []
		y = []
		for i in range(len(D)):
			x.append((D[i]['ann_B']['X'][:,j]*1024).tolist()) # scale by top-view camera dimensions
			x.append((D[i]['ann_W']['X'][:,j]*1024).tolist())
			y.append((D[i]['ann_B']['Y'][:,j]*570).tolist())
			y.append((D[i]['ann_W']['Y'][:,j]*570).tolist())
		X.append(x)
		Y.append(y)

	for i in range(len(D)):
		area_vec.append(D[i]['ann_B']['area'])
		area_vec.append(D[i]['ann_W']['area'])

	X = np.asarray(X)
	Y = np.asarray(Y)
	area_vec = np.asarray(area_vec)

	D = np.zeros((len(X),len(X[0])))
	sigma = np.zeros(len(X))
	for j in range(len(X)):
		for i in range(len(X[0])):
			xy = np.asarray([X[j][i], Y[j][i]]).reshape((2,len(X[j][i]))).T
			gt = np.median(xy,0)
			D[j][i] = np.mean(np.std(xy,0)) 
			D[j][i] /= np.sqrt(area_vec[i])*np.sqrt(2) # normalization to match CoCo definition of sigma
		sigma[j] = np.mean(D[j])
	
	return sigma



def estimate_front_view_sigmas(pkl_file):
	''' call this on 'AMT_data/top/AMT15_csv.pkl'
	we estimate keypoint accuracy in terms of the Object Keypoint Similarity (OKS) after Ronchi and Perona 2017.
	The OKS between a detection theta-hat(p) and the annotation theta(p) of a person p is the average over the
	labeled parts in the ground-truth (v_i) of the Keypoint Similarity between corresponding keypoint pairs.
	
	From equation 1 in that paper, the Keypoint Similarity (ks) is defined as:
	ks(theta-hat(p), theta(p)) = exp( - ||theta-hat_(p) - theta(p)||^2_2 / (2*s^2*k^2)
	
	Where s is the area of the instance, measured in pixels, and k is a keypoint-specific standard deviation
	that estimates the degree of between-annotator variability in labeling that point.
	
	In the CoCo evaluation API, the value of k for annotations of human poses ranges from 0.025 to 0.107,
	with more reliably placed body parts (such as the eyes) having the lowest values of k.
	
	should return:
	array([0.0873309 , 0.08602119, 0.0868102 , 0.09301264, 0.12411955,
       0.12454425, 0.0861696 , 0.1080549 , 0.14485149, 0.1274594 ,
       0.12496106, 0.12034103, 0.12748996])
	'''
	
	with open(pkl_file,'rb') as fp:
		D = pickle.load(fp)
	
	area_vec = []
	X = []
	Y = []

	for j in range(13):
		x = []
		y = []
		for i in range(len(D)):
			x.append((D[i]['ann_B']['X'][:,j]*1280).tolist()) # scale by front-view camera dimensions
			x.append((D[i]['ann_W']['X'][:,j]*1280).tolist())
			y.append((D[i]['ann_B']['Y'][:,j]*500).tolist())
			y.append((D[i]['ann_W']['Y'][:,j]*500).tolist())
		X.append(x)
		Y.append(y)

	for i in range(len(D)):
		area_vec.append(D[i]['ann_B']['area'])
		area_vec.append(D[i]['ann_W']['area'])

	X = np.asarray(X)
	Y = np.asarray(Y)
	area_vec = np.asarray(area_vec)

	D = np.zeros((len(X),len(X[0])))
	sigma = np.zeros(len(X))
	for j in range(len(X)):
		for i in range(len(X[0])):
			xy = np.asarray([X[j][i], Y[j][i]]).reshape((2,len(X[j][i]))).T
			D[j][i] = np.mean(np.std(xy,0))
			D[j][i] /= np.sqrt(area_vec[i])*np.sqrt(2) # normalization to match CoCo definition of sigma
		sigma[j] = np.mean(D[j])
	
	return sigma

