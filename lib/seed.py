from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Company, Dev, Freebie

# Set up the engine and session
engine = create_engine('sqlite:///freebie_tracker.db')
Session = sessionmaker(bind=engine)
session = Session()

# Drop and recreate all tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Seed data
company1 = Company(name="Tech Corp", founding_year=2001)
company2 = Company(name="Web Solutions", founding_year=2005)
dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")

freebie1 = Freebie(item_name="T-shirt", value=15, company=company1, dev=dev1)
freebie2 = Freebie(item_name="Mug", value=10, company=company2, dev=dev2)
freebie3 = Freebie(item_name="Sticker", value=2, company=company1, dev=dev2)

session.add_all([company1, company2, dev1, dev2, freebie1, freebie2, freebie3])
session.commit()

print("Database seeded!")

