'''
Table: Customers

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the ID and name of a customer.
 

Table: Orders

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| customerId  | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
customerId is a foreign key (reference columns) of the ID from the Customers table.
Each row of this table indicates the ID of an order and the ID of the customer who ordered it.
 

Write a solution to find all customers who never order anything.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Customers table:
+----+-------+
| id | name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
Orders table:
+----+------------+
| id | customerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
Output: 
+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
'''

import pandas as pd

def findCustomers(customers:pd.DataFrame, orders:pd.DataFrame)->pd.DataFrame:
    # we can use row filtering to remove customer IDs that do not meet the criteria.

    # isin(values) is used to filter and select rows based on whether their values are present in a given set values.
    # ~ represents logical negation.
    # Therefore, ~isin(values) selects rows if their values are NOT present in values.
    
    #select the rows in which `id` is not present in orders[customerId]
    df = customers[~customers['id'].isin(orders['customerId'])]

    '''
    We can obtain the following table:

    id	name
    2	Henry
    4	Max
    '''

    # Build a dataframe that only contains the column `name` 
    # and rename the column `name` as `Customers`.
    df = df[['name']].rename(columns={'name':'Customers'})

    return df



