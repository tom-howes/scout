from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ARRAY, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
import os

Base = declarative_base()

class Artist(Base):
    __tablename__ = 'artists'

    id = Column(Integer, primary_key=True)
    spotify_id = Column(String, unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    genres = Column(ARRAY(String), default=[])
    popularity = Column(Integer)
    followers = Column(Integer)
    monthly_listeners = Column(Integer)
    image_url = Column(String)
    spotify_url = Column(String)
    quality_score = Column(Float)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    def __repr__(self):
        return f"<Artist(name='{self.name}', followers={self.followers})>"

class Discovery(Base):
    __tablename__ = 'discoveries'

    id = Column(Integer, primary_key=True)
    user_id = Column(String(255))
    artist_id = Column(Integer, ForeignKey('artists.id'))
    discovered_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    followers_at_discovery = Column(Integer)

    artist = relationship("Artist")
