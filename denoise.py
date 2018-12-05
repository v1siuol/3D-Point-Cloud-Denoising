from scipy.spatial import Delaunay
import numpy as np
import math
from cloud_to_gts import gts_write
from cloud_to_gts import input_triangulation
from run_non_iterative import run_non_iterative
from BilateralMeshDenoising import run_bilateral_denoising


def run_denoise():
    print("3D POINT CLOUD DENOISING")
    print()
    print("Primary Algorithms: ")
    print("1: Bilateral Mesh Denoising")
    print("2: Non-Iterative Feature Preserving Mesh Smoothing")

    method = 0
    method = int(input("Selection: "))

    if(method == 1):
        run_bilateral_denoising()

    if(method == 2):
        run_non_iterative()

run_denoise()