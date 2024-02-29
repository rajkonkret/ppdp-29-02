# podejscie za pomocą ORM
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


# echo=True logowanie co się dzieje w bazie danych
engine = create_engine('sqlite:///mydatabse.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_user = User(name="John Doe", age=20)
session.add(new_user)  # INSERT INTO users (name, age) VALUES (?, ?)
session.commit()
session.close()

useers = session.query(User).all()  # SELECT * FROM users
for user in useers:
    print(user.name, user.age)
# John Doe 20
# John Doe 20
# John Doe 20
