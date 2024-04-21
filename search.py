# Search index with query video

from calc_shots import calcShots

if __name__ == "__main__":
    filename = "dataset/Queries/video_6_1_filtered.mp4"
    
    shot_list = calcShots(filename)

    print(shot_list)
