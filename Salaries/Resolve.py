from numpy import NAN, NaN, nan, unique
from numpy.core.fromnumeric import mean
import pandas as pd
import numpy as np
from collections import Counter
import math
# pf= pd.read_csv("Salaries.csv")
f = open('Salaries.csv','r')
data = pd.read_csv(f)
#1,2. 
print(data.head(10))
#3. 
print(data.info())
# 4.  
print("the average BasePay is", data["BasePay"].mean())
#5
print("the highest amount of OvertimePay in the dataset: ", max(data["OvertimePay"]))
#6
Bai6 = data[data['EmployeeName'] == 'JOSEPH DRISCOLL']
print(f"the job title of JOSEPH DRISCOLL is : {Bai6['JobTitle']}")
#7 
Bai7 = data[data['EmployeeName'] == 'JOSEPH DRISCOLL']
print(f"JOSEPH DRISCOLL make (including benefits) : {Bai7['TotalPayBenefits']}")
#8
max_pay = max(data["TotalPay"])
Bai8 = data[data['TotalPay'] == max_pay]
print(f"the name of highest paid person (including benefits) : {Bai8['EmployeeName']}")
#9
min_pay = min(data["TotalPay"])
Bai9 = data[data['TotalPay'] == min_pay]
print(f"the name of lowest paid person (including benefits) : {Bai9['EmployeeName']}")
#10. What was the average (mean) BasePay of all employees per year? (2011-2014)
Bai10 = data[data['Year'] == 2011]
print("the average BasePay (2011) is", Bai10["BasePay"].mean())
#11. How many unique job titles are there?
print(f"there are {len(unique(data['JobTitle']))} job title")
#12. What are the top 5 most common jobs?
print(f"the top 5 most common jobs is {Counter(data['JobTitle']).most_common(5)}")
#13 How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?)
Bai13 = data[data['Year'] == 2013]
print(f"there are: { sum(Bai13['JobTitle'].value_counts() == 1)} job title in 2013")
#14 How many people have the word Chief in their job title? (This is pretty tricky)
print(data['JobTitle'].apply(lambda str:('chief' in str.lower())).sum())
#15 Is there a correlation between length of the Job Title string and Salary?
data['Job_Title_Str'] = data['JobTitle'].str.len()
data['Salary'] = data['TotalPayBenefits']
print(data[['Job_Title_Str','Salary']].corr())
