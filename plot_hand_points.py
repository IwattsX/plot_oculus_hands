"""
Author: Isaac Watts
Description: Plot hand_tracking_data csv files in Matplotlib figures
"""
import matplotlib.pyplot as plt
import numpy as np
import csv 
import re
# from mpl_toolkits.mplot3d import Axes3D

class hand():
    def __init__(self):
        self.thumbs = []
        self.index = []
        self.middle = []
        self.ring = []
        self.pinkie = []
    
    def insert_to_hand(self, labels, x, y, z):
        for i, label in enumerate(labels):
            if re.search("Thumb", label) is not None:
                self.thumbs.append([x[i], y[i], z[i], label])

            elif re.search("Wrist", label) is not None: # wrist is the origin append it to all list
                self.thumbs.append([x[i], y[i], z[i], label])
                self.index.append([x[i], y[i], z[i], label])
                self.middle.append([x[i], y[i], z[i], label])
                self.ring.append([x[i], y[i], z[i], label])
                self.pinkie.append([x[i], y[i], z[i], label])

            elif re.search("Palm", label) is not None:
                self.middle.append([x[i], y[i], z[i], label])

            elif re.search("Index", label) is not None:
                self.index.append([x[i], y[i], z[i], label])

            elif re.search("Middle", label) is not None:
                self.middle.append([x[i], y[i], z[i], label])

            elif re.search("Ring", label) is not None:
                self.ring.append([x[i], y[i], z[i], label])

            elif re.search("Little", label) is not None:
                self.pinkie.append([x[i], y[i], z[i], label])
        # swap palm and MiddleMetacarpal
        if len(self.middle) > 2:
            self.middle[1], self.middle[2] = self.middle[2], self.middle[1]

# Sample data points
def read_csv_file(file_path):
    """
    Reads a CSV file and prints its contents row by row.

    Args:
        file_path (str): The path to the CSV file.
    """
    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            res = []
            for row in csv_reader:
                res.append(row)
            return res
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except Exception as e:
         print(f"An error occurred: {e}")
         return None



entries = np.genfromtxt(r"C:\Users\isaac\OneDrive\Documents\plot_oculus_hands\data\hand_tracking_data.csv", delimiter=',', names=True, dtype=None, encoding='utf-8')

# get column names in a dictionary with the arrays as the value
columns = {name: entries[name] for name in entries.dtype.names}


wrist_X = columns["Wrist_X"]
wrist_Y = columns["Wrist_Y"]
wrist_Z = columns["Wrist_Z"]

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



n = len(wrist_X)    
if __name__ == '__main__':
    fig = plt.figure()
    # plt.title(f"Iteration {i} for left (green) and right hand(purple)")
    ax = fig.add_subplot(111, projection='3d')

    # plot the wrist
    ax.scatter(wrist_X[0], wrist_Y[0], wrist_Z[0])
    ax.text(wrist_X[0], wrist_Y[0], wrist_Z[0], 'Wrist')

    # plot the Little finger
    ax.scatter(LittleMetacarpal_X[0], LittleMetacarpal_Y[0], LittleMetacarpal_Z[0])
    ax.text(LittleMetacarpal_X[0], LittleMetacarpal_Y[0], LittleMetacarpal_Z[0], 'LittleMetacarpal')

    ax.scatter(LittleProximal_X[0], LittleProximal_Y[0], LittleProximal_Z[0])
    ax.text(LittleProximal_X[0], LittleProximal_Y[0], LittleProximal_Z[0], "LittleProximal")

    ax.scatter(LittleIntermediate_X[0], LittleIntermediate_Y[0], LittleIntermediate_Z[0])
    ax.text(LittleIntermediate_X[0], LittleIntermediate_Y[0], LittleIntermediate_Z[0], "LittleIntermediate")

    ax.scatter(LittleDistal_X[0], LittleDistal_Y[0], LittleDistal_Z[0])
    ax.text(LittleDistal_X[0], LittleDistal_Y[0], LittleDistal_Z[0], "LittleDistal")

    ax.scatter(LittleTip_X[0], LittleTip_Y[0], LittleTip_Z[0])
    ax.text(LittleTip_X[0], LittleTip_Y[0], LittleTip_Z[0], "LittleTip")

    
    

    # Set labels for the axes
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')

    plt.show()