import sqlite3

conn = sqlite3.connect('petdatabase.db')
print "Opened database successfully";

conn.execute('CREATE TABLE dogs (dog_breed TEXT, dog_color TEXT, dog_sex TEXT, dog_age TEXT, dogt_behavior TEXT, dog_category TEXT)')
print "Table created successfully";
conn.close()



# DanielLove's code
# import pandas as pd
# from sqlalchemy import create_engine
# from sqlalchemy import Table, Column, Integer, String, Float
# from sqlalchemy.orm import Session
# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()
# ​
# # Create the Listings class.
# class Listing(Base):
#     __tablename__ = "listings"
#     id = Column(Integer, primary_key=True)
#     breed = Column(String(255))
#     color = Column(String(255))
#     pet_sex = Column(String(5))
#     pet_age = Column(String(35))
#     pet_behavior = Column(String(255))
#     pet_type = Column(String(255))

# ​
# # Create the database connection.
# database_path = "Resources/pet_db.sqlite"
# engine = create_engine(f"sqlite:///{database_path}")
# conn = engine.connect()
# session = Session(bind=engine)
# ​
# # Clear out current data in the database.
# Base.metadata.drop_all(engine)
# ​
# # Create a metadata layer that abstracts the database.
# Base.metadata.create_all(engine)
# ​
# # Store the scraped data as a data frame.
# scraped_data = pd.read_csv("Resources/petDataUpdated.csv")
# ​
# # Insert data into the database.
# for _, row in scraped_data.iterrows():
#     listing = Listing(
#       breed = row["breed"],
#       color = row["color"],
#       pet_sex = row["pet_sex"],
#       pet_age = row["pet_age"],
#       pet_behavior = row["pet_behavior"],
#       pet_type = row["pet_type"]
#       )
#     session.add(listing)
# ​
# # Commit all listings
# session.commit()
# ​
# # Close the session.
# session.close()
# ​
# # Close the connection.
# conn.close()