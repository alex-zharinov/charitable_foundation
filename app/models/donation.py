from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Text
from sqlalchemy.orm import validates

from app.core.db import Base


class Donation(Base):
    comment = Column(Text)
    full_amount = Column(Integer, nullable=False)
    fully_invested = Column(Boolean, default=False)
    invested_amount = Column(Integer, default=0)
    create_date = Column(DateTime, index=True, default=datetime.now)
    close_date = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'))

    def __repr__(self):
        return (
            f'Пожертвование на сумму {self.full_amount}'
        )

    @validates('full_amount')
    def validate_full_amount(self, key, value):
        if value < 1:
            raise ValueError('Требуемая сумма должна быть больше 0!')
        return value
