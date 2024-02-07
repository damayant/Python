'''
Table: Employee

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| salary      | int     |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the ID of an employee, their name, salary, and the ID of their manager.
 

Write a solution to find the employees who earn more than their managers.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Employee table:
+----+-------+--------+-----------+
| id | name  | salary | managerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | Null      |
| 4  | Max   | 90000  | Null      |
+----+-------+--------+-----------+
Output: 
+----------+
| Employee |
+----------+
| Joe      |
+----------+
Explanation: Joe is the only employee who earns more than his manager.
'''

import pandas as pd

def find_employees(employee:pd.DataFrame)->pd.DataFrame:
    #merge the employee table with itself to obtain the salary information of managers for each employee. 
    #Note that we set how=inner because we only need the rows where there is a match between the managerId and id columns. 
    #An inner join will return only the employees whose manager is not NULL.
    df =  employee.merge(employee,left_on='managerId',right_on='id',suffixes=['_e','_m'],how='inner')
    # Since there will be two columns with the same name after the merge operation, we need to assign suffixes to both tables. 
    #By default, the suffixes are _x and _y. 
    #In this problem, the left and right tables can be treated as information for employees and managers, respectively. Therefore, we use _e and _m for better understanding.
    
    #we can use loc to select rows of interest.
    df = df.loc[df['salary_e']>df['salary_m'],['name_e']]

    return df.rename(columns={'name_e':'Employee'})
