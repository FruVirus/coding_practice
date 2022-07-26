"""
Accounts Merge
--------------

Given a list of accounts where each element accounts[i] is a list of strings, where the
first element accounts[i][0] is a name, and the rest of the elements are emails
representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same
person if there is some common email to both accounts. Note that even if two accounts
have the same name, they may belong to different people as people could have the same
name. A person can have any number of accounts initially, but all of their accounts
definitely have the same name.

After merging the accounts, return the accounts in the following format: the first
element of each account is the name, and the rest of the elements are emails in sorted
order. The accounts themselves can be returned in any order.

Intuition
---------

Emails can be represented as nodes, and an edge between nodes will signify that they
belong to the same person. Since all of the emails in an account belong to the same
person, we can connect all of the emails with edges. Thus, each account can be
represented by a connected component. What if two accounts have an email in common? Then
we can add an edge between the two connected components, effectively merging them into
one connected component.

The first step is to find which accounts have an email in common and merge them to form
a larger connected component. Since most implementations of DSU use an array to record
the root (representative) of each component, we will use integers to represent each
component for ease of operability. Therefore, we will give each account a unique ID, and
we will map all the emails in the account to the account's ID. We will use a map,
emailGroup, to store this information.

We chose the account index to be the identifier for all the emails of an account. We
will assign the account index as the group when we get the email for the first time and
when we get an email that we have already traversed, we will merge the current account
and the group that we have previously stored in emailGroup using union operation.

After traversing over all the accounts, we will find the representative of all the
emails which will inform us about their group. Emails with the same representative
belong to the same person/group and hence will be stored together. Also, we can retrieve
the account name for our final answer using accountList as we have group which is the
index in the original accounts list.

1. Traverse over each account, and for each account, traverse over all of its emails. If
we see an email for the first time, then set the group of the email as the index of the
current account in emailGroup.

2. Otherwise, if the email has already been seen in another account, then we will union
the current group (i) and the group the current email belongs to (emailGroup[email]).

3. After traversing over every account and merging the accounts that share a common
email, we will now traverse over every email once more. Each email will be added to a
map (components) where the key is the email's representative, and the value is a list of
emails with that representative.

4. Traverse over components, here the keys are the group indices and the value is the
list of emails belonging to this group (person). Since the emails must be
"in sorted order" we will sort the list of emails for each group. Lastly, we can get the
account name using the accountList[group][0]. In accordance with the instructions, we
will insert this name at the beginning of the email list.

Complexity
==========

Time
----

accountsMerge_dset(accounts): O(n * k * lg (n * k)), where n is the number of accounts
and k is the maximum length of an account.

Space
-----

accountsMerge_dset(accounts): O(n * k).
"""

# Standard Library
from collections import defaultdict

# Repository Library
from src.leet.graph.number_of_provinces import DisjointSet


def sol_dset(accounts):
    n = len(accounts)
    dset, email_group = DisjointSet(n), {}
    for i in range(n):
        for j in range(1, len(accounts[i])):
            email = accounts[i][j]
            if email not in email_group:
                email_group[email] = i
            else:
                dset.union(i, email_group[email])
    group_to_emails = defaultdict(list)
    for email, group in email_group.items():
        group_to_emails[dset.find(group)].append(email)
    merged_accounts = []
    for group, emails in group_to_emails.items():
        name = accounts[group][0]
        merged_accounts.append([name] + sorted(emails))
    return merged_accounts
