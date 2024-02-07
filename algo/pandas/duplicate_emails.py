'''
Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.
 

Write a solution to report all the duplicate emails. Note that it's guaranteed that the email field is not NULL.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Person table:
+----+---------+
| id | email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
Output: 
+---------+
| Email   |
+---------+
| a@b.com |
+---------+
Explanation: a@b.com is repeated two times.
'''

import pandas as pd

def duplicate_emails(person:pd.DataFrame)->pd.DataFrame:
    
    #Using the groupby function of pandas, we cluster the rows of the DataFrame based on the values in the 'Email' column. 
    #This ensures that rows with identical email addresses are categorized into the same group. Subsequently, for each of these email groups, we count how many times that particular email appears. 
    #This process gives us a clear picture of the frequency of each unique email in our DataFrame.
    email_counts = person.groupby('email').size().reset_index(name='num')

    #filter for emails that occur more than once
    duplicated_emails_df = email_counts[email_counts['num']>1][['email']]

    return duplicated_emails_df