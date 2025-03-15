"""
Author: Isaac Watts
Description: Plot hand_tracking_data csv files in Matplotlib figures
"""
import matplotlib.pyplot as plt
import numpy as np

# function to plot hand joints for each of the hands
def plot_joints(finger_points : list[list]):
    for i in range(0, len(finger_points)):
        if i > 0:
            ax.plot([finger_points[i - 1][0], finger_points[i][0]], [finger_points[i - 1][1], finger_points[i][1]], [finger_points[i - 1][2], finger_points[i][2]], color="purple")
        ax.scatter(finger_points[i][0], finger_points[i][1], finger_points[i][2], c='purple')

entries = np.genfromtxt(r"C:\Users\isaac\OneDrive\Documents\plot_oculus_hands\data\hand_tracking_data.csv", delimiter=',', names=True, dtype=None, encoding='utf-8')

# get column names in a dictionary with the arrays as the value
columns = {name: entries[name] for name in entries.dtype.names}

# Palm
Palm_X = columns["Palm_X"]
Palm_Y = columns["Palm_Y"]
Palm_Z = columns["Palm_Z"]


# Wrist (origin point of all the hand joins)
wrist_X = columns["Wrist_X"]
wrist_Y = columns["Wrist_Y"]
wrist_Z = columns["Wrist_Z"]

# Index finger
IndexMetacarpal_X = columns["IndexMetacarpal_X"] 
IndexMetacarpal_Y = columns["IndexMetacarpal_Y"]
IndexMetacarpal_Z = columns["IndexMetacarpal_Z"]
IndexProximal_X = columns["IndexProximal_X"]
IndexProximal_Y = columns["IndexProximal_Y"]
IndexProximal_Z = columns["IndexProximal_Z"]
IndexIntermediate_X = columns["IndexIntermediate_X"]
IndexIntermediate_Y = columns["IndexIntermediate_Y"]
IndexIntermediate_Z = columns["IndexIntermediate_Z"]
IndexDistal_X = columns["IndexDistal_X"]
IndexDistal_Y = columns["IndexDistal_Y"]
IndexDistal_Z = columns["IndexDistal_Z"]
IndexTip_X = columns["IndexTip_X"]
IndexTip_Y = columns["IndexTip_Y"]
IndexTip_Z = columns["IndexTip_Z"]

# Middle Finger
MiddleMetacarpal_X = columns["MiddleMetacarpal_X"]
MiddleMetacarpal_Y = columns["MiddleMetacarpal_Y"]
MiddleMetacarpal_Z = columns["MiddleMetacarpal_Z"]
MiddleProximal_X = columns["MiddleProximal_X"]
MiddleProximal_Y = columns["MiddleProximal_Y"]
MiddleProximal_Z = columns["MiddleProximal_Z"]
MiddleIntermediate_X = columns["MiddleIntermediate_X"]
MiddleIntermediate_Y = columns["MiddleIntermediate_Y"]
MiddleIntermediate_Z = columns["MiddleIntermediate_Z"]
MiddleDistal_X = columns["MiddleDistal_X"]
MiddleDistal_Y = columns["MiddleDistal_Y"]
MiddleDistal_Z = columns["MiddleDistal_Z"]
MiddleTip_X = columns["MiddleTip_X"]
MiddleTip_Y = columns["MiddleTip_Y"]
MiddleTip_Z = columns["MiddleTip_Z"]


# Ring finger
RingMetacarpal_X = columns["RingMetacarpal_X"]
RingMetacarpal_Y = columns["RingMetacarpal_Y"]
RingMetacarpal_Z = columns["RingMetacarpal_Z"]
RingProximal_X = columns["RingProximal_X"]
RingProximal_Y = columns["RingProximal_Y"]
RingProximal_Z = columns["RingProximal_Z"]
RingIntermediate_X = columns["RingIntermediate_X"]
RingIntermediate_Y = columns["RingIntermediate_Y"]
RingIntermediate_Z = columns["RingIntermediate_Z"]
RingDistal_X = columns["RingDistal_X"]
RingDistal_Y = columns["RingDistal_Y"]
RingDistal_Z = columns["RingDistal_Z"]
RingTip_X = columns["RingTip_X"]
RingTip_Y = columns["RingTip_Y"]
RingTip_Z = columns["RingTip_Z"]

# Little finger 
LittleMetacarpal_X = columns["LittleMetacarpal_X"]
LittleMetacarpal_Y = columns["LittleMetacarpal_Y"]
LittleMetacarpal_Z = columns["LittleMetacarpal_Z"]
LittleProximal_X = columns["LittleProximal_X"]
LittleProximal_Y = columns["LittleProximal_Y"]
LittleProximal_Z = columns["LittleProximal_Z"]
LittleIntermediate_X = columns["LittleIntermediate_X"]
LittleIntermediate_Y = columns["LittleIntermediate_Y"]
LittleIntermediate_Z = columns["LittleIntermediate_Z"]
LittleDistal_X = columns["LittleDistal_X"]
LittleDistal_Y = columns["LittleDistal_Y"]
LittleDistal_Z = columns["LittleDistal_Z"]
LittleTip_X = columns["LittleTip_X"]
LittleTip_Y = columns["LittleTip_Y"]
LittleTip_Z = columns["LittleTip_Z"]

# Thumb
ThumbMetacarpal_X = columns["ThumbMetacarpal_X"]
ThumbMetacarpal_Y = columns["ThumbMetacarpal_Y"]
ThumbMetacarpal_Z = columns["ThumbMetacarpal_Z"]
ThumbProximal_X = columns["ThumbProximal_X"]
ThumbProximal_Y = columns["ThumbProximal_Y"]
ThumbProximal_Z = columns["ThumbProximal_Z"]
ThumbDistal_X = columns["ThumbDistal_X"]
ThumbDistal_Y = columns["ThumbDistal_Y"]
ThumbDistal_Z = columns["ThumbDistal_Z"]
ThumbTip_X = columns["ThumbTip_X"]
ThumbTip_Y = columns["ThumbTip_Y"]
ThumbTip_Z = columns["ThumbTip_Z"]


n = len(entries)
if __name__ == '__main__':
    for i in range(n):
        index = [[wrist_X[i], wrist_Y[i], wrist_Z[i] ], 
                      [IndexMetacarpal_X[i], IndexMetacarpal_Y[i], IndexMetacarpal_Z[i]], 
                      [IndexProximal_X[i], IndexProximal_Y[i], IndexProximal_Z[i]],
                      [IndexIntermediate_X[i], IndexIntermediate_Y[i], IndexIntermediate_Z[i]], 
                    [IndexDistal_X[i], IndexDistal_Y[i], IndexDistal_Z[i]],
                    [IndexTip_X[i], IndexTip_Y[i], IndexTip_Z[i]]]

        middle = [[wrist_X[i], wrist_Y[i], wrist_Z[i] ], 
                      [MiddleMetacarpal_X[i], MiddleMetacarpal_Y[i], MiddleMetacarpal_Z[i]],
                      [Palm_X[i], Palm_Y[i], Palm_Z[i]], 
                      [MiddleProximal_X[i], MiddleProximal_Y[i], MiddleProximal_Z[i]],
                      [MiddleIntermediate_X[i], MiddleIntermediate_Y[i], MiddleIntermediate_Z[i]], 
                    [MiddleDistal_X[i], MiddleDistal_Y[i], MiddleDistal_Z[i]],
                    [MiddleTip_X[i], MiddleTip_Y[i], MiddleTip_Z[i]]]
        
        ring = [[wrist_X[i], wrist_Y[i], wrist_Z[i] ], 
                      [RingMetacarpal_X[i], RingMetacarpal_Y[i], RingMetacarpal_Z[i]], 
                      [RingProximal_X[i], RingProximal_Y[i], RingProximal_Z[i]],
                      [RingIntermediate_X[i], RingIntermediate_Y[i], RingIntermediate_Z[i]], 
                    [RingDistal_X[i], RingDistal_Y[i], RingDistal_Z[i]],
                    [RingTip_X[i], RingTip_Y[i], RingTip_Z[i]]]
        pinkie = [[wrist_X[i], wrist_Y[i], wrist_Z[i] ], 
                      [LittleMetacarpal_X[i], LittleMetacarpal_Y[i], LittleMetacarpal_Z[i]], 
                      [LittleProximal_X[i], LittleProximal_Y[i], LittleProximal_Z[i]],
                      [LittleIntermediate_X[i], LittleIntermediate_Y[i], LittleIntermediate_Z[i]], 
                    [LittleDistal_X[i], LittleDistal_Y[i], LittleDistal_Z[i]],
                    [LittleTip_X[i], LittleTip_Y[i], LittleTip_Z[i]]]
        thumb = [[wrist_X[i], wrist_Y[i], wrist_Z[i] ], 
                      [ThumbMetacarpal_X[i], ThumbMetacarpal_Y[i], ThumbMetacarpal_Z[i]], 
                      [ThumbProximal_X[i], ThumbProximal_Y[i], ThumbProximal_Z[i]],
                    [ThumbDistal_X[i], ThumbDistal_Y[i], ThumbDistal_Z[i]],
                    [ThumbTip_X[i], ThumbTip_Y[i], ThumbTip_Z[i]]]
        




        fig = plt.figure()
        # plt.title(f"Iteration {i} for left (green) and right hand(purple)")
        ax = fig.add_subplot(111, projection='3d')

        plot_joints(index)
        plot_joints(middle)
        plot_joints(ring)    
        plot_joints(pinkie)
        plot_joints(thumb)
        

        # Set labels for the axes
        ax.set_xlabel('X Axis')
        ax.set_ylabel('Y Axis')
        ax.set_zlabel('Z Axis')

        plt.savefig(f"images/hand{i}.png")

        plt.close()


        # plt.show()