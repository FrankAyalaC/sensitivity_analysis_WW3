import numpy as np
import datetime as dt
import xarray as xr
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import matplotlib.dates as mdates
import matplotlib as mpl
import pandas as pd
import os
from datetime import datetime,timedelta
import glob as glob
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.dates import DateFormatter

a=np.load('sw3_spec.npz',allow_pickle=True)
print(a['arr_0'])