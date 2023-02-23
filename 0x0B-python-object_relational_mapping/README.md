# Object-Relational Mapping in Python

This project is designed to introduce you to Object-Relational Mapping (ORM) in Python, using the SQLAlchemy library. In this project, you will learn how to connect to a MySQL database from a Python script, and how to map Python classes to database tables using an ORM.

 ### Getting Started

Before you begin, make sure you have the following prerequisites installed:

Python 3.8.5 or later
MySQL server 8.0
MySQLdb module version 2.0.x
SQLAlchemy module version 1.4.x
To install MySQL server 8.0 on Ubuntu 20.04, follow the instructions in this tutorial.

To install the MySQLdb and SQLAlchemy modules, run the following commands:

ruby
Copy code
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
$ sudo pip3 install SQLAlchemy
Running the Code

To run the code, follow these steps:

Clone the repository to your local machine.
Create a MySQL database and configure the connection in config.py.
Run the command python3 setup_database.py to set up the database tables.
Run the command python3 run.py to execute the main program.
The run.py script will demonstrate how to use SQLAlchemy to perform basic CRUD operations on the database.

Project Structure

The project is structured as follows:

config.py: Configuration file containing database connection details.
setup_database.py: Python script to set up the database tables.
models.py: Python classes that map to database tables using SQLAlchemy.
run.py: Main program that demonstrates how to use SQLAlchemy to interact with the database.
Technologies Used

Python 3.8.5
MySQL server 8.0
MySQLdb module version 2.0.x
SQLAlchemy module version 1.4.x
Resources

Object-relational mappers
MySQLdb tutorial
SQLAlchemy tutorial
SQLAlchemy ORM Tutorial for Python Developers
Flask SQLAlchemy

