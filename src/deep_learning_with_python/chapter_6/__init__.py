"""The universal workflow of machine learning

The universal workflow of machine learning is broadly structured in three parts:

1. Define the task---Understand the problem domain and the business logic underlying
what the customer asked for.

2. Develop a model---Prepare your data so that it can be processed by a machine learning
model, select a model evaluation protocol and a simple baseline to beat, train a first
model that has generalization power and that can overfit, and then regularize and tune
your model until you achieve the best possible generalization performance.

3. Deploy the model---Present your work to stakeholders, shop the model to a web server,
a mobile app, etc., monitor the model's performance in the wild, and start collecting
the data you'll need to build the next-generation model.

6.1 Define the task
===================

6.1.1 Frame the problem
-----------------------

- What will your input data be? What are you trying to predict? You can only learn to
predict something if you have training data available.

- What type of machine learning task are you facing?

- What do existing solutions look like?

- Are there particular constraints you will need to deal with?

Be aware of the hypotheses you're making at this stage:

- You hypothesize that your targets can be predicted given your inputs.

- You hypothesize that the data that's available is sufficiently informative to learn
the relationship between inputs and targets.

6.1.2 Collect a dataset
-----------------------

Beware Of Non-Representative Data

It's critical that the data used for training should be representative of the production
data.

If possible, collect data directly from the environment where your model will be used.

A related phenomenon you should be aware of is concept drift. Concept drift occurs when
the properties of the production data change over time, causing model accuracy to
gradually decay.

Using machine learning trained on past data to predict the future is making the
assumption that the future will behave like the past. That often isn't the case.

6.1.3 Understand your data
--------------------------

- If your data includes images or natural language text, take a look at a few examples
directly.

- If your data contains numerical features, plot a histogram of feature values.

- If your data contains location information, plot it on a map and look for patterns.

- If your task is classification, are the classes balanced?

- Check for target leaking: the presence of features in your data that provide
information about the targets and which may not be available in production. Is every
feature in your data something that will be available in the same form in production?

6.1.4 Choose a measure of success
---------------------------------

Your metric for success will guide all of the technical choices you make throughout the
project. It should directly align with your higher-level goals, such as the business
success of your customer.

6.2 Develop a model
===================

6.2.1 Prepare the data
----------------------

Vectorization

All inputs and targets in a neural network must typically be tensors of floating-point
data. Whatever data you need to process, you must first turn into tensors, a step called
data vectorization.

Value Normalization

To make learning easier for your network, your data should have the following
characteristics:

- Take small values---Typically, most values should be in the 0 - 1 range.

- Be homogeneous---All features should take values roughly in the same range.

- Normalize each feature independently to have a mean of 0.

- Normalize each feature independently to have a standard deviation of 1.

Handle Missing Values

- If the feature is categorical, it's safe to create a category that means "the value is
missing." THe model will automatically learn what this implies with respect to the
targets.

- If the feature is numerical, avoid inputting an arbitrary value like "0", because it
may create a discontinuity in the latent space formed by your features, making it
harder for a model trained on it to generalize. Instead, consider replacing the missing
value with the average or median value for the feature in the dataset.

Note that if you're expecting missing categorical features in the test data, but the
network was trained on data without any missing values, the network won't have learned
to ignore missing values! In this situation, you should artificially generate training
samples with missing entries: copy some training samples several times, and drop some of
the categorical features that you expect are likely to be missing in the test data.

6.2.2 Choose an evaluation protocol
-----------------------------------

Three common evaluation protocols:

- Maintaining a holdout validation set---this is the way to go when you have plenty of
data

- Doing K-fold cross-validation---this is the right choice when you have too few samples
for holdout validation to be reliable.

- Doing iterated K-fold validation---this is for performing highly accurate model
evaluation when little data is available.

6.2.3 Beat a baseline
---------------------

The three most important things you should focus on:

- Feature engineering

- Select the correct architecture priors

- Selecting a good-enough training configuration

6.2.4 Scale up: Develop a model that overfits
---------------------------------------------

To figure out how big a model you'll need, you must develop a model that overfits by:

- Adding layers.

- Making the layers bigger.

- Training for more epochs.

WHen you see that the model's performance on the validation data begins to degrade,
you've achieved overfitting.

6.2.5 Regularize and tune your model
------------------------------------

- Try different architectures; add or remove layers.

- Add dropout.

- If your model is small, add L1 or L2 regularization.

- Try different hyperparameters to find the optimal configuration.

- Optionally, iterate on data curation or feature engineering.

Every time you use feedback from your validation process to tune your model, you leak
information about the validation process into the model. Repeated just a few times, this
is innocuous; done systematically over many iterations, it will eventually cause your
model to overfit to the validation process.

Once you've developed a satisfactory model configuration, you can train your final
production model on all the available data (training and validation) and evaluate it one
last time on the test set.

6.3 Deploy the model
====================

6.3.1 Explain your work to stakeholders and set expectations
------------------------------------------------------------

Success and customer trust are about consistently meeting or exceeding people's
expectations. The actual system you deliver is only half of that picture; the other half
is setting appropriate expectations before launch.

You should consider showing some examples of the failure modes of your model.

You should clearly convey model performance expectations. Clearly relate the model's
performance metrics to business goals.

Discuss with stakeholders the choice of key launch parameters---for instance, the
probability threshold at which a transaction should be flagged.

6.3.2 Ship an inference model
-----------------------------

Inference Model Optimization

There are two popular optimization techniques you can apply:

- Weight pruning---Not every coefficient in a weight tensor contributes equally to the
predictions. It's possible to considerably lower the number of parameters in the layers
of your model by only keeping the most significant ones.

- Weight quantization---Deep learning models are trained with single-precision
floating-point (float32) weights. However, it's possible to quantize weights to 8-bit
signed integers (int8) to get an inference-only model that's a quarter the size but
remains near the accuracy of the original model.

6.3.3 Monitor your model in the wild
------------------------------------

Once you've deployed a model, you need to keep monitoring its behavior, its performance
on new data, its interaction with the rest of the application, and its eventual impact
on business metrics.

- Consider using randomized A/B testing to isolate the impact of the model itself from
other changes.

- If possible, do a regular manual audit of the model's predictions on production data.

- When manual audits are impossible, consider alternative evaluation avenues such as
user surveys.

6.3.4 Maintain your model
-------------------------

As soon as your model has launched, you should be getting ready to train the next
generation that will replace it. As such,

- Watch out for changes in the production data. Are new features becoming available?
Should you expand or otherwise edit the label set?

- Keep collecting and annotating data, and keep improving your annotation pipeline over
time.
"""
