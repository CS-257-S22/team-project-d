# team-project-d
team-project-d created by GitHub Classroom

Repo for Team D in CS 257. 

For grader of Team Back End Deliverable:
All the necessary files are in the "Production Code" folder. All the files
in this "Production Code" folder need to stay together to be run, so please pull
them together. The followings are the specific details about the files:

(1) "app.py" contains our flask app. <br>
(2) "datasource.py" contains our python code that makes connection to our team database containing<br>
tables and execute the relevant queries, which are used in "app.py".<br>
(3) "app_test.py" and "datasource_test.py" contain a test suite for "app.py" and 
"datasource_test.py", respectively.<br>
(4) The "static" folder contains our CSS/Javascript files, and the "templates" folder contains our HTML files.<br>
(5) "createtable.sql" creates two tables based off of the two datasets "products.csv" and "reviews.csv".<br>

You might not use them, but the below is the instructions for how to create and copy tables on a databse.<br>
(1) Create tables by runing "createtable.sql" <br>
(2) Use the following commands to copy the contents into the two tables (while having the datasets in the same directory)<br>
Copy Command for "products.csv": <br>
```
\copy products FROM 'products.csv' DELIMITER ',' CSV
```
Copy Command for "reviews.csv": <br>
```
\copy reviews FROM 'reviews.csv' DELIMITER ',' CSV
```

Daisuke Yamada, Jake Jasmer, Shoko Ishikawa, Charlie Ney

