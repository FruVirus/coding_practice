"""
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

Scale

Once you know that you are building a general search engine, it’s also critical to
determine the scale of the system. A couple of important questions are:

    - How many websites exist that you want to enable through this search engine?

    - How many requests per second do you anticipate to handle?

Understanding this scale is important to architect our relevance system. For example,
later in the chapter, we will go over the funnel-based approach where you will continue
to increase model complexity and reduce document set, as you go down the funnel for this
large scale search system.

Personalization

Another important question that you want to address is whether the searcher is a
logged-in user or not. This will define the level of personalization that you can
incorporate to improve the relevance of our results.
"""
