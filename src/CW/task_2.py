from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists

e = create_engine("sqlite:///test.db", echo=True)

e.execute(
    """
    CREATE TABLE groups (
    name VARCHAR(255)
    );
    """
)
