"""Machine Learning Fundamentals: Sensitivity and Specificity

Once we've filled out the Confusion Matrix, we can calculate two useful metrics:
Sensitivity and Specificity.

2 x 2 Matrix
------------

Sensitivity tells us what percentage of patients with heart disease were correctly
classified.

Sensitivity = TP / (TP + FN)

Specificity tells us what percentage of patients without heart disease were correctly
classified.

Specificity = TN / (TN + FP)

Sensitivity tells us which model is better at correctly identifying positives.
Specificity tells us which model is better at correctly identifying negatives.

N x N Matrix
------------

The big difference for larger confusion matrices is that there are no single values that
work for the entire matrix.

Instead, we calculate a different Sensitivity and Specificity for each category.

                Troll 2     Gore Police     Cool as Ice
Troll 2         12          102             93
Gore Police     112         23              77
Cool as Ice     83          92              17

Sensitivity for Troll 2 = TP / (TP + FN) = 12 / (12 + 112 + 83) = 0.06
Specificity for Troll 2 = TN / (TN + FP) = (23 + 77 + 92 + 17) / (209 + 102 + 93) = 0.52

Sensitivity for Troll 2 tells us that only 6% of the people that loved the movie Troll 2
more than Gore Police or Cool as Ice were correctly identified.

Specificity for Troll 2 tells us that 52% of the people who loved Gore Police or Cool as
Ice more than Troll 2 were correctly identified.

Sensitivity for Gore Police = TP / (TP + FN) = 23 / (23 + 102 + 92)
Specificity for Gore Police = TN / (TN + FP) = (12 + 93 + 83 + 17) / (205 + 112 + 77)

Sensitivity for Cool as Ice = TP / (TP + FN) = 17 / (17 + 93 + 77)
Specificity for Cool as Ice = TN / (TN + FP) = (12 + 102 + 112 + 23) / (249 + 83 + 92)

Precision, Recall, and F1 SCore
-------------------------------

Recall tells us what percentage of patients with heart disease were correctly
classified.

Recall = Sensitivity = TP / (TP + FN)

Precision tells us what percentage of patients classified as having heart disease
actually have heart disease.

Precision = TP / (TP + FP)

F1 Score combines precision and recall. In order for the F1 Score to be high, both
precision and recall must be high.

F1 Score = 2 * Precision * Recall / (Precision + Recall)
"""
