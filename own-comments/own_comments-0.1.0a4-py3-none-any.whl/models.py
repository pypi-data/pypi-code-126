from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship

from .database import Base


class Thread(Base):
    __tablename__ = "threads"

    id = Column(Integer, primary_key=True, index=True)
    path = Column(String, index=True)
    date_created = Column(DateTime)
    auto_approve = Column(Boolean)
    locked = Column(Boolean)

    comments = relationship("Comment", back_populates="thread")

    def make_public(self):
        for c in self.comments:
            c.make_public()


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)

    author_name = Column(String, index=True)
    text = Column(String, index=True)

    approved = Column(Boolean)
    deleted = Column(Boolean)

    date_created = Column(DateTime)
    date_updated = Column(DateTime)
    update_key = Column(String)

    thread_id = Column(Integer, ForeignKey("threads.id"))
    thread = relationship("Thread", back_populates="comments")

    def make_public(self):
        self.update_key = None
