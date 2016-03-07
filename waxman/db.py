import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Wax(Base):
  __tablename__ = 'wax'

  id = sa.Column(sa.Integer, primary_key=True)
  albumName = sa.Column(sa.String)
  artistName = sa.Column(sa.String)

  def _repr_(self):
    return "<Album:%s - Artist:%s>" % (self.albumName, self.artistName)

class db:
  def __init__(self):
    # Connect to engine, here we use a temp Sqlite engine for development
    engine = sa.create_engine('sqlite:///:memory:', echo=True)
