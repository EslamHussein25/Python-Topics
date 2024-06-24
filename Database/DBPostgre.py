from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.orm import sessionmaker

# Database connection details
DATABASE_URL = 'postgresql://eslamsql:1234@127.0.0.1:5432/dbeslam'

# Create an engine
engine = create_engine(DATABASE_URL)

# Create a metadata object
metadata = MetaData()

# Define the books table
books_table = Table(
    'books', metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String),
    Column('author', String),
    Column('published_year', Integer)
)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Insert a single row into the books table
insert_statement = books_table.insert().values(title="Sample Book", author="John Doe", published_year=2023)
connection = engine.connect()
connection.execute(insert_statement)
connection.close()
'''
# Verify the insertion (Optional)
result = session.query(books_table).all()
for row in result:
    print(row)'''