"""
Metrics
=======

Component level metric
----------------------

In order to look for a suitable metric to measure the performance of an image segmenter,
the first notion that comes to mind is the pixel-wise accuracy. Using this metric, you
can simply compare the ground truth segmentation with the model’s predictive
segmentation at a pixel level. However, this might not be the best idea, e.g., consider
a scenario where the driving scene image has a major class imbalance, i.e., it mostly
consists of sky and road.

If your model correctly classifies all the pixels of only sky and road, it will result
in high pixel-wise accuracy. However, this is not really indicative of good performance
since the segmenter completely misses other classes such as building and roadside!

IoU
---

You will be using IoU as an offline metric to test the performance of the segmentation
model.

Intersection over Union (IoU) divides the overlapping area between the predicted
segmentation and the ground truth in perspective, by the area of union between the
predicted segmentation and the ground truth.

IoU = area of intersection / area of union
    = (Pred and GT) / ((Pred + GT) - (Pred and GT)

This metric ranges from 0 – 1. ‘0’ indicates no overlap while ‘1’ indicates perfectly
overlapping segmentation.

The driving images contain objects of multiple classes (e.g., building,roadside, sky,
road, etc.). So, you will be performing multi-class segmentation, for which the mean IoU
is calculated by taking the average of the IoU for each class.

You will begin by calculating the IoU for each class. Here, the “area of overlap” means
the number of pixels that belong to the particular class in both the prediction and
ground-truth. Whereas, the “area of union” refers to the number of pixels that belong to
the particular class in the prediction and in ground-truth, but not in both (the overlap
is subtracted).

End-to-end metric
-----------------

You also require an online, end-to-end metric to test the overall performance of the
self-driving car system as you plug in your new image segmenter to see its effect.

Manual intervention

Ideally, you want the system to be as close to self-driving as possible, where the
person never has to intervene and take control of the driving. So, you can use manual
intervention as a metric to judge the success of the overall system. If a person rarely
has to intervene, it means that your system is performing well.

Simulation errors

Another approach is to use historical data, such as driving scene recording, where an
expert driver was driving the car. You will give the historical data as input to your
self-driving car system with the new segmentation model and see how its decisions align
with the decisions made by an expert driver.

You will assume that the decisions made by the professional driver in that actual
scenario are your ground truths. The overall objective will be to minimize the movement
and planning errors with these ground truths.
"""
