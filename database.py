from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

# SQLite connection string for easy local development
SQLALCHEMY_DATABASE_URL = "sqlite:///./admin_tracker.db"

# Create SQLAlchemy engine with SQLite-specific parameters
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create base class for models
Base = declarative_base()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
