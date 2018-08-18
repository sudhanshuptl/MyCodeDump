import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationships
from sqlalchemy import create_engine

Base = declarative_base()  # this will let python know aur classes is special alchamy classes
# create Model Here


class Restaurant(Base):
    __tablename__ ='restaurant'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class MenuItems(Base):
    __tablename__ ='menu_items'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationships(Restaurant)



# insert engine at end of this File ##
engine = create_engine('mysql://root@localhost/food')
engine.execute('USE food;')

Base.metadata.create_all(engine)
