from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, func,UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.orm import mapped_column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    type = Column(String)
    full_name = Column(String)
    username = Column(String,unique=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    submitted_by = Column(String)
    updated_at = Column(DateTime,default=func.now(), onupdate=func.now())


class AttendanceLog(Base):
    __tablename__ = "attendence_log"

    id = Column(Integer, primary_key=True)
    student_id = mapped_column(ForeignKey("students.id"))
    course_id = mapped_column(ForeignKey("courses.id"))
    present = Boolean()
    submitted_by = Column(String)
    updated_at = Column(DateTime,default=func.now(), onupdate=func.now())

class Courses(Base):

    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    course_name = Column(String)
    department_id = mapped_column(ForeignKey("departments.id"))
    semester = Column(Integer)
    class_ = Column('class', String)
    lecture_hours = Column(Integer)
    submitted_by = Column(String)
    updated_at = Column(DateTime,default=func.now(), onupdate=func.now())

class Departments(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True)
    department_name = Column(String,unique=True)
    submitted_by = Column(String)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


class Students(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    department_id  = Column(Integer)
    class_ = Column('class', String)
    submitted_by = Column(String)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    __table_args__ = (
        UniqueConstraint('full_name', 'class', name='uix_full_name_class'),
    )
