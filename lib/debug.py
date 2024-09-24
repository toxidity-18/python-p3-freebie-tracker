from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Company, Dev, Freebie

# Set up the engine and session
engine = create_engine('sqlite:///freebie_tracker.db')
Session = sessionmaker(bind=engine)
session = Session()

# Test cases
company = session.query(Company).first()
dev = session.query(Dev).first()

# Create a new freebie
company.give_freebie(dev, "Cap", 5)

# Find the oldest company
print(Company.oldest_company())

# Dev receives freebie
print(dev.received_one("Cap"))

# Dev gives away freebie
dev.give_away(dev, session.query(Freebie).first())

# Print details of a freebie
freebie = session.query(Freebie).first()
print(freebie.print_details())
