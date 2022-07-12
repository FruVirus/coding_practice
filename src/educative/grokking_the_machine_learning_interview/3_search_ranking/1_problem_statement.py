"""
Main Takeaways
~~~~~~~~~~~~~~

Clarify the problem statement by specifying three aspects: scope, scale, and
personalization.

The interviewer’s question is really broad. Your best bet is to avoid ambiguities and
ask the interviewer as many questions as you can. This will narrow down your problem
space as you are thinking out loud for the best solution. This scoping down of the
problem is critical as you dive into finding the solutions.

Once you know that you are building a general search engine, it’s also critical to
determine the scale of the system. A couple of important questions are:

    - How many websites exist that you want to enable through this search engine?

    - How many requests per second do you anticipate to handle?

Understanding this scale is important to architect our relevance system.

Another important question that you want to address is whether the searcher is a
logged-in user or not. This will define the level of personalization that you can
incorporate to improve the relevance of our results.

Problem Statement
=================

Problem statement
-----------------

The interviewer has asked you to design a search relevance system for a search engine.

Clarifying questions
--------------------

Let’s clarify the problem statement by specifying three aspects: scope, scale, and
personalization.

Problem scope

The interviewer’s question is really broad. Your best bet is to avoid ambiguities and
ask the interviewer as many questions as you can. This will narrow down your problem
space as you are thinking out loud for the best solution.

So, your first question for the interviewer would be something like the following:

    Is it a general search engine like Google or Bing or a specialized search engine
like Amazon products search?

This scoping down of the problem is critical as you dive into finding the solutions. For
the sake of this chapter, we will assume that you are working towards finding relevant
results using a general search engine like Google search or Bing search, but the
techniques and discussion apply to all search engines.

Finally, the problem statement can be precisely described as:

    Build a generic search engine that returns relevant results for queries like
“Richard Nixon”, “Programming languages” etc.

This will require you to build a machine learning system that provides the most relevant
results for a search query by ranking them in order of relevance. Therefore, you will be
working on the search ranking problem.

Scale

Once you know that you are building a general search engine, it’s also critical to
determine the scale of the system. A couple of important questions are:

    - How many websites exist that you want to enable through this search engine?

    - How many requests per second do you anticipate to handle?

We will assume that you have billions of documents to search from, and the search engine
is getting around 10K queries per second (QPS).

Understanding this scale is important to architect our relevance system. For example,
later in the chapter, we will go over the funnel-based approach where you will continue
to increase model complexity and reduce document set, as you go down the funnel for this
large scale search system.

Personalization

Another important question that you want to address is whether the searcher is a
logged-in user or not. This will define the level of personalization that you can
incorporate to improve the relevance of our results. You will assume that the user is
logged in and you have access to their profile as well as their historical search data.
"""
