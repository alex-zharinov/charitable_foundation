from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, String, Text
from sqlalchemy.orm import validates

from app.core.db import Base


class CharityProject(Base):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)
    full_amount = Column(Integer, nullable=False)
    fully_invested = Column(Boolean, default=False)
    invested_amount = Column(Integer, default=0)
    create_date = Column(DateTime, index=True, default=datetime.now)
    close_date = Column(DateTime)

    def __repr__(self):
        return (
            f'Благодтворительный проект {self.name} на сумму {self.full_amount}'
        )

    @validates('full_amount')
    def validate_full_amount(self, key, value):
        if value < 1:
            raise ValueError('Требуемуя сумма должна быть больше 0!')
        return value

    @validates('name')
    def validate_name(self, key, value):
        if len(value) < 1:
            raise ValueError('Название проекта не может быть пустым!')
        return value

    @validates('description')
    def validate_description(self, key, value):
        if len(value) < 1:
            raise ValueError('Описание проекта не может быть пустым!')
        return value
