"""Decision Tree regression from scratch.

A decision tree is a binary tree that recursively splits a dataset until we are left
with pure leaf nodes; i.e., a data point with only one type of class label. Decision
trees are nonlinear classifiers.

There are two kinds of nodes: decision nodes and leaf nodes. Decision nodes contain a
condition to split the data. Leaf nodes helps us to decide the class of a new data
point. If a leaf node is not pure (i.e., it contains more than one class type), we
perform majority voting to determine the class label of the new data point.

There are many possible splitting conditions at each decision node. The decision tree
model should always choose the split that maximizes the information gain. To calculate
the information gain, we need to understand the information contained in a state. We can
use two metrics to determine the optimal split at each decision node: entropy and Gini
index.

Entropy/Gini index is a measure of the information contained in a state. If the
entropy is high, then we are very uncertain about the state and need more bits to
describe the state (and vice versa).

To find the information gain of a split, we subtract the sum of the entropies of the
child nodes from the entropy of the parent node. The split that provides the highest
information gain is chosen as the optimal split for each decision node. We iterate
through all possible splits of the dataset to determine the optimal splits for the
decision tree. In other words, the model iterates through all the features and feature
values to find the optimal split and split threshold in a greedy fashion---it does not
backtrack and change a previous optimal split. Thus, decision trees do not guarantee a
global optimal split but is fast.

Decision trees typically have two stopping conditions: 1. the minimum number of samples
to split on and 2. the maximum depth of the tree. If the number of samples at a node is
less than the minimum number of samples to split on, then we stop the splitting process.
Likewise, if we have reached the maximum depth of tree, we stop the splitting process.
"""

# type: ignore

# Standard Library
from collections import Counter

# Third Party Library
import numpy as np
import pandas as pd

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Get the data
col_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "type"]
data = pd.read_csv(
    "~/Projects/personal/coding_practice/src/ml/decision_trees/iris.csv",
    skiprows=0,
    header=None,
    names=col_names,
)
print(data.head(10))
print()


# Node class
class Node:
    def __init__(
        self,
        feature_index=None,
        feature_value=None,
        left=None,
        right=None,
        info_gain=None,
        value=None,
    ):
        # For decision nodes.
        self.feature_index = feature_index
        self.feature_value = feature_value
        self.left = left
        self.right = right
        self.info_gain = info_gain

        # For leaf nodes.
        self.value = value


# Tree class
class DecisionTreeClassifier:
    def __init__(self, min_samples_split=2, max_depth=2):
        self.min_samples_split = min_samples_split
        self.max_depth = max_depth
        self.root = None

    def build_tree(self, dataset, curr_depth=0):
        X, Y = dataset[:, :-1], dataset[:, -1]
        num_samples, num_features = np.shape(X)
        if num_samples >= self.min_samples_split and curr_depth <= self.max_depth:
            best_split = self.get_best_split(dataset, num_features)
            if best_split["info_gain"] > 0:
                left = self.build_tree(best_split["left"], curr_depth + 1)
                right = self.build_tree(best_split["right"], curr_depth + 1)
                return Node(
                    best_split["feature_index"],
                    best_split["feature_value"],
                    left,
                    right,
                    best_split["info_gain"],
                )
        return Node(value=self.compute_leaf_value(Y))

    @staticmethod
    def compute_leaf_value(Y):
        Y = list(Y)
        return max(Y, key=Y.count)

    @staticmethod
    def compute_probability(y):
        return {num: freq / len(y) for num, freq in Counter(y).items()}

    def entropy(self, y):
        probs = self.compute_probability(y)
        return sum(-probs[num] * np.log2(probs[num]) for num in probs)

    def fit(self, X, Y):
        dataset = np.concatenate((X, Y), axis=1)
        self.root = self.build_tree(dataset)

    def get_best_split(self, dataset, num_features):
        best_split, max_info_gain = {}, -float("inf")
        for feature_index in range(num_features):
            for feature_value in np.unique(dataset[:, feature_index]):
                left, right = self.split(dataset, feature_index, feature_value)
                if len(left) > 0 and len(right) > 0:
                    info_gain = self.information_gain(
                        dataset[:, -1], left[:, -1], right[:, -1]
                    )
                    if info_gain > max_info_gain:
                        best_split["feature_index"] = feature_index
                        best_split["feature_value"] = feature_value
                        best_split["left"] = left
                        best_split["right"] = right
                        best_split["info_gain"] = info_gain
                        max_info_gain = info_gain
        return best_split

    def gini_index(self, y):
        probs = self.compute_probability(y)
        return 1 - sum(probs[num] ** 2 for num in probs)

    def information_gain(self, parent, l_child, r_child, mode="gini"):
        weight_l, weight_r = len(l_child) / len(parent), len(r_child) / len(parent)
        if mode == "gini":
            gain = self.gini_index(parent) - (
                weight_l * self.gini_index(l_child)
                + weight_r * self.gini_index(r_child)
            )
        else:
            gain = self.entropy(parent) - (
                weight_l * self.entropy(l_child) + weight_r * self.entropy(r_child)
            )
        return gain

    def predict(self, X):
        preds = []
        for x in X:
            tree = self.root
            while tree:
                if tree.value:
                    preds.append(tree.value)
                    break
                feature_value = x[tree.feature_index]
                tree = tree.left if feature_value <= tree.feature_value else tree.right
        return preds

    def print_tree(self, tree=None, indent=" "):
        tree = tree or self.root
        if tree.value:
            print(tree.value)
        else:
            print(
                "X_" + str(tree.feature_index),
                "<=",
                tree.feature_value,
                "?",
                tree.info_gain,
            )
            print("%sleft:" % indent, end="")
            self.print_tree(tree.left, indent + indent)
            print("%sright:" % indent, end="")
            self.print_tree(tree.right, indent + indent)

    @staticmethod
    def split(dataset, feature_index, feature_value):
        left = np.array([row for row in dataset if row[feature_index] <= feature_value])
        right = np.array([row for row in dataset if row[feature_index] > feature_value])
        return left, right


# Train-Test split
X = data.iloc[:, :-1].values
Y = data.iloc[:, -1].values.reshape(-1, 1)
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=41
)

# Fit the model
classifier = DecisionTreeClassifier(min_samples_split=3, max_depth=3)
classifier.fit(X_train, Y_train)
classifier.print_tree()

# Test the model
Y_pred = classifier.predict(X_test)
print(accuracy_score(Y_test, Y_pred))
