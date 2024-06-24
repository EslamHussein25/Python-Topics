from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# إنشاء قاعدة البيانات (استبدل القيم بناءً على إعداداتك)
DATABASE_URL = "postgresql+psycopg2://eslamsql:1234@localhost:5432/dbeslam"

# إنشاء محرك القاعدة
engine = create_engine(DATABASE_URL)

# قاعدة البيانات الأساسية
Base = declarative_base()

# تعريف النموذج (Model) للجدول
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

# إنشاء جميع الجداول في قاعدة البيانات (إن لم تكن موجودة)
Base.metadata.create_all(engine)

# إنشاء جلسة
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


#**************************************** app ****************************************


# insert 
new_user = User(name="John Doe", age=30)
try:

    session = Session()
    session.add(new_user)
    session.commit()
    session.close()
    print("Added!")
except SQLAlchemyError as e:
    print(f"Can't add new user for this error: {e}")



# Read 
def GetAll():
    try:
        session = Session()
        users = session.query(User).all()
        session.close()
        print("Readed!")
        for user in users:
                print(f"ID: {user.id}, Name: {user.name}, Age: {user.age}")
    except SQLAlchemyError as e:
        print(f"Can't Read  user for this error: {e}")
    return users

u = GetAll()
for user in u:
    print(f"ID: {user.id}, Name: {user.name}, Age: {user.age}")
print("Done")

# Update 
try:
    session = Session()
    user = session.query(User).filter(User.id == 1).first()
    if user:
            user.name = "Ahmed"
            user.age = 28
            session.commit()
            session.close()
            print("Updated")
    else:
        print(" this user not found!")
except SQLAlchemyError as e:
    print(f"Can't update user for this error: {e}")


#Delete
try:
        session = Session()
        user = session.query(User).filter(User.id == 1).first()
        if user:
                session.delete(user)
                session.commit()
                print("Deleted!")
        else:
                print("Book Not Found!")
        session.close()
except SQLAlchemyError as e:
        print(f"Can't update book for this error: {e}")
        flag = False 

session.close()