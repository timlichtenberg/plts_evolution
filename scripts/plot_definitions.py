import os, math, sys, glob, struct, matplotlib
from natsort import natsorted
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import pandas as pd
import scipy
import numpy as np
import seaborn as sns
import csv
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.patheffects as path_effects
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# Working directories
working_dir = os.getcwd()
dat_dir     = working_dir+"/../data/two_stage/data/planetesimal_evolution/"
fig_dir     = working_dir+"/../figures/"

fscale  = 3.5
fsize   = 20
lw      = 2.5

fsize_m = 20
fsize_s = fsize_m-2
fsize_l = fsize_m+2

qgray       = "#768E95"
qblue       = "#4283A9"
qgreen      = "#62B4A9"
qred        = "#E6767A"
qturq       = "#2EC0D1"
qmagenta    = "#9A607F"
qyellow     = "#EBB434"
qgray_dark  = "#465559"
qblue_dark  = "#274e65"
qgreen_dark = "#3a6c65"
qred_dark   = "#b85e61"
qturq_dark  = "#2499a7"
qmagenta_dark = "#4d303f"
qyellow_dark  = "#a47d24"
qgray_light  = "#acbbbf"
qblue_light  = "#8db4cb"
qgreen_light = "#a0d2cb"
qred_light   = "#eb9194"
qturq_light  = "#57ccda"
qmagenta_light = "#c29fb2"
qyellow_light = "#f1ca70"
greys   = sns.color_palette("Greys", 7)
blues   = sns.color_palette("Blues", 7)
reds    = sns.color_palette("Reds", 7)
greens  = sns.color_palette("Greens", 7)
purples = sns.color_palette("Purples", 7)

params = {'text.usetex': False, 'mathtext.fontset': 'stixsans'}
plt.rcParams.update(params)

def find_nearest(array, value):
    array   = np.asarray(array)
    idx     = (np.abs(array - value)).argmin()
    return array[idx], idx

def find_nearest_idx(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx

# 2nd y-axis: Al-26 from tform (relartive to CAI initial)
def transform_tform_to_al26(t):
    # https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.log.html
    # t = -1.0344*np.log(Al)
    # return [ "%.2f" % z for z in t ]
    Al = 5.25*np.exp(-t/1.03)
    Al = Al/5.25 # normalise to CAIs
    return [ "%.2f" % z for z in Al ]
# Test:
# tform_list  = np.array(natsorted(set(tform)))
# Al26_init   = transform_tform_to_al26(tform_list)
# print(tform_list)
# print(Al26_init)