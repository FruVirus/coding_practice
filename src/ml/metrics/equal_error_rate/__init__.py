"""
Equal Error Rate (EER)
======================

Equal error rate (EER) is a biometric security system algorithm used to predetermine the
threshold values for its false acceptance rate and its false rejection rate. When the
rates are equal, the common value is referred to as the equal error rate. The value
indicates that the proportion of false acceptances is equal to the proportion of false
rejections. The lower the equal error rate value, the higher the accuracy of the
biometric system.

Equal error rate may also be referred to as a crossover rate or crossover error rate
(CER).

The EER is also the "rounded" point (top left corner) on ROC graphs. It is the value
when the FPR and FNR are equal (or minimized). If we draw a line from (0, 1) to (1, 0),
then the intersection of that line with the ROC graph is the EER.

EER means increasing the TPR and reducing the FPR as much as possible by choosing an
optimum threshold on a ROC curve. This could also be seen as maximizing TPR and
minimizing FPR or simply maximizing (TPR - FPR). By maximizing, I mean bringing the
value close to 1.

The above formulation can also be written as minimizing (1 - (TPR - FPR)); here,
minimizing means bringing the value close to 0. And since, FNR = 1 - TPR, the above
function takes the form, minimizing (FNR + FPR), i.e. both FNR and FPR must be close to
0.

EER = max(TPR - FPR) --> TPR - FPR = 1
EER = min(FPR + FNR) --> FPR + FNR = 0

To find the actual value for EER, find the point at which FPR = FNR. Then the value of
FPR (or FNR) is the EER.
"""
