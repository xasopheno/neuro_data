import os
import pandas as pd
import json
import mne
import numpy as np
import scipy.stats as stats
from matplotlib import pyplot
import matplotlib.pyplot as plt
import matplotlib.pyplot
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 20)

subject = "f1exphe7"

raw = mne.io.read_raw_fif(f"ds003703-download/sub-{subject}/meg/sub-{subject}_task-rest_run-01_meg.fif")
print(raw)
print(raw.info)

ica = mne.preprocessing.ICA(n_components=20, random_state=97, max_iter=800)
ica.fit(raw)
ica.exclude = [1, 2]  # details on how we picked these are omitted here

#  # set up and fit the ICA
#  ica = mne.preprocessing.ICA(n_components=306, random_state=97, max_iter=800)
#  ica.fit(raw)
#  ica.exclude = [1, 2]  # details on how we picked these are omitted here
print(raw.ch_names)
orig_raw = raw.copy()
raw.load_data()
ica.apply(raw)

chs = ['MEG0111', 'MEG0121', 'MEG0131', 'MEG0211', 'MEG0221', 
        'MEG0231', 'MEG0311', 'MEG0321', 'MEG0331', 'MEG1511', 'MEG1521', 'MEG1531']

for ch in chs:
    a = str(ch)
    m = np.array(raw[a][0])
    np.savetxt('output/' + "sample_audvis_filt-0-40_raw_chanel_" + a + "_array_0.csv", m, delimiter=",")
