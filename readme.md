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

-postgresql, advantages of postgresql. familiar syntax
WKB2

## R4 - Identify and discuss the key functionalities and benefits of an ORM

WKB2

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


