# Index a file from dataset

import numpy as np
from calc_shots import calc_shotlist

# build inverted index
def build_invind(filename, shot_list):
    indexfilename = "index/" + filename.split("/")[-1].split(".")[0] + "_ind.txt"
    
    index = {}
    lines = []
    for start, length in shot_list:
        if length not in index:
            index[length] = list()
        index[length].append(start)
    
    for key in index.keys():
        line = str(key) + ":" + ",".join(str(start) for start in index[key]) + "\n"
        lines.append(line)
    
    f = open(indexfilename, "w")
    f.writelines(lines)
    f.close()


if __name__ == "__main__":
    filename = 'dataset/Videos/video6.mp4'

    # calculate and save shot list
    shot_list = calc_shotlist(filename)
    outfilename = "index/" + filename.split("/")[-1].split(".")[0] + "_list.csv"
    np.savetxt(outfilename, shot_list, delimiter=",", fmt="%d")

    # build inverse index
    build_invind(filename, shot_list)
