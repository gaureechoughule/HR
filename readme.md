TASK 1:

Write a program to get details of employees who's salary is > 9000. The output should be in following format
{
"Name": "<first_name last_name>",
"email": "<email>",
"phone number": "<phone number without DOT>"
}

1. import csv module
2. Open file using file handling
3. access data in form of dictionary
4. compare the SALARY with given SALARY
5. access the NAME,EMAIL,PHONE_NUMBER
6. data store in dictionary format 


TASK 2:

Write a program to get "HIRE DATE" of employee who's department is within range 30 to 110 AND who's salary is > 4200.
The output should be in following format.

{
"<HIRE DATE in YYYY-MM-DD format>": [
"<first_name last_name>",
...,
"<first_name last_name>"
],
}

1. import csv module
2. Open file using file handling
3. method for access the employees hire date and salary > 4200
  - access of employees DEPARTMENT_ID
  - compare the id 
  - access the compare id employees name and Hire date 
  - Store in dictionary format 
