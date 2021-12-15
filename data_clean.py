import os
from pathlib import Path

datadir = Path("./output/")
for file in datadir.glob('*.csv'):
    print(file)
    short = file.name.split("_chanel_")[1]
    short = short.split("_array_")[0]
    short = "_".join(short.split(" ")).lower()
    short = short + ".csv"
    filename = f"{datadir.name}/{file.name}"
    print(short)
    os.rename(filename, short)
