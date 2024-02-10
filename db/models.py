from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Route(Base):
    __tablename__ = "routes"
    id = Column(Integer, primary_key=True, index=True)
    points = relationship("Point", backref="route")


class Point(Base):
    __tablename__ = "points"
    id = Column(Integer, primary_key=True, index=True)
    lat = Column(Float)
    lng = Column(Float)
    route_id = Column(Integer, ForeignKey('routes.id'))
