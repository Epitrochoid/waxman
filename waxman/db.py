import sqlalchemy

class db:
  def __init__(self):
    # Connect to engine, here we use a temp Sqlite engine for development
    engine = create_engine('sqlite:///:memory:', echo=True)
