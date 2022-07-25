"""Naive Bayesian classification from scratch.

Bayesian classification deals with conditional probabilities. Naive Bayesian
classification deals with joint probabilities.

The Bayesian classification problem is as follows:

Given features X = (x_1, x_2, ..., x_n), we want to find the correct label: Y.

From a probabilistic point of view, we consider X and Y as random variables and the
problem is to find the maximum of the following expression for all values of Y:

For which value of y is

P(Y = y|X = (x_1, x_2, ..., x_n))

maximized?

P(Y|X) = P(X|Y) * P(Y) / P(X)

P(Y|X): posterior probability
P(X|Y): likelihood
P(Y): prior probability
P(X): evidence

Typically, we can ignore P(X) since it remains the same for all values of Y.

In Bayesian classification, we do NOT assume that the features in X are independent.
This leads to issues when computing P(X|Y) since it becomes less and less likely for the
likelihood to be non-zero as the number of features in X increases (the chances of a
data point containing the exact combination of 50 features is much smaller than the
chances of a dataset containing the exact combination of 2 features).

Thus, we make the assumption that the individual features of X are independent. This is
Naive Bayesian classification. Due to this assumption, we don't have to find the exact
combination of all the features of X in the dataset. We can write the likelihood as a
product of probabilities instead:

P(X = (0, 2)|Y = 1) = P(x_1 = 0|Y = 1) * P(x_2 = 2|Y = 1)
P(X = (0, 2)|Y = 0) = P(x_1 = 0|Y = 0) * P(x_2 = 2|Y = 0)

Dealing with Continuous Features
--------------------------------

1. Discretization
2. Fit a known distribution to the dataset (e.g., a normal distribution)

Why Naive Bayes is Naive
------------------------

Naive Bayes does not take the word order into account when calculating probabilities
(i.e., it assumes bag-of-words).
"""

# Third Party Library
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from sklearn.metrics import confusion_matrix, f1_score
from sklearn.model_selection import train_test_split

sns.set_style("darkgrid")

# Dataset
data = pd.read_csv(
    "~/Projects/personal/coding_practice/src/ml/bayesian_classifiers/Breast_cancer_data.csv"  # noqa: E501
)
print(data.head(10))
print()

# Basic EDA
#
# This shows that there are more positive examples than negative ones. Thus, the dataset
# is slightly imbalanced.
data["diagnosis"].hist()
# plt.show()

# To apply Naive Bayesian algorithm, the features must be independent of one another.
# The heatmap shows that radius, area, and perimeter are highly correlated. Thus, we
# just take the radius feature and ignore the area and perimeter features from the
# dataset.
corr = data.iloc[:, :-1].corr(method="pearson")
cmap = sns.diverging_palette(250, 354, 80, 60, center="dark", as_cmap=True)
sns.heatmap(corr, vmax=1, vmin=-0.5, cmap=cmap, square=True, linewidths=0.2)
# plt.show()

data = data[["mean_radius", "mean_texture", "mean_smoothness", "diagnosis"]]
print(data.head(10))
print()

# Since the dataset features are continuous, we can use either discretization or fit a
# known distribution to the dataset (e.g., Gaussian). Before we fit a Gaussian
# distribution, we should perform a sanity check to see if the dataset features can be
# approximated with a Gaussian distribution.
#
# Smoothness and texture are relatively Gaussian but radius is not. However, we'll fit a
# Gaussian to the radius feature as well for simplicity.
fig, axes = plt.subplots(1, 3, figsize=(18, 6), sharey=True)
sns.histplot(data, ax=axes[0], x="mean_radius", kde=True, color="r")
sns.histplot(data, ax=axes[1], x="mean_smoothness", kde=True, color="b")
sns.histplot(data, ax=axes[2], x="mean_texture", kde=True)
# plt.show()


# Calculate P(Y = y) for all possible y
def compute_prior(df, Y):
    return [len(df[df[Y] == i]) / len(df) for i in sorted(list(df[Y].unique()))]


# Approach 1: Calculate P(X = x|Y = y) using Gaussian distribution
def compute_likelihood_gaussian(df, feat_name, feat_val):
    mean, std = df[feat_name].mean(), df[feat_name].std()
    p_x_given_y = np.exp(-0.5 * ((feat_val - mean) / std) ** 2) / (
        np.sqrt(2 * np.pi) * std
    )
    return p_x_given_y


# Calculate P(X = x_1|Y = y) * P(X = x_2|Y = y) * ... * P(X = x_n|Y = y) * P(Y = y) for
# all y and find the maximum
def naive_bayes_gaussian(df, X, Y):
    feature_names, prior = list(df.columns)[:-1], compute_prior(df, Y)
    labels, y_pred = sorted(list(df[Y].unique())), []
    for x in X:
        likelihood = [1] * len(labels)
        for i, label in enumerate(labels):
            for j, feature_name in enumerate(feature_names):
                likelihood[i] *= compute_likelihood_gaussian(
                    df[df[Y] == label], feature_name, x[j]
                )
        post_prob = [likelihood[i] * prior[i] for i in range(len(labels))]
        y_pred.append(np.argmax(post_prob))
    return np.array(y_pred)


# Test Gaussian model
#
# When we train the Naive Bayesian model, we use the training dataset to compute the
# priors and get the unique labels. Then, for each new data point, we compute the
# likelihood of each of the features of the new data point given the training data.
train, test = train_test_split(data, test_size=0.2, random_state=41)
X_test = test.iloc[:, :-1].values
Y_test = test.iloc[:, -1].values
Y_pred = naive_bayes_gaussian(train, X=X_test, Y="diagnosis")
print(confusion_matrix(Y_test, Y_pred))
print(f1_score(Y_test, Y_pred))
print()

# Convert continuous features to categorical features
data["cat_mean_radius"] = pd.cut(data["mean_radius"].values, bins=3, labels=[0, 1, 2])
data["cat_mean_texture"] = pd.cut(data["mean_texture"].values, bins=3, labels=[0, 1, 2])
data["cat_mean_smoothness"] = pd.cut(
    data["mean_smoothness"].values, bins=3, labels=[0, 1, 2]
)

data = data.drop(columns=["mean_radius", "mean_texture", "mean_smoothness"])
data = data[["cat_mean_radius", "cat_mean_texture", "cat_mean_smoothness", "diagnosis"]]
print(data.head(10))
print()


# Approach 2: Calculate P(X = x|Y = y) categorically
def compute_likelihood_categorical(df, feat_name, feat_val):
    p_x_given_y = len(df[df[feat_name] == feat_val]) / len(df)
    return p_x_given_y


# Calculate P(X = x_1|Y = y) * P(X = x_2|Y = y) * ... * P(X = x_n|Y = y) * P(Y = y) for
# all y and find the maximum
def naive_bayes_categorical(df, X, Y):
    feature_names, prior = list(df.columns)[:-1], compute_prior(df, Y)
    labels, y_pred = sorted(list(df[Y].unique())), []
    for x in X:
        likelihood = [1] * len(labels)
        for i, label in enumerate(labels):
            for j, feature_name in enumerate(feature_names):
                likelihood[i] *= compute_likelihood_categorical(
                    df[df[Y] == label], feature_name, x[j]
                )
        post_prob = [likelihood[i] * prior[i] for i in range(len(labels))]
        y_pred.append(np.argmax(post_prob))
    return np.array(y_pred)


# Test categorical model
train, test = train_test_split(data, test_size=0.2, random_state=41)
X_test = test.iloc[:, :-1].values
Y_test = test.iloc[:, -1].values
Y_pred = naive_bayes_categorical(train, X=X_test, Y="diagnosis")
print(confusion_matrix(Y_test, Y_pred))
print(f1_score(Y_test, Y_pred))
