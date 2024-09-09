
from database import engine
from models import Base

Base.metadata.create_all(engine)
print("All tables have been created successfully.")