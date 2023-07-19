from __future__ import annotations

from sqlalchemy import (
    Column,
    Text,
    Integer,
    )

from database.db_models.base import Base


class Feedback(Base):
    __tablename__ = 'feedback'

    id = Column(Integer(), primary_key=True)
    name = Column(Text(), nullable=False)
    phone = Column(Text(), nullable=False)
    period = Column(Text())
    business = Column(Text())

    def __repr__(self):
        return f"<Client(fio='{self.name}, phone={self.phone}, id='{self.id}'"


