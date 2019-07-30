#Assessment: Flask Microblog 
This assessment introduces Flask through the [Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) series.

## Author
<ul>
<li>Kash Farhadi</li>
</ul>

## Reference Material and Credits
<li>Miguel Grinberg -- Flask Mega Tutorial Author</li>

### Part 1: Hello World
<ul>
<li>Learn how to set up a Flask project.</li>
<li>Run a simple Flask web application.</li>
</ul>

### Part 2: Templates
<ul>
<li>Generate a more elaborate web page that has a complex structure and many dynamic components.</li>
<li>Create template html pages so you DRY and separates the user interface layout from the business logic. </li>

</ul>

### Part 3: Web Forms
<ul>
<li>Create forms to allow users to submit blog posts and  log in to the application.</li>
<li>Implement the FlaskWTF extension</li>
</ul>

### Part 4: Database
<ul></ul>
<li>Implement SQLAlchemy that allow development with a simple SQLite database without a server, and then choose a more robust server at the time of deployment to a production server without altering your application.</li>
<li> Implement Alembic, for a robust way to make changes to your database in the future.</li>
</ul>
</ul>


## Getting Started

## Running the Application

Clone this repository to your local machine
Use pipenv to create a python 3 virtual environment at the top level of your microblog folder, 

To run the application in terminal:

    FLASK_APP=microblog.py 
    
and execute:
        
        flask run

OR 

        python microblog.py

 while in this directory in your terminal

Open the site by entering the following URL in your web browser's address bar:

        http://localhost:5000/ 

## Built With:
<ul>
<li>[Python](https://wiki.python.org/moin/BeginnersGuide)
</li>


<li>

[Flask](https://palletsprojects.com/p/flask/) -- a lightweight WSGI web application framework. It is designed to make getting started quick and easy.
</li>
<li>

[FlaskWTF](https://flask-wtf.readthedocs.io/en/stable/)--Integrates Flask and WTForms.
</li>

<li>

[FlaskSQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) -- an extension for Flask that adds support for SQLAlchemy to your application. It aims to simplify using SQLAlchemy with Flask by providing useful defaults and extra helpers that make it easier to accomplish common tasks.
</li>
<li>

[Alembic](https://bitbucket.org/zzzeek/alembic/src/master/)--a database migrations tool for SQLAlchemy</li>
</ul>

