import os
from pathlib import Path
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

subjects = [
    "a68d5xp5",
    #  "aoiyzwiy",
    #  "b2scmyvu",
    #  "bszjeu9t",
    #  "cybu8sao",
    #  "d85ay07w",
    #  "dvpmnk0o",
    #  "efhumn1s",
    #  "f1exphe7",
    #  "fa7dlyiy",
    #  "h01ew7gu",
    #  "ja50o035",
    #  "on3kplto",
    #  "opwvtd9h",
    #  "pgdrzql6",
    #  "phepjqh5",
    #  "q9zk9d60",
    #  "qox2w7zs",
    #  "qu5g9dgl",
    #  "qyxt7aso",
    #  "rrp3kgd0",
    #  "rvdodovm",
    #  "soshxei0",
    #  "thkr6bpz",
    #  "ubtkiuvp",
    #  "um0bvhu4",
    #  "ur5xvo5v",
    #  "vui8ua9x",
    #  "wi1lmhbs",
    #  "wxki41ba",
    #  "y6ykwq70",
    #  "yi3hkj7g",
    #  "zn6x1no3",
    #  "zzb3eyyq",
]

#  subject = "f1exphe7"
for subject in subjects: 
    raw = mne.io.read_raw_fif(f"ds003703-download/sub-{subject}/meg/sub-{subject}_task-rest_run-01_meg.fif")
    print(raw)
    print(raw.info)

    #  ica = mne.preprocessing.ICA(n_components=20, random_state=97, max_iter=800)
    #  ica.fit(raw)
    #  ica.exclude = [1, 2]  # details on how we picked these are omitted here

    print(raw.ch_names)
    #  orig_raw = raw.copy()
    #  raw.load_data()
    #  ica.apply(raw)

    chs = [
        'MEG0111', 'MEG0121', 'MEG0131', 
        'MEG0211', 'MEG0221', 'MEG0231', 
        'MEG0311', 'MEG0321', 'MEG0331', 
        'MEG1511', 'MEG1521', 'MEG1531'
    ]

    #  output_dir = f"output/{subject}"

    #  Path(output_dir).mkdir(parents=True, exist_ok=True) 

    #  for ch in chs:
        #  channel = str(ch)
        #  m = np.array(raw[channel][0])
        #  np.savetxt(f"{output_dir}/{channel.lower()}.csv", m, delimiter=",")
