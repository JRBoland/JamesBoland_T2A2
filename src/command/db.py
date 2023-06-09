from main import db, bcrypt
from flask import Blueprint
from models.drone import Drone
from models.flight_log import FlightLog
from models.pilot import Pilot
from models.user import User

# Set the blueprint
db_cmd = Blueprint("db", __name__)

# Create tables
@db_cmd.cli.command('create')
def create_db():
    db.create_all()
    print('Tables Created')

# Drop tables
@db_cmd.cli.command('drop')
def drop_db():
    db.drop_all()
    print('Tables Dropped')

# Function for seed command, to be used with reset command below

def seed_db():

    user1 = User(
        username = "Test user",
        password = bcrypt.generate_password_hash("password123").decode("utf-8"),
        email = "user@gmail.com",
        is_admin = False
    )
    db.session.add(user1)


    user2 = User(
        username = "Test admin user",
        password = bcrypt.generate_password_hash("password123").decode("utf-8"),
        email = "admin@gmail.com",
        is_admin = True
    )
    db.session.add(user2)

    user_null = User(
        id = 0,
        username = "NULL USER - USER PREVIOUSLY DELETED",
        password = bcrypt.generate_password_hash("NO-ONE-SHOULD-EVER-LOG-INTO-THIS").decode("utf-8"),
        email = "user_null@gmail.com",
        is_admin = True
    )
    db.session.add(user_null)


    db.session.commit()
    
    #for drones consider having a specialisation attribute
    drone1 = Drone(
        build_specifications = "Lightweight carbon fiber frame, high-speed brushless motors, FPV camera and transmitter, Carbon Fiber propellers, 45 LiPO battery, DRFPV software",
        weight_gms = 160,
        developed_by = "Drone Corp",
        year_of_manufacture = 2019,
        last_service = "2022 12 3",
        created_by_user_id = 2
    )
    db.session.add(drone1)
    
    drone2 = Drone(
        build_specifications = "Foldable and waterproof carbon fiber frame, 4k HD SEICA lens, Carbon Fiber propellers, 45 LiPO battery, stock software",
        weight_gms = 980,
        developed_by = "Drone Flyers Inc",
        year_of_manufacture = 2021,
        last_service = "2021 7 4",
        created_by_user_id = 2
    )
    db.session.add(drone2)

    drone3 = Drone(
        build_specifications = "Modular, Carbon Fiber propellers, 60 LiPO battery, 1080p camera, DR software",
        weight_gms = 880,
        developed_by = "Drone Flyers Inc",
        year_of_manufacture = 2022,
        last_service = "2022 9 3",
        created_by_user_id = 2
    )
    db.session.add(drone3)

    drone_null = Drone(
        id = 0000,
        build_specifications = "Null - DEFAULT DRONE LINK FOR WHEN A DRONE HAS BEEN DELETED",
        developed_by = "NULL",
        year_of_manufacture = 0000,
        created_by_user_id = 2
    )
    db.session.add(drone_null)

    db.session.commit()
  
    pilot1 = Pilot(
        name = "John Example",
        license = "Drone Pilots NSW",
        specialization = "Real estate site inspections",
        created_by_user_id = 2
    )
    db.session.add(pilot1)

    pilot2 = Pilot(
        name = "Vera Craig",
        license = "Drone Pilots NSW",
        specialization = "Nature photography",
        created_by_user_id = 2
    )
    db.session.add(pilot2)

    pilot3 = Pilot(
        name = "Johnathan Kihan",
        license = "Degenerate Drones VIC",
        specialization = "Weather and site monitoring (engineering)",
        created_by_user_id = 2
    )
    db.session.add(pilot3)

    pilot4 = Pilot(
        name = "James Daniels",
        license = "Drone Pilots NSW, RR",
        specialization = "FPV Racing",
        created_by_user_id = 2
    )
    db.session.add(pilot4)

    pilot_null = Pilot(
        id = 0000,
        name = "NULL PILOT - PILOT PREVIOUSLY DELETED",
        created_by_user_id = 2
    )
    db.session.add(pilot_null)

    db.session.commit()

    flight_log1 = FlightLog(
        flight_date = "2023 1 17",
        flight_time = "14:22", 
        flight_location = "Maddens Plains, NSW",
        flight_minutes = 26,
        flight_performance_rating_of_10 = 8,
        footage_recorded = True,
        drone_id = 3,
        pilot_id = 1,
        posted_by_user = 1
    )
    db.session.add(flight_log1)

    flight_log2 = FlightLog(
        flight_date = "2023 1 29",
        flight_time = "18:30", 
        flight_location = "Hyde Park, Sydney, NSW 2000",
        flight_minutes = 12,
        flight_performance_rating_of_10 = 9,
        footage_recorded = True,
        drone_id = 1,
        pilot_id = 4,
        posted_by_user = 1
    )
    db.session.add(flight_log2)

    flight_log3 = FlightLog(
        flight_date = "2023 2 07",
        flight_time = "14:30", 
        flight_location = "Killalea State Park, NSW",
        flight_minutes = 50,
        flight_performance_rating_of_10 = 7,
        footage_recorded = True,
        drone_id = 2,
        pilot_id = 2,
        posted_by_user = 2
    )
    db.session.add(flight_log3)

    flight_log4 = FlightLog(
        flight_date = "2023 2 22",
        flight_time = "10:15", 
        flight_location = "Hayman Island, Whitsundays, NSW",
        flight_minutes = 55,
        flight_performance_rating_of_10 = 8,
        footage_recorded = True,
        drone_id = 3,
        pilot_id = 2,
        posted_by_user = 1
    )
    db.session.add(flight_log4)

    flight_log5 = FlightLog(
        flight_date = "2023 2 26",
        flight_time = "11:45", 
        flight_location = "Kembla Grange Racetrack, Illawarra region NSW",
        flight_minutes = 15,
        flight_performance_rating_of_10 = 8,
        footage_recorded = True,
        drone_id = 1,
        pilot_id = 4,
        posted_by_user = 1
    )
    db.session.add(flight_log5)

    flight_log6 = FlightLog(
        flight_date = "2023 2 26",
        flight_time = "09:10", 
        flight_location = "Tamworth, NSW",
        flight_minutes = 50,
        flight_performance_rating_of_10 = 8,
        footage_recorded = True,
        drone_id = 2,
        pilot_id = 3,
        posted_by_user = 2
    )
    db.session.add(flight_log6)

    db.session.commit()

    print("Tables Seeded")


# Reset db CLI command with seed

@db_cmd.cli.command('reset')
def reset_db():
    db.drop_all()
    print('tables dropped')
    db.create_all()
    print('tables created')
    seed_db()
    