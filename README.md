# Assessment: Flask Microblog 
This assessment introduces Flask through the [Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) series.

## Author
- Kash Farhadi

### Reference Material and Credits
- Miguel Grinberg -- Flask Mega Tutorial Author

### Part 1: Hello World
- Learn how to set up a Flask project.
- Run a simple Flask web application.

### Part 2: Templates
- Generate a more elaborate web page that has a complex structure and many dynamic components.
- Create template html pages so you DRY and separates the user interface layout from the business logic. 


### Part 3: Web Forms
- Create forms to allow users to submit blog posts and  log in to the application.
- Implement the FlaskWTF extension

### Part 4: Database

- Implement SQLAlchemy that allows development with a simple SQLite database without a server. Then at the time of deployment, choose a more robust server to a production server without altering your application.
- Implement Alembic, for a robust way to make changes to your database in the future.

## Getting Started

### Running the Application

Clone this repository to your local machine
Use pipenv to create a python 3 virtual environment at the top level of your microblog folder, 

To run the application in terminal:

    FLASK_APP=microblog.py 
    
and execute:
        
        flask run

 Or enter this command into the terminal while in the project directory 

          python microblog.py

Then, open the site by entering the following URL in your web browser's address bar:

        http://localhost:5000/ 

## Built With:

- [Python](https://wiki.python.org/moin/BeginnersGuide) --  an object-oriented, high-level programming language that uses simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance.

- [Flask](https://palletsprojects.com/p/flask/) -- a lightweight WSGI web application framework that is designed to make getting started quick and easy.

- [FlaskWTF](https://flask-wtf.readthedocs.io/en/stable/)--a flask extension that simplifies integration of Flask and WTForms.

- [FlaskSQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) -- an extension for Flask that adds support for SQLAlchemy to your application. It provides useful defaults and helpers that make it easier to accomplish common tasks.

- [Alembic](https://bitbucket.org/zzzeek/alembic/src/master/)--a database migrations tool for SQLAlchemy.

