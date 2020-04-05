import sqlalchemy as sql
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from uuid import uuid4

from core.orm import Base

from .common import Region, Currency


class ApiUser(Base):
    __tablename__ = 'api_user'

    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    name = sql.Column(sql.String(64), index=True)
    uuid = sql.Column(UUID(as_uuid=True), default=uuid4(), index=True)

    region_id = sql.Column(sql.ForeignKey('region.id'), nullable=True)
    region: Region = relationship('Region')

    currency_id = sql.Column(sql.ForeignKey('currency.id'), nullable=True)
    currency_: Currency = relationship('Currency')

    @property
    def currency(self) -> Currency:
        return self.currency_ or self.region.currency if self.region else None
