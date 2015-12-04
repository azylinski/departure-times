from sqlalchemy import Column, Integer, String, DateTime

from utils.sql import db


class Departure(db.Model):
    __tablename__ = 'departures'

    id = Column(Integer, primary_key=True, autoincrement=True)

    stop_tag = Column(String, index=True)
    departure_at = Column(DateTime, index=True)
    destination = Column(String)
    route = Column(String)

    def __init__(self, stop_tag, departure_at, destination, route):
        self.stop_tag = stop_tag
        self.departure_at = departure_at
        self.destination = destination
        self.route = route

    @property
    def serialize(self):
        """
        Return object data as a dict
        """
        return {
            'departure_at': self.departure_at.isoformat(),
            'destination': self.destination,
            'route': self.route
        }
