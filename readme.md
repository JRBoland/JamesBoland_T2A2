# THIS PROJECT IS A WORK IN PROGRESS.

## R1 - Identification of the problem you are trying to solve by building this particular app.

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

With this, an organisation or individual or group of hobbyists can keep a track on which pilot flew which drone whilst also having a log of further details of the flight that may be tailored to their needs(??).

________________________

-- advancements in tech, more uses for drones
-- constantly break, modular builds,
-- test the performance of the builds
-- log to assist with file storage with drones (footage etc)
-- business related, drone and pilot responsibility
-- personal log for the keen hobbyist

## R2 - Why is it a problem that needs solving?

(mention how theyre in the military too maybe)
With great advancements in its space over the last decade, drones have seen a great rise in popularity across various different fields. Beyond the recognised instances of using a drone to record footage of nature or sports, it's common to see they're now being used for further business-related purposes such as recording weddings or real estate/construction site inspections. Beyond filming footage, they're also being used to transport small goods, monitor weather conditions, or even race in a competitive setting. There is a demand for drones that are custom built for certain purposes. 

Additionally, the culture of 'modular' drones has seen a great rise (though mainly in the racing scene), with a following of keen hobbyists and engineers mixing and matching parts to build their own custom drone. From this it can be seen how keeping a record of how these custom drones, built to their missions objective, can prove useful for its users. Whether in a business or as an individual hobbyist, keeping logs can prove useful for various different reasons;

- To keep records of the date, time and location of the flight
- To have a means of recording a drones performance in certain conditions
- To keep a tally on which footage was recorded where, and when
- To log which pilot flew the drone for a certain flight


## R3 - Why have you chosen this database system. What are the drawbacks compared to others?

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

## R4 - Identify and discuss the key functionalities and benefits of an ORM

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

Ongoing

## R6 - An ERD for your app

![T2A2-ERD](./docs/T2A2%20ERD.png)


## R7 - Detail any third party services that your app will use

Ongoing2

## R8 - Describe your projects models in terms of the relationships they have with each other

- user
- pilot
- drone
- flight log


## R9 - Discuss the database relations to be implemented in your application

Ongoing


## R10 - Describe the way tasks are allocated and tracked in your project
- trello


