"""
Regularization
==============

Overview
--------

Q: How do Ridge or Lasso know which variables are useless? Will they not also shrink the
parameter of important variables?

A: You could think of it as if Ridge and Lasso are balancing between the predictive
ability and the complexity of the model. If a feature is very helpful in predicting,
then even if we have Ridge or Lasso as penalties, it won't make the weight of this
feature go to 0 because in that case the least square error (or whatever the objective
function is) will increase. On the other hand, if a feature is not very useful, yet we
initially assigned a weight to it, Ridge or Lasso can help to remove/reduce how much
this feature contributes to the final result by penalising the model for having this
(useless) feature, because by reducing/removing this feature, our least square error
won't increase much, but we can get a much larger reduction in the penalty term.

Part 1: Ridge (L2) Regression
=============================

Ridge Regression Main Ideas
---------------------------

Suppose we have a training dataset with (x, y) pairs. If the data looks relatively
linear, we can use Linear Regression (i.e., Least Squares), to model the relationship
between x and y.

When we have a lot of measurements, we can be fairly confident that the Least Squares
line accurately reflects the relationship between x and y. But what if we only have two
measurements? If we fit a new line to two data points, the minimum sum of squared
residuals is 0. This means that the new line has high variance and is overfit to the
training data.

The main idea behind Ridge Regression is to find a new line that doesn't fit the
training data as well. We introduce a small amount of bias into how the new line is fit
to the data. In other words, by starting with a slightly worse fit, Ridge Regression can
provide better long term predictions (i.e., better predictions on unseen data).

Ridge Regression details
------------------------

When Least Squares minimizes the values for the parameters in the line, it minimizes the
sum of the squared residuals.

In contrast, when Ridge Regression determines the values for the parameters in the line,
it minimizes the sum of the squared residuals plus lambda * slope^2. The latter part
adds a penalty to the traditional Least Squares method and lambda determines how severe
that penalty is.

Without a small amount of Bias that the penalty creates, the Least Squares Fit has a
large amount of Variance. In contrast, the Ridge Regression Line, which has the small
amount of Bias due to the penalty, has less Variance. In effect, the Least Squares Fit
might have a lower penalty from the sum of squared residuals, but it will have a higher
penalty from the slope and vice versa for the Ridge Regression line.

Intuitively, when the slope of the line is steep, then the predicted y values are very
sensitive to relatively small changes in the x values. And when the slope of the line is
small, then the predicted y values are less sensitive to changes in the x values.

The Ridge Regression Penalty results in a line that has a smaller slope, which means
that predictions made with the Ridge Regression Line are less sensitive to the x values
that the Least Squares Line.

Lambda can be any value from 0 to infinity. As lambda increases, the slope of the line
decreases. As lambda approaches infinity, the slope of the line approaches 0 and this
means that the predicted y values becomes less and less sensitive to the x values, and
ultimately, the predicted y values is just the average y value.

Ridge Regression for fancy models
---------------------------------

In general, the Ridge Regression Penalty contains all of the parameters except for the
y-intercept.

Ridge Regression Penalty = lambda * sum(param_1^2 + param_2^2 + ...)

Every parameter, except for the y-intercept, is scaled by the measurements and that's
why the y-intercept is excluded in the Ridge Regression Penalty.

Ridge Regression when you don't have much data
----------------------------------------------

In order for Least Squares to solve for the parameters of a line (i.e., the y-intercept
and the slope), it needs at least two data points. When we have three parameters, we
need a minimum of three data points and so on.

What do we do if we have an equation with 10,001 parameters but only 500 data points?

We use Ridge Regression!

It turns out that by adding the Ridge Regression Penalty, we can solve for all 10,001
parameters with only 500 (or even fewer) samples.

If we only have one data point, Least Squares can't find a single optimal solution since
any line that goes through the data point will minimize the sum of the squared
residuals. But Ridge Regression with Cross Validation can find a solution that favors
smaller parameter values (see explanation below).

Summary of concepts
-------------------

When the sample sizes are relatively small, then Ridge Regression can improve
predictions made from new data (i.e., reduce Variance) by making the predictions less
sensitive to the Training Data.

This is done by adding the Ridge Regression Penalty to the thing that must be minimized.

The Ridge Regression Penalty itself is lambda times the sum of all squared parameters,
except for the y-intercept and lambda is determined using Cross Validation.

Lastly, even when there isn't enough data to find the Least Squares parameter estimates,
Ridge Regression can still find a solution with Cross Validation and the Ridge
Regression Penalty.

Part 2: Lasso (L1) Regression
=============================

Lasso Regression is very similar to Ridge Regression but it has some very important
differences.

The Lasso Regression Penalty is lambda * sum(abs(param_1) + abs(param_2) + ...). Just
like with Ridge Regression, lambda can be any value from 0 to infinity and is determined
using Cross Validation. In addition, Lasso Regression includes all parameters except for
the y-intercept.

Like Ridge Regression, Lasso Regression results in a line with a little bit of Bias but
less Variance than Least Squares.

The big difference between Ridge and Lasso Regression is that Ridge Regression can only
shrink the slope asymptotically close to 0 while Lasso Regression can shrink the slope
all the way to 0. In other words, the Lasso penalty will force some of the coefficients
quickly to zero, which means that variables are removed from the model, hence the
sparsity. Ridge regression will more or less compress the coefficients to become
smaller, which does not necessarily result in 0 coefficients and removal of variables.

Since Lasso Regression can exclude useless variables from equations, it is a little
better than Ridge Regression at reducing the Variance in models that contain a lot of
useless variables. In contrast, Ridge Regression tends to do a little better when most
variables are useful.

Part 3: Elastic Net Regression
==============================

When happens when we have a model with millions of parameters? When you have millions of
parameters, then you will almost certainly need to use some sort of regularization to
estimate them. The variables in those models might be useful or useless---we don't know
in advance. So how do you choose if you should use Lasso or Ridge Regression?

The good news is that you don't have to choose---instead, you use Elastic-Net
Regression.

Just like Lasso and Ridge Regression, Elastic Net Regression starts with Least Squares,
then it combines the Lasso Regression Penalty with the Ridge Regression Penalty.
Altogether, Elastic Net Regression combines the strengths of Lasso and Ridge Regression.

The Lasso and Ridge Regression Penalties get their own lambdas. We use Cross Validation
on different combinations of lambda_1 and lambda_2 to find the best values.

When lambda_1 = lambda_2 = 0, we get Least Squares Regression.

When lambda_2 = 0, we get Lasso Regression.

When lambda_1 = 0, we get Ridge Regression.

When lambda_1 > 0 and lambda_2 > 0, we get Elastic Net Regression, which is really good
at dealing with situations when there are correlations between parameters.

This is because on its own, Lasso Regression tends to pick just one of the correlated
terms and eliminates the others whereas Ridge Regression tends to shrink all of the
parameters for the correlated variables together. By combining Lasso and Ridge
Regression, Elastic Net Regression groups and shrinks the parameters associated with the
correlated variables and leaves them in the equation or removes them all at once.
"""
