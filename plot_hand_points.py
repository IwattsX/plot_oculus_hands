"""
Author: Isaac Watts
Description: Plot hand_tracking_data csv files in Matplotlib figures
"""
import matplotlib.pyplot as plt
import numpy as np

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

# make a vector
# make vectors based off of the order of joint values
index = [[wrist_X[0], wrist_Y[0], wrist_Z[0] ], 
                      [IndexMetacarpal_X[0], IndexMetacarpal_Y[0], IndexMetacarpal_Z[0]], 
                      [IndexProximal_X[0], IndexProximal_Y[0], IndexProximal_Z[0]],
                      [IndexIntermediate_X[0], IndexIntermediate_Y[0], IndexIntermediate_Z[0]], 
                    [IndexDistal_X[0], IndexDistal_Y[0], IndexDistal_Z[0]],
                    [IndexTip_X[0], IndexTip_Y[0], IndexTip_Z[0]]]



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


middle = [[wrist_X[0], wrist_Y[0], wrist_Z[0] ], 
                      [MiddleMetacarpal_X[0], MiddleMetacarpal_Y[0], MiddleMetacarpal_Z[0]],
                      [Palm_X[0], Palm_Y[0], Palm_Z[0]], 
                      [MiddleProximal_X[0], MiddleProximal_Y[0], MiddleProximal_Z[0]],
                      [MiddleIntermediate_X[0], MiddleIntermediate_Y[0], MiddleIntermediate_Z[0]], 
                    [MiddleDistal_X[0], MiddleDistal_Y[0], MiddleDistal_Z[0]],
                    [MiddleTip_X[0], MiddleTip_Y[0], MiddleTip_Z[0]]]

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

ring = [[wrist_X[0], wrist_Y[0], wrist_Z[0] ], 
                      [RingMetacarpal_X[0], RingMetacarpal_Y[0], RingMetacarpal_Z[0]], 
                      [RingProximal_X[0], RingProximal_Y[0], RingProximal_Z[0]],
                      [RingIntermediate_X[0], RingIntermediate_Y[0], RingIntermediate_Z[0]], 
                    [RingDistal_X[0], RingDistal_Y[0], RingDistal_Z[0]],
                    [RingTip_X[0], RingTip_Y[0], RingTip_Z[0]]]



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


# make vectors based off of the order of joint values
pinkie = [[wrist_X[0], wrist_Y[0], wrist_Z[0] ], 
                      [LittleMetacarpal_X[0], LittleMetacarpal_Y[0], LittleMetacarpal_Z[0]], 
                      [LittleProximal_X[0], LittleProximal_Y[0], LittleProximal_Z[0]],
                      [LittleIntermediate_X[0], LittleIntermediate_Y[0], LittleIntermediate_Z[0]], 
                    [LittleDistal_X[0], LittleDistal_Y[0], LittleDistal_Z[0]],
                    [LittleTip_X[0], LittleTip_Y[0], LittleTip_Z[0]]]

# TODO: Thumbs
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

thumb = [[wrist_X[0], wrist_Y[0], wrist_Z[0] ], 
                      [ThumbMetacarpal_X[0], ThumbMetacarpal_Y[0], ThumbMetacarpal_Z[0]], 
                      [ThumbProximal_X[0], ThumbProximal_Y[0], ThumbProximal_Z[0]],
                    [ThumbDistal_X[0], ThumbDistal_Y[0], ThumbDistal_Z[0]],
                    [ThumbTip_X[0], ThumbTip_Y[0], ThumbTip_Z[0]]]


n = len(wrist_X)    
if __name__ == '__main__':
    fig = plt.figure()
    # plt.title(f"Iteration {i} for left (green) and right hand(purple)")
    ax = fig.add_subplot(111, projection='3d')

    # plot the wrist
    ax.scatter(wrist_X[0], wrist_Y[0], wrist_Z[0])

    # plot the index finger
    for i in range(0, len(index)):
        if i > 0:
            ax.plot([index[i - 1][0], index[i][0]], [index[i - 1][1], index[i][1]], [index[i - 1][2], index[i][2]], color="purple")
        ax.scatter(index[i][0], index[i][1], index[i][2], c='purple')
    
    # plot the middle finger
    for i in range(0, len(middle)):
        if i > 0:
            ax.plot([middle[i - 1][0], middle[i][0]], [middle[i - 1][1], middle[i][1]], [middle[i - 1][2], middle[i][2]], color="purple")
        ax.scatter(middle[i][0], middle[i][1], middle[i][2], c='purple')
    # plot the ring finger
    for i in range(0, len(ring)):
        if i > 0:
            ax.plot([ring[i - 1][0], ring[i][0]], [ring[i - 1][1], ring[i][1]], [ring[i - 1][2], ring[i][2]], color="purple")
        ax.scatter(ring[i][0], ring[i][1], ring[i][2], c='purple')

    # plot the pinkie finger    
    for i in range(0, len(pinkie)):
        if i > 0:
            ax.plot([pinkie[i - 1][0], pinkie[i][0]], [pinkie[i - 1][1], pinkie[i][1]], [pinkie[i - 1][2], pinkie[i][2]], color="purple")
        ax.scatter(pinkie[i][0], pinkie[i][1], pinkie[i][2], c='purple')

    # plot the thumb
    for i in range(0, len(thumb)):
        if i > 0:
            ax.plot([thumb[i - 1][0], thumb[i][0]], [thumb[i - 1][1], thumb[i][1]], [thumb[i - 1][2], thumb[i][2]], color="purple")
        ax.scatter(thumb[i][0], thumb[i][1], thumb[i][2], c='purple')
    # Set labels for the axes
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')

    plt.show()