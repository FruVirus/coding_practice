"""
Designing a URL Shortening service like TinyURL
===============================================

This service will provide short aliases redirecting to long URLs.

1. Why do we need URL shortening?
---------------------------------

URL shortening is used to create shorter aliases for long URLs. We call these shortened
aliases “short links.” Users are redirected to the original URL when they hit these
short links. Short links save a lot of space when displayed, printed, messaged, or
tweeted. Additionally, users are less likely to mistype shorter URLs.

URL shortening is used to optimize links across devices, track individual links to
analyze audience, measure ad campaigns’ performance, or hide affiliated original URLs.

2. Requirements and Goals of the System
---------------------------------------

You should always clarify requirements at the beginning of the interview. Be sure to ask
questions to find the exact scope of the system that the interviewer has in mind.

Our URL shortening system should meet the following requirements:

Functional Requirements:

1. Given a URL, our service should generate a shorter and unique alias of it. This is
called a short link. This link should be short enough to be easily copied and pasted
into applications.

2. When users access a short link, our service should redirect them to the original
link.

3. Users should optionally be able to pick a custom short link for their URL.

4. Links will expire after a standard default timespan. Users should be able to specify
the expiration time.

Non-Functional Requirements:

1. The system should be highly available. This is required because, if our service is
down, all the URL redirections will start failing.

2. URL redirection should happen in real-time with minimal latency

3. Shortened links should not be guessable (not predictable).

Extended Requirements:

1. Analytics; e.g., how many times a redirection happened?

2. Our service should also be accessible through REST APIs by other services.

3. Capacity Estimation and Constraints
--------------------------------------

Our system will be read-heavy. There will be lots of redirection requests compared to
new URL shortenings. Let’s assume a 100:1 ratio between read and write.

Traffic estimates: Assuming, we will have 500M new URL shortenings per month, with 100:1
read/write ratio, we can expect 50B redirections during the same period:

	100 * 500M => 50B

What would be Queries Per Second (QPS) for our system? New URLs shortenings per second:

	500 million / (30 days * 24 hours * 3600 seconds) = ~200 URLs/s

Considering 100:1 read/write ratio, URLs redirections per second will be:

	100 * 200 URLs/s = 20K/s

Storage estimates: Let’s assume we store every URL shortening request (and associated
shortened link) for 5 years. Since we expect to have 500M new URLs every month, the
total number of objects we expect to store will be 30 billion:

	500 million * 5 years * 12 months = 30 billion

Let’s assume that each stored object will be approximately 500 bytes (just a ballpark
estimate–we will dig into it later). We will need 15TB of total storage:

30 billion * 500 bytes = 15 TB

Bandwidth estimates: For write requests, since we expect 200 new URLs every second,
total incoming data for our service will be 100KB per second:

	200 * 500 bytes = 100 KB/s

For read requests, since every second we expect ~20K URLs redirections, total outgoing
data for our service would be 10MB per second:

	20K * 500 bytes = ~10 MB/s

Memory estimates: If we want to cache some of the hot URLs that are frequently accessed,
how much memory will we need to store them? If we follow the 80-20 rule, meaning 20% of
URLs generate 80% of traffic, we would like to cache these 20% hot URLs.

Since we have 20K requests per second, we will be getting 1.7 billion requests per day:

	20K * 3600 seconds * 24 hours = ~1.7 billion

To cache 20% of these requests, we will need 170GB of memory.

	0.2 * 1.7 billion * 500 bytes = ~170GB

One thing to note here is that since there will be many duplicate requests (of the same
URL), our actual memory usage will be less than 170GB.

High-level estimates: Assuming 500 million new URLs per month and 100:1 read:write
ratio, following is the summary of the high level estimates for our service:

Types of URLs       Time estimates

New URLs            200/s

URL redirections    20K/s

Incoming data       100KB/s

Outgoing data       10 MB/s

Storage for 5 years 15 TB

Memory for cache    170 GB

4. System APIs
--------------

System APIS explicitly state what is expected from the system.

We can have SOAP or REST APIs to expose the functionality of our service. Following
could be the definitions of the APIs for creating and deleting URLs:

createURL(
	api_dev_key, original_url, custom_alias=None, user_name=None, expire_date=None
)

deleteURL(api_dev_key, url_key)

How do we detect and prevent abuse? A malicious user can put us out of business by
consuming all URL keys in the current design. To prevent abuse, we can limit users via
their api_dev_key. Each api_dev_key can be limited to a certain number of URL creations
and redirections per some time period (which may be set to a different duration per
developer key).

5. Database Design
------------------

Defining the DB schema in the early stages of the interview would help to understand the
data flow among various components and later would guide towards data partitioning.

A few observations about the nature of the data we will store:

1. We need to store billions of records.

2. Each object we store is small (less than 1K).

3. There are no relationships between records—other than storing which user created a
URL.

4. Our service is read-heavy.

Database Schema:

We would need two tables: one for storing information about the URL mappings and one for
the user’s data who created the short link.

What kind of database should we use? Since we anticipate storing billions of rows, and
we don’t need to use relationships between objects – a NoSQL store like DynamoDB,
Cassandra or Riak is a better choice. A NoSQL choice would also be easier to scale.

6. Basic System Design and Algorithm
------------------------------------

The problem we are solving here is how to generate a short and unique key for a given
URL.

In the TinyURL example in Section 1, the shortened URL is
“https://tinyurl.com/rxcsyr3r”. The last eight characters of this URL constitute the
short key we want to generate. We’ll explore two solutions here:


"""
