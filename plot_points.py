"""
Author: Isaac Watts
Description: Plot hand_tracking_data csv files in Matplotlib figures
"""
import matplotlib.pyplot as plt
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



entries = read_csv_file("hand_tracking_data.csv")
x_left = []
y_left = []
z_left = []
left_labels = []


x_right = []
y_right = []
z_right = []
right_labels = []

for entry in entries[1::]:
    if entry[1] == "Left":
        x_left.append(float(entry[-3]))
        y_left.append(float(entry[-2]))
        z_left.append(float(entry[-1]))
        left_labels.append(entry[2])
    elif entry[1] == "Right":
        x_right.append(float(entry[-3]))
        y_right.append(float(entry[-2]))
        z_right.append(float(entry[-1]))
        right_labels.append(entry[2])

# each entry has 26 for left and right hands
# make each hand iter a figure
left_hand_iterations = dict()
right_hand_iterations = dict()
n = len(x_left)//26

for i in range(0, n):
    left_hand_iterations[i] = {
        "x_left" : x_left[i * 26: i * 26 + 26],
        "y_left" : y_left[i * 26: i * 26 + 26],
        "z_left" : z_left[i * 26: i * 26 + 26],
        "left_labels" : left_labels[i * 26: i * 26 + 26],
    }
    right_hand_iterations[i] = {
        "x_right" : x_right[i * 26: i * 26 + 26],
        "y_right" : y_right[i * 26: i * 26 + 26],
        "z_right" : z_right[i * 26: i * 26 + 26],
        "right_labels" : right_labels[i * 26: i * 26 + 26],
    }
    # print(f"The length of iter {i} is {len(left_hand_iterations[i]["x_left"])}")
    
for i in range(0, n):
    # Create a figure and a 3D axes object
    x_left = left_hand_iterations[i]["x_left"]
    y_left = left_hand_iterations[i]["y_left"]
    z_left = left_hand_iterations[i]["z_left"]
    left_labels = left_hand_iterations[i]["left_labels"]

    x_right = right_hand_iterations[i]["x_right"]
    y_right = right_hand_iterations[i]["y_right"]
    z_right = right_hand_iterations[i]["z_right"]
    right_labels = right_hand_iterations[i]["right_labels"]

    fig = plt.figure()
    plt.title(f"Iteration {i} for left (green) and right hand(purple)")
    ax = fig.add_subplot(111, projection='3d')

    # Plot the points
    ax.scatter(x_left, y_left, z_left, c='g', marker='o')
    ax.scatter(x_right, y_right, z_right, c='purple', marker='o')

    # create left hand
    left_hand = hand()
    left_hand.insert_to_hand(left_labels, x_left, y_left, z_left)
    thumbs_left = left_hand.thumbs
    index_left = left_hand.index
    middle_left = left_hand.middle
    ring_left = left_hand.ring
    pinkie_left = left_hand.pinkie


    # create right hand
    right_hand = hand()
    right_hand.insert_to_hand(right_labels, x_right, y_right, z_right)
    thumbs_right = right_hand.thumbs
    index_right = right_hand.index
    middle_right = right_hand.middle
    ring_right = right_hand.ring
    pinkie_right = right_hand.pinkie


    # plot left hand
    for i in range(1, len(thumbs_left)):
        ax.plot([thumbs_left[i - 1][0], thumbs_left[i][0]], [thumbs_left[i - 1][1], thumbs_left[i][1]], [thumbs_left[i - 1][2], thumbs_left[i][2]], color="green")

    for i in range(1, len(index_left)):
        ax.plot([index_left[i - 1][0], index_left[i][0]], [index_left[i - 1][1], index_left[i][1]], [index_left[i - 1][2], index_left[i][2]], color="green")

    for i in range(1, len(middle_left)):
        ax.plot([middle_left[i - 1][0], middle_left[i][0]], [middle_left[i - 1][1], middle_left[i][1]], [middle_left[i - 1][2], middle_left[i][2]], color="green")

    for i in range(1, len(ring_left)):
        ax.plot([ring_left[i - 1][0], ring_left[i][0]], [ring_left[i - 1][1], ring_left[i][1]], [ring_left[i - 1][2], ring_left[i][2]], color="green")

    for i in range(1, len(pinkie_left)):
        ax.plot([pinkie_left[i - 1][0], pinkie_left[i][0]], [pinkie_left[i - 1][1], pinkie_left[i][1]], [pinkie_left[i - 1][2], pinkie_left[i][2]], color="green")


    # plot right hand
    for i in range(1, len(thumbs_right)):
        ax.plot([thumbs_right[i - 1][0], thumbs_right[i][0]], [thumbs_right[i - 1][1], thumbs_right[i][1]], [thumbs_right[i - 1][2], thumbs_right[i][2]], color="purple")

    for i in range(1, len(index_right)):
        ax.plot([index_right[i - 1][0], index_right[i][0]], [index_right[i - 1][1], index_right[i][1]], [index_right[i - 1][2], index_right[i][2]], color="purple")

    for i in range(1, len(middle_right)):
        ax.plot([middle_right[i - 1][0], middle_right[i][0]], [middle_right[i - 1][1], middle_right[i][1]], [middle_right[i - 1][2], middle_right[i][2]], color="purple")

    for i in range(1, len(ring_right)):
        ax.plot([ring_right[i - 1][0], ring_right[i][0]], [ring_right[i - 1][1], ring_right[i][1]], [ring_right[i - 1][2], ring_right[i][2]], color="purple")

    for i in range(1, len(pinkie_right)):
        ax.plot([pinkie_right[i - 1][0], pinkie_right[i][0]], [pinkie_right[i - 1][1], pinkie_right[i][1]], [pinkie_right[i - 1][2], pinkie_right[i][2]], color="purple")


    # Set labels for the axes
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')

    plt.show()