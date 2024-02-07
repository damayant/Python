'''
You’re given a dataframe of students named students_df:

students_df table

name	age	favorite_color	grade
Tim Voss	19	red	91
Nicole Johnson	20	yellow	95
Elsa Williams	21	green	82
John James	20	blue	75
Catherine Jones	23	green	93
Write a function named grades_colors to select only the rows where the student’s favorite color is green or red and their grade is above 90.
'''

import pandas as pd

def grades_colors(students_df:pd.DataFrame):
    students_df = students_df[(students_df['grade'] > 90) &
          students_df['favorite_color'].isin(['red','green'])]
    print(students_df)



grades_colors(student_df={"name" : ["Tim Voss", "Nicole Johnson", "Elsa Williams", "John James", "Catherine Jones"], "age" : [19, 20, 21, 20, 23], "favorite_color" : ["red", "yellow", "green", "blue", "green"], "grade" : [91, 95, 82, 75, 93]})