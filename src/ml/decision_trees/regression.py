"""Decision Tree regression from scratch.

The idea is the same as decision tree classifiers: We recursively split the dataset
until we are left with pure leaf nodes. The two main differences are how we define
impurity and how we make predictions.

To make a prediction, we average the values of the data points when we arrive at a leaf
node during the tree traversal process.

To split the dataset, we have to find the split that decreases the impurities of the
child nodes the most. In the context of regression, we use variance reduction as a
measure of impurity. A higher value of variance means a higher impurity (and vice
versa). Variance reduction is computed by subtracting the combined variances of the
child nodes from the variance of the parent node. The weights of the child nodes are the
relative size of the child nodes w.r.t the parent node.
"""

# type: ignore

# Third Party Library
import numpy as np
import pandas as pd

from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Get the data
data = pd.read_csv(
    "~/Projects/personal/coding_practice/src/ml/decision_trees/airfoil_noise_data.csv",
)
print(data.head(5))
print()


# Node class
class Node:
    def __init__(
        self,
        feature_index=None,
        feature_value=None,
        left=None,
        right=None,
        var_red=None,
        value=None,
    ):
        # For decision nodes.
        self.feature_index = feature_index
        self.feature_value = feature_value
        self.left = left
        self.right = right
        self.var_red = var_red

        # For leaf nodes.
        self.value = value


# Tree class
class DecisionTreeRegressor:
    def __init__(self, min_samples_split=2, max_depth=2):
        self.min_samples_split = min_samples_split
        self.max_depth = max_depth
        self.root = None

    def build_tree(self, dataset, curr_depth=0):
        X, Y = dataset[:, :-1], dataset[:, -1]
        num_samples, num_features = np.shape(X)
        if num_samples >= self.min_samples_split and curr_depth <= self.max_depth:
            best_split = self.get_best_split(dataset, num_features)
            if best_split["var_red"] > 0:
                left = self.build_tree(best_split["left"], curr_depth + 1)
                right = self.build_tree(best_split["right"], curr_depth + 1)
                return Node(
                    best_split["feature_index"],
                    best_split["feature_value"],
                    left,
                    right,
                    best_split["var_red"],
                )
        return Node(value=self.compute_leaf_value(Y))

    @staticmethod
    def compute_leaf_value(Y):
        return np.mean(Y)

    def fit(self, X, Y):
        dataset = np.concatenate((X, Y), axis=1)
        self.root = self.build_tree(dataset)

    def get_best_split(self, dataset, num_features):
        best_split, max_var_red = {}, -float("inf")
        for feature_index in range(num_features):
            for feature_value in np.unique(dataset[:, feature_index]):
                left, right = self.split(dataset, feature_index, feature_value)
                if len(left) > 0 and len(right) > 0:
                    var_red = self.var_red(dataset[:, -1], left[:, -1], right[:, -1])
                    if var_red > max_var_red:
                        best_split["feature_index"] = feature_index
                        best_split["feature_value"] = feature_value
                        best_split["left"] = left
                        best_split["right"] = right
                        best_split["var_red"] = var_red
                        max_var_red = var_red
        return best_split

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
                tree.var_red,
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

    @staticmethod
    def var_red(parent, l_child, r_child):
        weight_l, weight_r = len(l_child) / len(parent), len(r_child) / len(parent)
        return np.var(parent) - (
            weight_l * np.var(l_child) + weight_r * np.var(r_child)
        )


# Train-Test split
X = data.iloc[:, :-1].values
Y = data.iloc[:, -1].values.reshape(-1, 1)
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=41
)

# Fit the model
regressor = DecisionTreeRegressor(min_samples_split=3, max_depth=3)
regressor.fit(X_train, Y_train)
regressor.print_tree()

# Test the model
Y_pred = regressor.predict(X_test)
print(np.sqrt(mean_squared_error(Y_test, Y_pred)))
