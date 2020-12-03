import numpy as np
import pandas as pd

def get_kinematics(x, z):
	dx = x - x.shift()
	dz = z - z.shift()
	d2x = dx - dx.shift()
	d2z = dz - dz.shift()

	speed = np.sqrt(dx**2 + dz**2)
	acceleration = np.sqrt(d2x**2 + d2z**2)

	return speed, acceleration

def remove_outliers(data, m):
	d = np.abs(data - np.nanmedian(data))
    mdev = np.nanmedian(d)
    s = d/mdev if mdev else 0.
    
    return np.where(s < m)