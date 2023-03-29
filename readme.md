# Table of contents


**0. [Installation Instructions](#installation)**

**1. [R1 - Identification of the problem you are trying to solve by building this particular app.](#req1)**

**2. [R2 - Why is it a problem that needs solving?](#req2)**

**3. [R3 - Why have you chosen this database system. What are the drawbacks compared to others?](#req3)**

**4. [R4 - Identify and discuss the key functionalities and benefits of an ORM](#req4)**

**5. [R5 - Document all endpoints for your API](#req5)**

**6. [R6 - An ERD for your app](#req6)**

**7. [R7 - Detail any third party services that your app will use](#req7)**

**8. [R8 - Describe your projects models in terms of the relationships they have with each other](#req8)**

**9. [R9 - Discuss the database relations to be implemented in your application](#req9)**

**10. [R10 - Describe the way tasks are allocated and tracked in your project](#req10)**


## Installation instructions <a name="installation"></a>

Clone or download the repository from Github. 

Ensure that PostgreSQL is installed. Open command line/terminal and run the following commands:
```psql```

Create the database by typing:
```CREATE DATABASE drone_logs_db;```

Connect to the database:
```\c drone_logs_db;```

Create a user and set a password:
```CREATE USER admin WITH PASSWORD 'admin123';```

Grant the user all privileges:
```GRANT ALL PRIVILEGES ON DATABASE drone_logs_db TO admin;```

Open another command line/terminal and run the following commands:

```python3 -m venv .venv```

```source .venv/bin/activate```

Install dependencies:
```pip install -r requirements.txt```

In the `/src` folder, rename the `.envexample` file to `.env` and set the database connection and JWT secret key
```DATABASE_URL="postgresql+psycopg2://db_dev:123456@localhost:5432/drone_logs_db"```
```SECRET_KEY="example secret key"```

Create, drop and seed the database with the flask reset function. In the console type:
```flask db reset``` 

*Note that this seeds mock records amongst other mock user information, so that additional user records with and without admin privileges are created. See `/src/command/db.py` for more information.*

Run the application:
```flask run```

You should be able to use the application in your browser with the URL prefix 127.0.0.1:5000/, localhost:5000/, or through setup with Insomnia or Postman.


## R1 - Identification of the problem you are trying to solve by building this particular app. <a name="req1"></a>

The purpose of this application is to store data for drone flights. It is intended to by used by either organisations or individuals that require a form of a record keeping and data storage tool. For a hobbyist or organisation that utilises a number of drones, it's a measure of good practice to record the details of the flights as a form of documenting the flight that took place. 

The application allows the user to create and retrieve flight logs of the drone flights, as well as linking the information of the drone that was used and the pilot that flew it. 

In a business setting, a company which utilises a number of drones may find it useful to keep a record of which individual is flying which drone and when, and how the job went. 
A group of racers might hold a comp and need to log their flight times (__might need to change flight minutes or change this sentence). 
Engineers may may need to record how a drone with a certain build performed in a particular weather event. 

An improvement in the flight protocol to include logs can provide a more organised structure to the maintaining of a drones performance and auditing of its intended purpose. Something about the existence of logs helping to draw conclusions about: Examples include: 

- Logs of drones which are damaged or perform poorly in certain circumstances
- How a pilot performs with certain drones
- Alternative form of record keeping for recorded footage
- How a drone performed after a modification
(and more)


Within the application, an organisation or individual may be registered as a User, which is then able to create (log) a drone flight, along with its affiliated pilot and drone. The User is also able to access and read the other flights available.

A separate (or could be the same - reword) account may also be made with administration privileges that can also delete a log. They are also able to create, edit, or delete a pilot or drone on top of the regular User features.

With this, an organisation or individual or group of hobbyists can keep a track on which pilot flew which drone whilst also having a log of custom further details.


## R2 - Why is it a problem that needs solving? <a name="req2"></a>

(mention how theyre in the military too maybe)
With great advancements in its space over the last decade, drones have seen a great rise in popularity across various different fields. Beyond the recognised instances of using a drone to record footage of nature or sports, it's common to see they're now being used for further business-related purposes such as recording weddings or real estate/construction site inspections. Beyond filming footage, they're also being used to transport small goods, monitor weather conditions, or even race in a competitive setting. There is a demand for drones that are custom built for certain purposes. 

Additionally, the culture of 'modular' drones has seen a great rise (though mainly in the racing scene), with a following of keen hobbyists and engineers mixing and matching parts to build their own custom drone. From this it can be seen how keeping a record of how these custom drones, built to their missions objective, can prove useful for its users. Whether in a business or as an individual hobbyist, keeping logs can prove useful for various different reasons;

- To keep records of the date, time and location of the flight
- To have a means of recording a drones performance in certain conditions
- To keep a tally on which footage was recorded where, and when
- To log which pilot flew the drone for a certain flight


## R3 - Why have you chosen this database system. What are the drawbacks compared to others? <a name="req3"></a>

For my project I have chosen to use PostgreSQL as the database management system. 

> “PostgreSQL is an open-source object relational database system with advanced, enterprise-grade capabilities.”
> 

I have chosen this database system for the following reasons: 

- PostgreSQL is an Object Relational Database Management System (ORDBMS) which is able to support both SQL (relational) and JSON (non-relational) queries. It is compatible with Python and flask as well as other third party software used in the development of this app (SQLAlchemy, Marshmallow, JWT).
- As it is an ORDBMS, it maintains the perks of a Relational Database Management System (RDBMS) (storing data in table like structures that may be queried with SQL), with the addition of support for object oriented programming concepts, such as table inheritance and custom data types.
- PostgreSQL software is open source, meaning that it is freely available to use, resulting in no cost for startup or upgrades.
- Has high level, three pillared security with a focus on network-level security, transport-level security and database-level security. It supports user authentication and authorisation, as well as utilising hashing for one-way encryption in the storage of users passwords(1).
- It is highly customisable, and supports a wide range of data types.
- It has a long development history (30+ years) and a large and active community, resulting in a lot of resources and supporting documentation to assist in production.
- Though not yet fully utilised, it is highly scalable, making it suitable for an enterprise level application that handles large amounts of data.

Finally, PostgresQL meets ACID compliance, a computer science term that stands for atomicity, consistency, isolation, and durability. 

> “They represent the key guarantees that database transactions must support to avoid validity errors and maintain data integrity. 
ACID compliance is a primary concern for relational databases as it represents the typical expectations for storing and modifying highly structured data.” (2)
> 

For the purpose of this particular project, PostgreSQL does not have many drawbacks other than initial set up complexity and a steeper learning curve(3). However if the application were to scale and upgrade over time, it’s disadvantages should be considered. Some of the further drawbacks include:

- Performance limitations. Whilst PostgreSQL is very capable when it comes to scaling, it is not highest in class when it comes to speed, MySQL is considered faster.
- Fewer third party tools. As PostgreSQL is not the most popular DBMS (MySQL is the most popular), resulting in less third-party tools that are available to implement.

## R4 - Identify and discuss the key functionalities and benefits of an ORM <a name="req4"></a>

This project utilises SQLAlchemy, a popular pythonic ORM to write simpler queries when interacting with the database. 

Object-Relational Mapping, or ORM, is a programming technique that provides a way to map object oriented programming (OOP) to relational databases(1). ORM libraries (such as SQLAlchemy) provide tools for developers’ to write simpler code to work with SQL databases through a high level of abstraction to perform CRUD (create, read, update, delete) operations by being the intermediary between the application’s code and the SQL database, providing a more object-oriented approach to creating and performing the databases’ interactions. 

Some key functionalities of an ORM include that they allow developers to map objects (or models) to the tables within a relational database. The properties of the models class define the columns of the database table, and the instances of the objects themselves are expressed as a row in the SQL table (see files in `src/models/`). 

ORM can define a relationship between these objects (one-to-one, one-to-many, many-to-many or part of a join table) and the direction of the relationship through the assignment of primary and foreign keys. An example of this can be seen in the file `src/models/drone.py`. 

The Drone model sets its own primary key to be represented in the table, and pulls the foreign key `created_by_user_id` from the primary key column in the table “USERS”, whilst establishing the direction and relationship with another table, FlightLog - indicating that the “DRONES” table will have its own primary key used as a foreign key in another table (represented by the FlightLog model).

```python
db = SQLAlchemy()

class Drone(db.Model):

		# Setting the table name
    __tablename__= "DRONES"

		# Setting the primary key of the DRONES table
    id = db.Column(db.Integer, primary_key=True)

		# Properties of the Drone model (class) 
		# these will be the columns in the database table.
		# Note the validation data validation aspects of the columns
    build_specifications = db.Column(db.String(300))
    weight_gms = db.Column(db.Integer())
    developed_by = db.Column(db.String(50), nullable=False)
    year_of_manufacture = db.Column(db.Integer(), nullable=False)
    last_service = db.Column(db.Date())

    # A column that pulls the primary key(id) of another table ("USERS") 
		# as a foreign key in the column 'created_by_user_id' in "DRONES"
    created_by_user_id = db.Column(
        db.Integer, db.ForeignKey("USERS.id"), nullable=False
        )
    # Relationships to other db tables, establishing that
		# the FlightLog class will pull the "DRONES" primary key as a foreign key
    drones_flight_logs = db.relationship("FlightLog", backref="drones", lazy=True)
```

ORM benefits the developer by providing a layer of abstraction, handling the logic behind the scenes, simplifying and lessening the code required to write and interact with a database, with no SQL commands required.  This allows for easier updating and maintenance of the code, resulting in more time efficient development. 

It also provides a standardised way of ensuring the data involved in performing CRUD operations with a SQL database is valid and meets the requirements set by the model, improving the integrity of the database and eliminating any risks associated with a lack of data consistency.

Additionally, ORM provides application portability as it allows the program to be used with different databases systems simply by changing the configuration, allowing developers to (if required) change database systems to meet the changing requirements of the application.

## R5 - Document all endpoints for your API 

[See end of page](#req5)

## R6 - An ERD for your app <a name="req6"></a>

![T2A2-ERD](./docs/T2A2%20ERD.png)


## R7 - Detail any third party services that your app will use <a name="req7"></a>

**PostgreSQL** was used as the database for this project.

**Flask**

This application has been built using Flask, a web application framework that makes it easier for  developers to build web applications and RESTful web services. It is based on the Werkzeug WSGI (Web Server Gateway Interface) toolkit to handle web server requests and responses, and uses the Jinja2 template engine.  

Flask allows developers to quickly build scalable applications with its support for extensions. It’s a micro framework that provides features to assist development without needing to worry about low level details. It’s easy to set up, making it a good choice for small to medium sized web applications. Additionally, the Flask framework is extensible, with many libraries that are tailored to integrate and expand its functionality.

**SQLAlchemy**

SQLAlchemy is a Python library and Object Relational Mapper that gives the developer the full power and flexibility of SQL (Structured Query Language) in development, providing a high level abstraction to provide a “Pythonic” way of interacting with databases. It has been used with this application to map defined models (`User`, `Drone`, `Pilot`, `FlightLog`) to tables on the database (PostgreSQL). Through using SQLAlchemy, no SQL queries are required in order to communicate with the database. 

It is used in conjunction with Flask-SQLAlchemy, an extension for Flask that adds support and provides integration between Flask and SQLAlchemy through providing simpler ways for the developer to connect to a database and define models and Python classes, as well as performing database operations.

**Marshmallow**

Marshmallow is an Object-Relational Mapping library that has been used to simplify the process of serialising and deserialising Python objects. It is used to convert objects (in this case, JSON strings) to and from Python data types. Marshmallow utilises a “schema” (blueprint) to define and validate input data, convert the input data to a JSON string to use with the API, and serialise the JSON string back to native Python types (defined by the schema). 

Marshmallow is used in conjunction with Flask-Marshmallow, a flask extension that provides integration between Flask and Marshmallow. Like Flask-SQLAlchemy, it provides simpler ways for the developer to use the Marshmallow library within a Flask environment with improved syntax and support. Some files include use of the `marshmallow-sqlalchemy` library, providing further integration between Marshmallow and SQLALchemy.

**JSON Web Tokens (JWT)**

JSON Web Tokens (JWT) is an open standard for securely transmitting information between parties as a JSON object through the use of a digital signature (using a secret key or public/private key pair). (1) It has been used in this application for the main purpose of authorisation and authentication. With JWT, once a user has logged in via `/auth/login`, a token is created, and each subsequent request will read the token allowing the user to access the routes and perform the methods that have been permitted with the associated token. 

JWT-Flask-Extended is used as a flask extension to provide integration between Flask and JWT, simplifying the process of integrating JWT authentication and authorisation. The use of JWT within this application protects certain (admin) routes and their methods (DELETE, PUT, PATCH, and some POST methods) by ensuring that only authorised users can perform the methods or access the protected routes (through verifying that the user has admin permissions via the users JWT).  

This API web server requires that a user is logged in in order to access any of the routes outside of the `/auth/login`and `/auth/register` routes. Certain routes require further admin level authorisation. This is done through the use of JWT decorators indicating that a token is required (`@jwt_required`) assigned to each route, providing a simple and effective way to secure the API without need for complex authentication/authorisation code.

**Bcrypt**

Bcrypt was used to hash and salt (adding additional random data to the input of a hashing function that makes each password hash unique(1)) users passwords. Passwords are not stored in plain text within the database, but are hashed as they are associated with the User record. Hashing is different to encryption, as encryption is a two-way process that allows for the data to be decrypted (and thus read again). Hashing is one way through its use of salt, and as a result cannot be decrypted. Through storing a password and transforming it into data that can be checked, however can not be converted back to the original password, provides functionality without compromising password security.

Flask-Bcrypt (A Flask extension) was used to provide bcrypt functionality to the Flask application.

**Psycopg2**

Pyscopg2 is a Python library that is used to connect and interact with PostgreSQL. It is used to establish a connection to the PostgreSQL database and execute SQL queries, abstracted via SQLAlchemy. It allows for a pythonic way to cover CRUD (Create, Read, Update, Delete) functionality via executing SQL queries and retrieving the results.

**Insomnia** was used to test API endpoints functionality:

![T2A2-Insomnia](./docs/insomnia-ss.png)


## R8 - Describe your projects models in terms of the relationships they have with each other <a name="req8"></a>

The models in this project are User, Drone, Pilot, and FlightLog, found in their respective files within the `/src/models/` folder. Their data fields and relationship amongst themselves have been defined with SQLAlchemy `(db.Model)` (where `db = SQLALchemy` from `flask_sqlalchemy`).

**User model:**

*user.py*

A User with an email and password must be registered to login and access the API. Once a User is logged in, they are able to post and read a flight log, and read pilot and drone information. 

A User may have admin permissions, which will allow them the full functionality of a regular User with the additional permissions of being able to create, update or delete a pilot or drone record. They may also update or delete flight logs, or delete a user. 

```python
from main import db

class User(db.Model):
    
    #define the table name for the db
    __tablename__= "USERS"

    #set the primary key, we need to define that each attribute is also a column in the db table
    id = db.Column(db.Integer, primary_key=True)

    #add the rest of the attributes
    email = db.Column(db.String(100), nullable=False, unique=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
```

- `__tablename__` defines the table name to be mapped to the model.
- `id = db.Column(db.Integer, primary_key=True)` Creates a column titled ‘id’, of the integer data type. This will be the primary key, and auto increment through each creation of a new User. Not to be set by the user but instead looked after by SQLAlchemy.
- The remaining attribute fields (`email`, `username`, `password`, `is_admin`) are established, with their data type and character limit (`String()` or `Boolean`) set. Mandatory fields are noted by the `nullable=` clause and fields which are required to be unique (not already existing) are noted with boolean clause `unique=`.
- The `is_admin` attribute is not mandatory and will revert to false if not included upon creation. `is_admin` is used to determine if a user is authorised for certain routes (see endpoints).

- Relationships:
    - User:
        - One to many relationship with pilots,
        - One to many relationship with drones,
        - One to many relationship with flight logs.

**Pilot model:**

*pilot.py*

```python
from main import db

class Pilot(db.Model):
    # Define table name for db
    __tablename__= "PILOTS"

    # Set the primary key
    id = db.Column(db.Integer, primary_key=True, nullable=False)

    # Rest of attributes
    name = db.Column(db.String(50), nullable=False)
    license = db.Column(db.String(50))
    specialization = db.Column(db.String(100))

    # To be a count of flights in flight_logs, see pilots_schema.py
    flights_recorded = db.Column(db.Integer())

    # Relationships to other db
    pilot_flight_logs = db.relationship("FlightLog", backref="pilot", lazy=True)
    
    # Created by user id foreign key
    created_by_user_id = db.Column(
        db.Integer, db.ForeignKey("USERS.id"), nullable=False
        )
```

- `__tablename__` defines the table name to be mapped to the model.
- `id = db.Column(db.Integer, primary_key=True, nullable=False)` creates a column with the title ‘id’, of the integer data type. This will be the primary key for the Pilot record and will auto increment with each creation of a new Pilot. Not to be set by the user but instead looked after by SQLAlchemy. Not nullable.
- The remaining attribute fields (`name`, `license`, `specialization`, `flights_recorded`) are established, with their data type and character limit (`String()` or `Integer()`. Mandatory fields are noted by the `nullable=` clause.
- The `flights_recorded` attribute is an integer column which will keep a count of the number of flights recorded for each pilot, achieved through code within the schema file counting the number of existing instances of `pilot_flight_logs` that have a relationship with the particular pilot.
    
    Found in the file *pilots_schema.py*:
    

```python
...
flights_recorded = fields.Method("count_flight_logs")

    def count_flight_logs(self, pilot):
        return len(pilot.pilot_flight_logs)
```

- `pilot_flight_logs` is a `relationship` that establishes the one-to-many relationship between the `Pilot` model and the `FlightLog` model. This allows for the easy retrieval of all flight logs associated with a particular pilot.

- The `created_by_user_id` attribute is a foreign key that references the `id` column in the `"USERS"` table, showing which user created the pilot record. `nullable=False` clause indicates that each pilot must be created by (and associated with) a user. It has been coded to pull the user id from the current user, as seen in this code when posting a Pilot record:
    
    *pilots_controller.py:*
    

```python
...
user_id = get_jwt_identity()
user = User.query.get(user_id)
... 
pilot_fields["created_by_user_id"] = [user.id]
```

- Relationships:
    - Pilot:
        - One to many relationship with flight_logs (a pilot can have many flights),
        - Many to many relationship with drones. A drone can be flown by many different pilots and a pilot can fly many different drones).
        - Can only be created by one user.

**Drone model:**

*drone.py*

```python
from main import db

class Drone(db.Model):
    # Define the table name
    __tablename__= "DRONES"
    
    # Set the primary key. SQLALchemy to automatically set the first
    # Integer PK column thats not marked as FK as autoincrement=True
    id = db.Column(db.Integer, primary_key=True)

    # Attributes
    build_specifications = db.Column(db.String(300))
    weight_gms = db.Column(db.Integer())
    developed_by = db.Column(db.String(50), nullable=False)
    year_of_manufacture = db.Column(db.Integer(), nullable=False)
    last_service = db.Column(db.Date())

    # Relationships to other db
    drones_flight_logs = db.relationship("FlightLog", backref="drones", lazy=True)

    # Created by user id foreign key column
    created_by_user_id = db.Column(
        db.Integer, db.ForeignKey("USERS.id"), nullable=False
        )
```

- `__tablename__` defines the table name to be mapped to the model.
- `id = db.Column(db.Integer, primary_key=True)` creates a column with the title ‘id’, of the integer data type. This will be the primary key for the Drone record and will auto increment with each creation of a new Drone. Not to be set by the user but instead looked after by SQLAlchemy.
- The remaining attribute fields (`build_specifications`, `weight_gms`, `developed_by`, `year_of_manufacture`, `last_service`) are established, with their data type and character limit (`String()`, `Integer()`, or `Date()`). Mandatory fields are noted by the `nullable=` clause.
- `drones_flight_logs` is a `relationship` that establishes the one-to-many relationship between the `Drone` model and the `FlightLog` model. This allows for the easy retrieval of all flight logs associated with a particular drone.
- The `created_by_user_id` attribute is a foreign key that references the `id` column in the `USERS` table, showing which user created the drone record. `nullable=False` clause indicates that each drone must be created by (and associated with) a user. It has been coded to pull the user id from the current user, as seen in this code when posting a Drone record:
    
    *drones_controller.py*:
    

```python
...
user_id = get_jwt_identity()
user = User.query.get(user_id)
... 
drone_fields["created_by_user_id"] = [user.id]
```

- Relationships:
    - Drone:
        - One to many relationship with flight_logs (a drone can be associated with many flight logs),
        - Many to many relationship with pilots. A drone can be flown by many different pilots and a pilot can fly many different drones.
        - Can only be created by one user.

**FlightLog model:**

A flight log model is to be posted by a user, and contains the foreign key information of the associated drone id, pilot id and the user which posted the flight log.

*flight_log.py*

```python
from main import db
from marshmallow import fields

class FlightLog(db.Model):
    # Define the table name for the db
    __tablename__= "FLIGHT_LOGS"
    
    # Set primary key
    id = db.Column(db.Integer, primary_key=True) 

    # Attributes
    flight_date = db.Column(db.Date, nullable=False)
    flight_time = db.Column(db.Time, nullable=False)
    flight_location = db.Column(db.String(100), nullable=False)
    flight_minutes = db.Column(db.Integer(), nullable=False) 
    footage_recorded = db.Column(db.Boolean(), nullable=False)

    # Must be between 1 - 10 (see flight_logs_schema.py)
    flight_performance_rating_of_10 = db.Column(db.Integer(), nullable=False)

    # Foreign key attributes
    drone_id = db.Column(
        db.Integer(), db.ForeignKey("DRONES.id",), nullable=False
        )
    pilot_id = db.Column(
        db.Integer(), db.ForeignKey("PILOTS.id"), nullable=False
        )
    posted_by_user = db.Column(
        db.Integer(), db.ForeignKey("USERS.id"), nullable=False
        )
    
    # Included as bridge to show intention to automate the attribute fields data (date, time, location, duration can be pulled information)
    footage_recorded = fields.Boolean(load_default=False)
```

- `__tablename__` defines the table name to be mapped to the model.
- `id = db.Column(db.Integer, primary_key=True)` creates a column with the title ‘id’, of the integer data type. This will be the primary key for the FlightLog record and will auto increment with each creation of a new FlightLog. Not to be set by the user but instead looked after by SQLAlchemy.
- The remaining attribute fields (`flight_date`, `flight_time`, `flight_location`, `flight_minutes`, `footage_recorded`, `flight_performance_rating_of_10`) are established, with their data type and character limit (`Date()`, `Time()`, `String()`, `Integer()`, `Boolean()`, `Integer()`). Mandatory fields are noted by the `nullable=` clause.
- The `footage_recorded` attribute is a boolean column that indicates whether footage was recorded during the flight or not. `load_default=False` indicates that if this field is not included when creating a new FlightLog, it will default to `False`.
- The `flight_performance_rating_of_10` attribute is an integer column that must be between 1 and 10, and is validated against logic within the flight log schema.
    
    **flight_logs_schema.py:*
    
    ```python
    ...
    def validate_flight_performance_rating_of_10(value):
            if not (1 <= value <= 10):
                raise ValueError('Flight performance rating must be between 1 and 10.')
            
    
        flight_performance_rating_of_10 = fields.Integer(
            validate=validate_flight_performance_rating_of_10,
            required=True
        )
    ```
    
- The foreign key attributes (`drone_id`, `pilot_id`, `posted_by_user`) reference the `id` column of the respective tables (`DRONES`, `PILOTS`, `USERS`) and show which drone, pilot, and user created the FlightLog record. `nullable=False` indicates that each FlightLog must be associated with a drone, pilot, and user. It has been coded to pull the user id from the current user, as seen in this code when posting a FlightLog record:
    
    *flight_logs_controller.py:*
    

```python
...
user_id = get_jwt_identity()
user = User.query.get(user_id)
... 
flight_log_fields["created_by_user_id"] = [user.id]
```

- Relationships:
    - FlightLog:
        - Stores the information.
        - One flight log can be associated with only one drone, pilot and user at a time, however drones, pilots or users may have many different flight logs.


## R9 - Discuss the database relations to be implemented in your application <a name="req9"></a>

Please see the ERD in R6 for further understanding of the relations that were to be implemented as part of planning for the build of the application.

The relations between each entity are visually shown on the ERD.

Example fields are included in the tables, with their data type and condition. The format is:

`field` `data type(characterlimit)` `condition`

eg. `email charvar(100) NOT NULL unique`

Each table contains an integer type primary key (PK). 

User relationships:

- The users table has a user_id of integer data type which will be the primary key.
- The users table has a one-to-many relationship with the drone, flight_log and pilots table. Denoted by the single lined connecter attached to the users table, and the multi-lined connector that is touching the drone, flight_log and pilots table.
- One user can be associated with many drone, pilot, or flight_log records.
- A drone, pilot, or flight_log record may only be associated with one user.

Flight Log relationships:

- The flight_log table has a flight_id of integer data type which will be the primary key.
- It also has the foreign key values drone_id, pilot_id and posted_by_user_id which are to be the associated drone, pilot and user record.
- The flight_log table has a many-to-one relationship with the users, drones and pilots table. Denoted by the multi-lined connector attached to the flight_log table, and the single-lined connector that is touching the users, drones and pilots tables.
- Many flight logs can be associated with one user, drone or pilot.
- A single user, drone or pilot record may be associated with many flight log records.

Drones relationships:

- The drones table has a drone_id of integer data type which will be the primary key.
- The drones table has a one-to-many relationship with flight logs. Denoted by the single lined connector attached to the drones table and the multi-lined end of the connector attached to the flight_log table.
- The drones table has a many-to-one relationship with users. Denoted by the multi-lined end of the connector attached to the drones table and the single lined end of the connector attached to the users table.
- One drone can be associated with many flight logs. (A flight log can be associated with one drone)
- Many drones can be created by one user.  (A drone can only be created by one user)
- Drones have a many-to-many relationship with pilots, with the flight_log table acting as a join table.
- Many pilots can fly many drones, and many drones can be flown by many pilots.

Pilots relationships:

- The pilots table has a pilot_id of integer data type which will be the primary key.
- The pilots table has a one-to-many relationship with flight logs. Denoted by the single lined connector attached to the pilots table and the multi-lined end of the connector attached to the flight_log table.
- The pilots table has a many-to-one relationship with users. Denoted by the multi-lined end of the connector attached to the drones table and the single lined end of the connector attached to the users table.
- One pilot can be associated with many flight logs. (A flight log can be associated with one pilot)
- Many pilots can be created by one user. (A pilot can only be created by one user)
- Pilots have a many-to-many relationship with drones, with the flight_log table acting as a join table.
- Many pilots can fly many drones, and many drones can be flown by many pilots.


## R10 - Describe the way tasks are allocated and tracked in your project <a name="req10"></a>
- Trello (ongoing)

## R5 - Document all endpoints for your API <a name="req5"></a>

## ENDPOINTS

Endpoints are presented in the following format:

### Route: “/”

- **Method:**
- `@decorator`
- Functionality:
- Admin required:
- Local host URL:
- JSON Body:
- *Example expected response:*

**Local host URL may be localhost:5000/ or alternatively, http://127.0.0.1:5000/  in a browser.**

**All actions require that the user is logged in.** 

**/<int:value> -  Enter the integer id value** 

*(eg. for User with id: 1  |  <int:id> = 1)*

**/<string:value> - Enter the value that matches the ‘value’ field. Use `%20` in as a space** 

*(eg. with reference to the name John Example  |  <string:name> = John%20Example).* 

### 

## Auth:

## URL prefix = “/auth”

### Route: “/register”

- **Method: POST**
- `@auth.route("/register", methods=["POST"])`
- Functionality: Creates a new user. `"is_admin"` field is not required and defaults to `"false"` unless specified.
- Admin required: No
- Local host URL: localhost:5000/auth/register
- JSON Body (example user **without** admin privileges):

```json
{
	"email": "[user@gmail.com](mailto:auth_test@gmail.com)",
	"username":"Test user",
	"password": "password123"
}
```

- *Expected response includes encrypted password token (JWT):*

```json
{
	"is_admin": false,
	"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY3OTkwMTQ0NywianRpIjoiZTQ3Y2I2NWItZjZhMC00MDYwLWFhZDctNWJhZTdmY2U4MTIyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjMiLCJuYmYiOjE2Nzk5MDE0NDcsImV4cCI6MTY3OTk4Nzg0N30.dxqaeNisNF87_ENFkxD-OC4BG0p89veooZtDi8K6VHI",
	"user email": "[user@gmail.com](mailto:test_user@gmail.com)",
	"username": "Test user"
}
```

- JSON Body (example user **with** admin privileges):

```json
{
	"email": "[admin@gmail.com](mailto:test_admin@gmail.com)",
	"username":"Test admin user",
	"password": "password123",
	"is_admin": true
}
```

- *Expected response:*

```json
{
	"is_admin": true,
	"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY3OTkwMTY1NiwianRpIjoiZTQ0YjJkNzAtYmJlZS00MTFjLWExYmItNTk4YmQzMGNjZjljIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjQiLCJuYmYiOjE2Nzk5MDE2NTYsImV4cCI6MTY3OTk4ODA1Nn0.M5MYmst-FihPKOy1PFQIyb6CyDSSWseq8d0jhuDuSwE",
	"user email": "[admin@gmail.com](mailto:test_admin@gmail.com)",
	"username": "Test admin user"
}
```

### Route: “/login”

- **Method: POST**
- `@auth.route("/login", methods=["POST"])`
- Functionality: User login. Requires `"email"` and `"password"`.
- Admin required: No
- Local host URL: localhost:5000/auth/login
- JSON body:

```json
{
	"email": "[admin@gmail.com](mailto:admin@gmail.com)",
	"password": "password123"
}
```

-*Expected response returns the user’s email address and encrypted password token (JWT):*

```json
{
	"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY3OTkwMTg0MywianRpIjoiODFkYTEwZmItZTFhYy00NzQ3LTk0NDMtNTE1NDc0ZjEwYzM5IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjIiLCJuYmYiOjE2Nzk5MDE4NDMsImV4cCI6MTY3OTk4ODI0M30.djf2NN5VC_JUDsY6v5hmIDvAWaDhbAUEXkgdO1gcang",
	"user": "[admin@gmail.com](mailto:admin@gmail.com)"
}
```

## Users:

## URL prefix = “/users”

### Route: “/”

- **Method: GET**
- `@user.route("/", methods=["GET"])`
- Functionality: Returns a list of all users.
- Admin required: No
- Localhost URL: localhost:5000/users
- JSON Body: None
- *Example expected response:*

```python
[
	{
		"email": "[user@gmail.com](mailto:user@gmail.com)",
		"id": 1,
		"is_admin": false,
		"password": "$2b$12$nI8ulvyF1wpX6IZsiDclBOQVgyeZWqaGhEfszdtiY/nQm0rOdRZEq",
		"username": "Test user"
	},
	{
		"email": "[admin@gmail.com](mailto:admin@gmail.com)",
		"id": 2,
		"is_admin": true,
		"password": "$2b$12$mJyZPyoHXqWS48TswjOSxutx8dGrDYivLSz4g6Ggr2oThqoKqFQVq",
		"username": "Test admin user"
	}
]
```

### Route: “/<int:id>”

- **Method: GET**
- `@user.route("/<int:id>", methods=["GET"])`
- Functionality: Return a user specified by id.
- Admin required: No
- Local host URL: localhost:5000/users/<int:id>
- JSON Body: None
- *Example expected response when searching for user with id: 1, localhost:5000/users/1:*

```python
{
	"email": "[user@gmail.com](mailto:user@gmail.com)",
	"id": 1,
	"is_admin": false,
	"password": "$2b$12$nI8ulvyF1wpX6IZsiDclBOQVgyeZWqaGhEfszdtiY/nQm0rOdRZEq",
	"username": "Test user"
}
```

### Route: “/<int:id>”

- **Method: DELETE**
- `@user.route("/int:id", methods=["DELETE"])`
- Functionality: Deletes a user specified by id.
- Admin required: Yes
- Local host URL: localhost:5000/users/<int:id>
- JSON Body: None
- *Example expected response when deleting user with id: 1, localhost:5000/users/1*
    - *Response will show the record of the user that is deleted:*

```python
{
	"email": "[user@gmail.com](mailto:user@gmail.com)",
	"id": 1,
	"is_admin": false,
	"password": "$2b$12$bb4805qPGky03wRcebGNs.hRPdIaQPvSpzcNSFiBCA3TizG4DnMzm",
	"username": "Test user"
}
```

## Drones:

## URL prefix = “/drones”

### Route: “/”

- **Method: GET**
- `@drone.route("/", methods=["GET"])`
- Functionality: Returns a list of all drone records.
- Admin required: No
- Local host URL: localhost:5000/drones
- JSON Body: None
- *Example expected response*

```json
[
	{
	"build_specifications": "Lightweight carbon fiber frame, high-speed brushless motors, FPV camera and transmitter, Carbon Fiber propellers, 45 LiPO battery, DRFPV software",
	"created_by_user_id": 2,
	"developed_by": "Drone Corp",
	"id": 1,
	"last_service": "2022-12-03",
	"weight_gms": 160,
	"year_of_manufacture": 2019
	},
	{
	"build_specifications": "Foldable and waterproof carbon fiber frame, 4k HD SEICA lens, Carbon Fiber propellers, 45 LiPO battery, stock software",
	"created_by_user_id": 2,
	"developed_by": "Drone Flyers Inc",
	"id": 2,
	"last_service": "2021-07-04",
	"weight_gms": 980,
	"year_of_manufacture": 2021
	}
]
```

### Route: “/<int:id>”

- **Method: GET**
- `@drone.route("/int:id", methods=["GET"])`
- Functionality: Return a drone specified by id.
- Admin required: No
- Local host URL: localhost:5000/drones/<int:id>
- JSON Body: None
- *Example expected response when searching for drone with id: 1, localhost:5000/drones/1:*

```json
{
	"build_specifications": "Lightweight carbon fiber frame, high-speed brushless motors, FPV camera and transmitter, Carbon Fiber propellers, 45 LiPO battery, DRFPV software",
	"created_by_user_id": 2,
	"developed_by": "Drone Corp",
	"id": 1,
	"last_service": "2022-12-03",
	"weight_gms": 160,
	"year_of_manufacture": 2019
}
```

### Route: “/”

- **Method: POST**
- `@drone.route("/", methods=["POST"])`
- Functionality: Creates a drone record.
- Admin required: Yes
- Local host URL: localhost:5000/drones
- JSON Body:

```json
{
	"build_specifications": "Example drone",
	"weight_gms": "1595",
	"developed_by": "XYZ Co",
	"year_of_manufacture": "2018",
	"last_service": "2022, 12 03"
}
```

- *The expected response will be the same as the JSON Body input, plus additional fields of an assigned `"id"` and `"created_by_user_id"`:*

```json
{
	"build_specifications": "Example drone",
	"created_by_user_id": 2,
	"developed_by": "XYZ Co",
	"id": 4,
	"last_service": "2022-12-03",
	"weight_gms": 1595,
	"year_of_manufacture": 2018
}
```

### Route: “/<int:id>”

- **Method: PUT**
- `@drone.route("/int:id", methods=["PUT"])`
- Functionality: Update a drone record, specified by id.
- Admin required: Yes
- Local host URL: localhost:5000/drones/<int:id>
- JSON Body:

```json
{
	"build_specifications": "Fuller drone",
	"weight_gms": "15950",
	"developed_by": "ABC Co",
	"year_of_manufacture": "2019",
	"last_service": "2023, 01 03"
}
```

- *The expected response will be the same as the JSON Body input, plus additional fields of the drones `"id"` and its assigned`"created_by_user_id"`:*

```json
{
	"build_specifications": "Fuller drone",
	"created_by_user_id": 2,
	"developed_by": "ABC Co",
	"id": 2,
	"last_service": "2023-01-03",
	"weight_gms": 15950,
	"year_of_manufacture": 2019
}
```

### Route: “/<int:id>”

- **Method: PATCH**
- `@drone.route("/int:id", methods=["PATCH"])`
- Functionality: Update a drone’s “last_service” field, specified by id.
- Admin required: Yes
- Local host URL: localhost:5000/<int:id>
- JSON Body:

```json
{
	"last_service": "2023, 01 04"
}
```

- *The expected response will be the specified drones record, with the updated `"last_service"` field.*

```json
{
	"build_specifications": "Fuller drone",
	"created_by_user_id": 2,
	"developed_by": "ABC Co",
	"id": 2,
	"last_service": "2023-01-04",
	"weight_gms": 15950,
	"year_of_manufacture": 2019
}
```

### Route: “/<int:id>”

- **Method: DELETE**
- `@drone.route("/<int:id>", methods=["DELETE"])`
- Functionality: Delete a drone record, specified by id.
- Admin required: Yes
- Local host URL: localhost:5000/drones/<int:id>
- JSON Body: None
- *The expected response is the record of the drone that is deleted. Example expected response when deleting drone with id: 2, localhost:5000/drones/2:*

```json
{
	"build_specifications": "Fuller drone",
	"created_by_user_id": 2,
	"developed_by": "ABC Co",
	"id": 2,
	"last_service": "2023-01-04",
	"weight_gms": 15950,
	"year_of_manufacture": 2019
}
```

## Pilots:

## URL prefix = “/pilots”

### Route: “/”

- **Method: POST**
- `@pilot.route("/", methods=["POST"])`
- Functionality: Creates a pilot record.
- Admin required: Yes
- Local host URL: localhost:5000/pilots
- JSON Body:

```json
{
	"name": "John Example",
	"license": "Drone Pilots NSW",
	"specialization": "Site inspections (engineering)"
}
```

- *The expected response will be the same as the JSON Body input, plus additional fields of the flight_logs linked* `"flights_recorded"`, *an assigned* `"id"` *and* `"created_by_user_id"`*:*

```json
{
	"created_by_user_id": 2,
	"flights_recorded": 0,
	"id": 1,
	"license": "Drone Pilots NSW",
	"name": "John Example",
	"specialization": "Site inspections (engineering)"
}
```

### Route: “/”

- **Method: GET**
- `@pilot.route("/", methods=["GET"])`
- Functionality: Returns a list of all pilot’s records.
- Admin required: No
- Local host URL: localhost:5000/pilots
- JSON Body: None
- *Example expected response*

```json
[
	{
		"created_by_user_id": 2,
		"flights_recorded": 0,
		"id": 1,
		"license": "Drone Pilots NSW",
		"name": "John Example",
		"specialization": "Site inspections (engineering)"
	},
	{
		"created_by_user_id": 2,
		"flights_recorded": 2,
		"id": 2,
		"license": "Drone Pilots NSW",
		"name": "Vera Craig",
		"specialization": "Nature photography"
	},
	{
		"created_by_user_id": 2,
		"flights_recorded": 6,
		"id": 3,
		"license": "Degen Drones VIC",
		"name": "Johnathan Kihan",
		"specialization": "Weather and site monitoring (engineering)"
	}
]
```

### Route: “/<int:id>”

- **Method: GET**
- `@pilot.route("/<int:id>", methods=["GET"])`
- Functionality: Return a pilot specified by id.
- Admin required: No
- Local host URL: localhost:5000/pilots/<int:id>
- JSON Body: None
- *Example expected response when searching for pilot with id: 2, localhost:5000/pilots/2:*

```json
{
	"created_by_user_id": 2,
	"flights_recorded": 2,
	"id": 2,
	"license": "Drone Pilots NSW",
	"name": "Vera Craig",
	"specialization": "Nature photography"
}
```

### Route: “/<string:pilot_name>”

- **Method: GET**
- `@pilot.route("/<string:pilot_name>/", methods=["GET"])`
- Functionality: Return a pilot specified by name (case sensitive). Use `%20` as a space, eg. `/John%20Example`
- Admin required: No
- Local host URL: localhost:5000/pilots/<string:pilot_name>
- JSON Body: None
- *Example expected response when searching for pilot with name “John Example”, localhost:5000/pilots/John%20Example:*

```json
{
	"created_by_user_id": 2,
	"flights_recorded": 0,
	"id": 1,
	"license": "Drone Pilots NSW",
	"name": "John Example",
	"specialization": "Site inspections (engineering)"
}
```

### Route: “/<int:id>”

- **Method: PUT**
- `@pilot.route("/<int:id>", methods=["PUT"])`
- Functionality: Update a pilot record, specified by id.
- Admin required: Yes
- Local host URL: localhost:5000/pilots/<int:id>
- JSON Body:

```json
{
"name": "John Example-Change",
"license": "Some new license",
"specialization": "Site and weather inspections (engineering)"
}
```

- *The expected response is the specified record with updated changes. It is the same as the JSON body with the additional fields of the specified* `"id"` *and the assigned* `"created_by_user_id"`. *Example expected PUT outcome of the above JSON body, localhost:5000/pilots/1:*

```json
{
	"created_by_user_id": 2,
	"flights_recorded": 0,
	"id": 1,
	"license": "Some new license",
	"name": "John Example-Change",
	"specialization": "Site and weather inspections (engineering)"
}
```

### Route: “/flights_recorded”

- **Method: GET**
- `@pilot.route("/flights_recorded", methods=["GET"])`
- Functionality: Only returns the fields `"Flights Recorded"`, `"Pilot ID"` and `"Pilot Name"`.  Streamlined view of pilots and their tally of flights recorded.
- Admin required: No
- Local host URL: localhost:5000/pilots/flights_recorded
- JSON Body:

```json
[
	{
		"Flights Recorded": 0,
		"Pilot ID": 1,
		"Pilot Name": "John Example"
	},
	{
		"Flights Recorded": 6,
		"Pilot ID": 2,
		"Pilot Name": "Johnathan Kihan"
	},
	{
		"Flights Recorded": 2,
		"Pilot ID": 3,
		"Pilot Name": "James Daniels"
	}
]
```

### Route: “/<int:id>”

- **Method: DELETE**
- `@pilot.route("/<int:id>", methods=["DELETE"])`
- Functionality: Delete a pilot record, specified by id.
- Admin required: Yes
- Local host URL: localhost:5000/pilot/<int:id>
- JSON Body: None
- *The expected response is the record of the pilot that is deleted. Example expected response when deleting pilot with id: 1, localhost:5000/pilots/1:*

```json
{
	"created_by_user_id": 2,
	"flights_recorded": 0,
	"id": 1,
	"license": "Drone Pilots NSW",
	"name": "John Example",
	"specialization": "Site inspections (engineering)"
}
```

## Flight Logs:

## URL prefix = “/flight_logs”

### Route: “/”

- **Method: POST**
- `@flight_log.route("/", methods=["POST"])`
- Functionality: Post a flight log. Fields to be posted:
    - `"flight_date"`
    - `"flight_time"`
    - `"flight_location"`
    - `"flight_minutes"`
    - `"flight_performance_rating_of_10"`
    - `"footage_recorded"`
- Also to include the foreign key values for the associated drone and pilot.
    - `"drone_id"`
    - `"pilot_id"`
- Admin required: No
- Local host URL: localhost:5000/flight_logs
- JSON Body:

```json
[
	{
		"drone_id": 3,
		"flight_date": "2023-01-17",
		"flight_location": "Maddens Plains, NSW",
		"flight_minutes": 26,
		"flight_performance_rating_of_10": 8,
		"flight_time": "14:22:00",
		"footage_recorded": true,
		"pilot_id": 1,
	}
]
```

- *Expected result is the JSON body request with additional fields of the assigned flight_log* `"id"` and the id of the user that posted the log, represented as `"posted_by_user”`:

```json
[
	{
		"drone_id": 3,
		"flight_date": "2023-01-17",
		"flight_location": "Maddens Plains, NSW",
		"flight_minutes": 26,
		"flight_performance_rating_of_10": 8,
		"flight_time": "14:22:00",
		"footage_recorded": true,
		"id": 1,
		"pilot_id": 1,
		"posted_by_user": 1
	}
]
```

### Route: “/”

- **Method: GET**
- `@flight_log.route("/", methods=["GET"])`
- Functionality: Returns a list of all flight logs.
- Admin required: No
- Local host URL: localhost:5000/flight_logs
- JSON Body: None
- *Example expected response:*

```json
[
	{
		"drone_id": 3,
		"flight_date": "2023-01-17",
		"flight_location": "Maddens Plains, NSW",
		"flight_minutes": 26,
		"flight_performance_rating_of_10": 8,
		"flight_time": "14:22:00",
		"footage_recorded": true,
		"id": 1,
		"pilot_id": 1,
		"posted_by_user": 1
	},
	{
		"drone_id": 1,
		"flight_date": "2023-01-29",
		"flight_location": "Hyde Park, Sydney, NSW 2000",
		"flight_minutes": 12,
		"flight_performance_rating_of_10": 9,
		"flight_time": "18:30:00",
		"footage_recorded": true,
		"id": 2,
		"pilot_id": 4,
		"posted_by_user": 1
	}
]
```

### Route: “/<int:id>”

- **Method: GET**
- `@flight_log.route("/<int:id>", methods=["GET"])`
- Functionality: Returns a flight log specified by id.
- Admin required: No
- Local host URL: localhost:5000/flight_logs/<int:id>
- JSON Body: None
- *Example expected response when searching for flight_log with id: 1, localhost:5000/flight_logs/1:*

```json
{
	"drone_id": 3,
	"flight_date": "2023-01-17",
	"flight_location": "Maddens Plains, NSW",
	"flight_minutes": 26,
	"flight_performance_rating_of_10": 8,
	"flight_time": "14:22:00",
	"footage_recorded": true,
	"id": 1,
	"pilot_id": 1,
	"posted_by_user": 1
}
```

### Route: “/drones”

- **Method: GET**
- `@flight_log.route("/", methods=["GET"])`
- Functionality: Returns a condensed list of all flight logs, only displaying the `"Drone ID"` and `"Flight ID"` fields.
- Admin required: No
- Local host URL: localhost:5000/flight_logs/drones
- JSON Body: None
- *Example expected response:*

```json
[
	{
		"Drone ID": 3,
		"Flight ID": 1
	},
	{
		"Drone ID": 1,
		"Flight ID": 2
	}
]
```

### Route: “/drones/more”

- **Method: GET**
- `@flight_log.route("/drones/more", methods=["GET"])`
- Functionality: Returns a list of all flight logs, displaying the `"Drone ID"` and `"Flight ID"` fields, as well as additional fields of `"Flight Date"`, `"Flown by Pilot ID"`, `"Pilot Name"` and `"Location"`. Extension of `/drones` route. Displays same data as the flight_logs `/pilots` route with different endpoint for smoother flow of displaying data (utilising the condensed `/` list, `id` specification, `/more` and `/full` endpoints).
- Admin required: No
- Local host URL: localhost:5000/flight_logs/drones/more
- JSON Body: None
- *Example expected response:*

```json
[
	{
		"Drone ID": 3,
		"Flight Date": "Tue, 17 Jan 2023 00:00:00 GMT",
		"Flight ID": 1,
		"Flown by Pilot ID": 1,
		"Location": "Maddens Plains, NSW",
		"Pilot name": "John Example"
	},
	{
		"Drone ID": 1,
		"Flight Date": "Sun, 29 Jan 2023 00:00:00 GMT",
		"Flight ID": 2,
		"Flown by Pilot ID": 4,
		"Location": "Hyde Park, Sydney, NSW 2000",
		"Pilot name": "James Daniels"
  }
]
```

### Route: “/drones/<int:drone_id>”

- **Method: GET**
- `@flight_log.route("/drones/<int:drone_id>", methods=["GET"])`
- Functionality: Returns a condensed list of all flight logs flown by a particular drone, specified by the drones id. Only returns the fields `"Drone ID"` and `"Flight ID"`.
- Admin required: No
- Local host URL: localhost:5000/flight_logs/drones/<int:drone_id>
- JSON Body: None
- *Example expected response when searching for flight_logs that are linked with drone id: 1, localhost:5000/flight_logs/drones/1:*

```json
[
	{
		"Drone ID": 1,
		"Flight ID": 2
	}
]
```

### Route: “/drones/<int:drone_id>/more”

- **Method: GET**
- `@flight_log.route("/drones/<int:drone_id>/more", methods=["GET"])`
- Functionality: Returns a list of all flight logs flown by a particular drone, specified by the drones id. Only returns the fields `"Drone ID"`, `"Flight ID"`, `"Flight Date"`, `"Flown by pilot ID"`, `"Location"`.
- Admin required: No
- Local host URL: localhost:5000/flight_logs/drones/<int:drone_id>/more
- JSON Body: None
- *Example expected response when searching for flight_logs that are linked with drone id: 1, localhost:5000/flight_logs/drones/1/more:*

```json
[
	{
		"Drone ID": 1,
		"Flight Date": "Sun, 29 Jan 2023 00:00:00 GMT",
		"Flight ID": 2,
		"Flown by Pilot ID": 4,
		"Location": "Hyde Park, Sydney, NSW 2000"
	}
]
```

### Route: “/drones/<int:drone_id>/full”

- **Method: GET**
- `@flight_log.route("/drones/<int:id>/full", methods=["GET"])`
- Functionality: Returns a list of all flight logs flown by a particular drone, specified by the drones id. Returns all `flight_logs` fields.
- Admin required: No
- Local host URL: localhost:5000/flight_logs/drones/<int:drone_id>/full
- JSON Body: None
- *Example expected response when searching for flight_logs that are linked with drone id: 1, localhost:5000/flight_logs/drones/1/full:*

```json
[
	{
		"drone_id": 1,
		"flight_date": "2023-01-29",
		"flight_location": "Hyde Park, Sydney, NSW 2000",
		"flight_minutes": 12,
		"flight_performance_rating_of_10": 9,
		"flight_time": "18:30:00",
		"footage_recorded": true,
		"id": 2,
		"pilot_id": 4,
		"posted_by_user": 1
	}
]
```

### Route: “/pilots”

- **Method: GET**
- `@flight_log.route("/pilots", methods=["GET"])`
- Functionality: Returns a condensed list of all flight logs, only displaying the `"Pilot ID"` and `"Flight ID"` fields. Pulls `"Pilot Name"` from pilots record.
- Admin required: No
- Local host URL: localhost:5000/flight_logs/pilots
- JSON Body: None
- *Example expected response:*

```json
[
	{
		"Flight ID": 1,
		"Pilot ID": 1,
		"Pilot Name": "John Example"
	},
	{
		"Flight ID": 2,
		"Pilot ID": 4,
		"Pilot Name": "James Daniels"
	}
]
```

### Route: “/pilots/more”

- **Method: GET**
- `@flight_log.route("/pilots/more", methods=["GET"])`
- Functionality: Returns a list of all flight logs, displaying the `"Pilot ID"`,  `"Flight ID"`, and `"Pilot Name"` fields, as well as additional fields of `"Flight Date"`, `"Location"` and `"Drone ID"`. Extension of `/pilots` route. Displays same data as the flight_logs `/drones` route with different endpoint for smoother flow of displaying data (utilising the condensed `/` list, `id` specification, `/more` and `/full` endpoints).
- Admin required: No
- Local host URL: localhost:5000/flight_logs/pilots
- JSON Body: None
- *Example expected response:*

```json
[
	{
		"Drone ID": 3,
		"Flight Date": "Tue, 17 Jan 2023 00:00:00 GMT",
		"Flight ID": 1,
		"Pilot ID": 1,
		"Location": "Maddens Plains, NSW",
		"Pilot name": "John Example"
	},
	{
		"Drone ID": 1,
		"Flight Date": "Sun, 29 Jan 2023 00:00:00 GMT",
		"Flight ID": 2,
		"Pilot ID": 4,
		"Location": "Hyde Park, Sydney, NSW 2000",
		"Pilot name": "James Daniels"
	}
]
```

### Route: “/pilots/<int:pilot_id>”

- **Method: GET**
- `@flight_log.route("/pilots/<int:pilot_id>", methods=["GET"])`
- Functionality: Returns a condensed list of all flight logs flown by a particular pilot, specified by the pilots id. Only returns the fields `"Pilot ID"`, `"Flight ID"` and pulls the `"Pilot Name"` field from the associated pilots record.
- Admin required: No
- Local host URL: localhost:5000/flight_logs/pilots/<int:pilot_id>
- JSON Body: None
- *Example expected response when searching for flight_logs that are linked with pilot id: 4, localhost:5000/flight_logs/pilots/4:*

```json
[
	{
		"Flight ID": 2,
		"Pilot ID": 4,
		"Pilot Name": "James Daniels"
	},
	{
		"Flight ID": 5,
		"Pilot ID": 4,
		"Pilot Name": "James Daniels"
	}
]
```

### Route: “/pilots/<int:pilot_id>/more”

- **Method: GET**
- `@flight_log.route("/pilots/<int:pilot_id>/more", methods=["GET"])`
- Functionality: Returns a list of all flight logs flown by a particular pilot, specified by the drones id. Only returns the fields `"Pilot ID"`, `"Flight ID"`, `"Pilot Name"`, `"Flight Date"`, `"Drone ID"`, `"Location"`.
- Admin required: No
- Local host URL: localhost:5000/flight_logs/pilots/<int:pilot_id>/more
- JSON Body: None
- *Example expected response when searching for flight_logs that are linked with pilot id: 4, localhost:5000/flight_logs/pilots/4/more:*

```json
[
	{
		"Drone ID": 1,
		"Flight Date": "Sun, 29 Jan 2023 00:00:00 GMT",
		"Flight ID": 2,
		"Location": "Hyde Park, Sydney, NSW 2000",
		"Pilot ID": 4,
		"Pilot Name": "James Daniels"
	},
	{
		"Drone ID": 1,
		"Flight Date": "Sun, 26 Feb 2023 00:00:00 GMT",
		"Flight ID": 5,
		"Location": "Kembla Grange Racetrack, Illawarra region NSW",
		"Pilot ID": 4,
		"Pilot Name": "James Daniels"
	}
]
```

### Route: “/pilots/<int:pilot_id>/full”

- **Method: GET**
- `@flight_log.route("/pilots/<int:pilot_id>/full", methods=["GET"])`
- Functionality: Returns a list of all flight logs flown by a particular pilot, specified by the pilots id. Returns all `flight_logs` fields.
- Admin required: No
- Local host URL: localhost:5000/flight_logs/pilots/<int:pilot_id>/full
- JSON Body: None
- *Example expected response when searching for flight_logs that are linked with pilot id: 4, localhost:5000/flight_logs/pilots/4/full:*

```json
[
	{
		"drone_id": 1,
		"flight_date": "2023-01-29",
		"flight_location": "Hyde Park, Sydney, NSW 2000",
		"flight_minutes": 12,
		"flight_performance_rating_of_10": 9,
		"flight_time": "18:30:00",
		"footage_recorded": true,
		"id": 2,
		"pilot_id": 4,
		"posted_by_user": 1
	},
	{
		"drone_id": 1,
		"flight_date": "2023-02-26",
		"flight_location": "Kembla Grange Racetrack, Illawarra region NSW",
		"flight_minutes": 15,
		"flight_performance_rating_of_10": 8,
		"flight_time": "11:45:00",
		"footage_recorded": true,
		"id": 5,
		"pilot_id": 4,
		"posted_by_user": 1
	}
]
```

### Route: “/dp_flights”

- **Method: GET**
- `@flight_log.route("/dp_flights", methods=["GET"])`
- Functionality: (Drone Pilot flights) returns a list of all flight logs, displaying  the`"Drone ID"`, `"Pilot ID"`, and `"Flight ID"` of the flight, and pulls `"Pilot Name"` from the pilots record.
- Admin required: No
- Local host URL: localhost:5000/flight_logs/dp_flights
- JSON Body: None
- *Example expected response*

```json
[
	{
		"Drone ID": 3,
		"Flight ID": 1,
		"Pilot ID": 1,
		"Pilot Name": "John Example"
	},
	{
		"Drone ID": 1,
		"Flight ID": 2,
		"Pilot ID": 4,
		"Pilot Name": "James Daniels"
	}
]
```

### Route: “/dp_flights/drones/<int:drone_id>”

- **Method: GET**
- `@flight_log.route("/dp_flights/drones/<int:drone_id>", methods=["GET"])`
- Functionality: Returns a list of all flight logs with a relationship to a specific drone, displaying the  `"Drone ID"` and `"Pilot ID"` and the  `"Flight ID"` of the flight, specified by the drone id.
- Admin required: No
- Local host URL: localhost:5000/flight_logs/dp_flights/drones/<int:drone_id>
- JSON Body: None
- *Example expected response, displaying drone pilot flight_logs information with drone id: 3, localhost:5000/flight_logs/dp_flights/drones/3*

```json
[
	{
		"Drone ID": 3,
		"Flight ID": 1,
		"Pilot ID": 1
	}
]
```

### Route: “/dp_flights/pilots/<int:pilot_id>”

- **Method: GET**
- `@flight_log.route("/dp_flights/pilots/<int:pilot_id>", methods=["GET"])`
- Functionality: Returns a list of all flight logs with a relationship to a specific pilot, displaying the  `"Drone ID"` and `"Pilot ID"` and the  `"Flight ID"` of the flight, specified by the pilot id.
- Admin required: No
- Local host URL: localhost:5000/flight_logs/dp_flights/pilots/<int:pilot_id>
- JSON Body: None
- *Example expected response, displaying drone pilot flight_logs information with pilot id: 1, localhost:5000/flight_logs/dp_flights/pilots/1*

```json
[
	{
		"Drone ID": 3,
		"Flight ID": 1,
		"Pilot ID": 1
	}
]
```

### Route: “/dp_flights/dp/<int:drone_id>/and/<int:pilot_id>”

- **Method: GET**
- `@flight_log.route("/dp_flights/dp/<int:drone_id>/and/<int:pilot_id>", methods=["GET"])`
- Functionality: Returns a list of all flight logs pertaining to a specific drone and pilot relationship, displaying the  `"Drone ID"` and `"Pilot ID"` and the  `"Flight ID"` of the flight, specified by both the pilot id and drone id.
- Admin required: No
- Local host URL: localhost:5000/flight_logs/dp_flights/dp/<int:drone_id>/and/<int:pilot_id>
- JSON Body: None
- *Example expected response, displaying drone pilot flight_logs information with pilot id: 1, localhost:5000/flight_logs/dp_flights/pilots/1*

```json
[
	{
		"Drone ID": 3,
		"Flight ID": 1,
		"Pilot ID": 1
	}
]
```

### Route: “/<int:id>”

- **Method: PUT**
- `@flight_log.route("/<int:id>", methods=["PUT"])`
- Functionality: Update a flight log. Fields to be posted:
    - `"flight_date"`
    - `"flight_time"`
    - `"flight_location"`
    - `"flight_minutes"`
    - `"flight_performance_rating_of_10"`
    - `"footage_recorded"`
- Also to include the foreign key values for the associated drone and pilot.
    - `"drone_id"`
    - `"pilot_id"`
- Admin required: Yes
- Local host URL: localhost:5000/flight_logs/<int:id>
- JSON Body:

```json
[
	{
		"drone_id": 1,
		"flight_date": "2023-01-17",
		"flight_location": "Maddens Plains, NSW",
		"flight_minutes": 22,
		"flight_performance_rating_of_10": 6,
		"flight_time": "14:52:00",
		"footage_recorded": true,
		"pilot_id": 2,
	}
]
```

- *Expected result is the updated JSON body request with additional fields of the assigned flight_log `"id"` and the id of the user that posted the log, represented as `"posted_by_user”`. localhost:5000/flight_logs/1:*

```json
[
	{
		"drone_id": 1,
		"flight_date": "2023-01-17",
		"flight_location": "Maddens Plains, NSW",
		"flight_minutes": 22,
		"flight_performance_rating_of_10": 6,
		"flight_time": "14:52:00",
		"footage_recorded": true,
		"id": 1,
		"pilot_id": 2,
		"posted_by_user": 1
	}
]
```

### Route: “/<int:id>”

- **Method: DELETE**
- `@flight_log.route("/<int:id>", methods=["DELETE"])`
- Functionality: Delete a pilot record, specified by id.
- Admin required: Yes
- Local host URL: localhost:5000/flight_logs/<int:id>
- JSON Body: None
- *The expected response is the record of the flight_log that is deleted. Example expected response when deleting flight_log with id: 1, localhost:5000/flight_log/1:*

[
	{
		"drone_id": 1,
		"flight_date": "2023-01-17",
		"flight_location": "Maddens Plains, NSW",
		"flight_minutes": 22,
		"flight_performance_rating_of_10": 6,
		"flight_time": "14:52:00",
		"footage_recorded": true,
		"id": 1,
		"pilot_id": 2,
		"posted_by_user": 1
	}
]