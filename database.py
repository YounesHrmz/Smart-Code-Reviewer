from sqlalchemy import create_engine, Column, String, Text, Integer, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import UUID
import uuid, datetime

Base = declarative_base()

# غيّر 1234 بباسورد PostgreSQL عندك
engine = create_engine("postgresql://postgres:1234@localhost/code_reviewer_db")

class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class Submission(Base):
    __tablename__ = "submissions"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    code_content = Column(Text)
    language = Column(String)
    status = Column(String, default="pending")
    submitted_at = Column(DateTime, default=datetime.datetime.utcnow)

class ReviewReport(Base):
    __tablename__ = "review_reports"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    quality_score = Column(Integer)
    security_score = Column(Integer)
    summary = Column(Text)

Base.metadata.create_all(engine)
print("✅ الجداول تم إنشاؤها بنجاح")