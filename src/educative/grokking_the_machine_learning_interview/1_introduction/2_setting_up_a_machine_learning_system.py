"""
Setting up a Machine Learning System
====================================

Overview
--------

Interviewers will generally ask you to design a machine learning system for a particular
task. For instance, they may ask you to design the machine learning system for the
following problems:

    - Build a system that shows relevant ads for search engines.
    - Extract all persons, locations, and organizations from a given corpus of
documents.
    - Recommend movies to a user on Netflix.

Key steps in ML system setup
----------------------------

The key steps involved in machine learning project set up are as follows:

1. Setting up the problem

The interviewer’s question is generally very broad. So, the first thing you need to do
is ask questions. Asking questions will close the gap between your understanding of the
question and the interviewer’s expectations from your answer. You will be able to narrow
down your problem space, chalk out the requirements of the system, and finally arrive at
a precise machine learning problem statement.

Some problems may require you to think about hardware components that could provide
input for the machine learning models.

2. Understanding scale and latency requirements

Another very important part of the problem setup is the discussion about performance and
capacity considerations of the system. This conversation will allow you to clearly
understand the scale of the system and its requirements.

Latency requirements

    - Do we want to return the search result in 100 milliseconds or 500 milliseconds?
    - Do we want to return the list of relevant tweets in 300 milliseconds or 400
milliseconds?

Scale of the data

    - How many requests per second do we anticipate to handle?
    - How many websites exist that we want to enable through this search engine?
    - If a query has 10 billion matching documents, how many of these would be ranked by
our model?
    - How many tweets would we have to rank according to relevance for a user at a time?

The answers to these questions will guide you when you come up with the architecture of
the system. Knowing that you need to return results quickly will influence the depth and
complexity of your models. Having huge amounts of data to process, you will design the
system with scalability in mind.

3. Defining metrics

Metrics will help you to see if your system is performing well. Knowing our success
criteria helps in understanding the problem and in selecting key architectural
components.

Metrics for offline testing

You will use offline metrics to quickly test the models’ performance during the
development phase. You may have generic metrics; for example, if you are performing
binary classification, you will use AUC, log loss, precision, recall, and F1-score. In
other cases, you might have to come up with specific metrics for a certain problem. For
instance, for the search ranking problem, you would use NDCG as a metric.

Metrics for online testing

Think of end-to-end metrics as well as component metrics.

You will use online metrics to test them in the production environment. The decision to
deploy the newly created model depends on its performance in an online test. While
coming up with online metrics, you may need both component-wise and end-to-end metrics.

4. Architecture discussion

You need to think about the components of the system and how the data will flow through
those components.

Architecting for scale

The requirements gathered during problem setup help you in chalking out the
architecture. The funnel approach is a good method to narrow down examples in stages and
using more complex models in later stages.

5. Offline model building and evaluation

This step involves:

    - Training data generation. It is crucial that your training data is of good quality
and quantity. Broadly speaking, we have two methods of training data
collection/generation for supervised learning tasks:

        1. Human labeled data. This is an expensive way to gather data. So we need to
    supplement it with in-house labelers or open-source datasets.
        2. Data collection through a user’s interaction with the pre-existing system.

    Another way to gather data is through the online (currently deployed/pre-existing)
    system.

    - Feature engineering. This is another very crucial step as good features influence
the model’s ability to a great extent. You start this process by explicitly pinpointing
the actors involved in the given task, which you have implicitly identified during
problem setup as well.

    In order to make features, you would individually inspect these actors and explore
their relationships too. For instance, if you individually inspect the logged-in user,
you can come up with features such as the user’s age, gender, language, etc. Likewise,
if you look at the context, an important feature could be the “upcoming holiday”. If
Christmas is approaching and the movie under consideration is also a Christmas movie,
there is a greater chance that the user would watch it. Similarly, we can look at the
historical engagement between the user and media to come up with features. An example
could be the user’s interaction with the movie’s genre in the last three months.

    - Model training. Now, you can finally decide on the ML models that you should use
for the given tasks, keeping the performance and capacity considerations in mind. We can
also try out different hyperparameter values to see what works best.

    If you are using the funnel approach, you may select simpler models for the top of
the funnel where data size is huge and more complex neural networks or trees based
models for successive parts of the funnel.

    We also have the option of utilizing pre-trained SOTA (state of the art) models to
leverage the power of transfer learning (you don’t need to reinvent the wheel completely
each time).

    - Offline evaluation. With careful consideration, divide the data into training and
validation sets. Utilize the metrics you decided on earlier, to measure the model
performance. The top few models, showing the most promise, are taken to the next stage.

6. Online model execution and evaluation

Now that you have selected the top-performing models, you will test them in an online
environment. Online testing heavily influences the decision of deploying the model. This
is where online metrics come into play.

Depending on the type of problem, you may use both component level and end-to-end
metrics. If you see a substantial increase in system performance during the online test,
you can deploy it on production.

7. Iterative model improvement

Your model may perform well during offline testing, but the same increase in performance
may not be observed during an online test. Here, you need to think about debugging the
model to find out what exactly is causing this behavior. The problem areas identified
during model debugging will guide you in building successive iterations of your model.

Is a particular component not working correctly? Is the features’ distribution different
during training and testing time? For instance, a feature called “user’s top five
interest” may show a difference in distribution during training and testing, when
plotted.

Moreover, after the first version of your model has been built and deployed, you still
need to monitor its performance. If the model is not performing as expected, you need to
go towards debugging. You may observe a general failure from a decrease in AUC. Or, you
may note that the model is failing in particular scenarios. For instance, by analysing
the video recording of the self-driving car, you may find out that the image
segmentation fails in rushy areas.
"""
