from enum import Enum

import sqlalchemy as sql
from sqlalchemy.orm import relationship

from core.mixins.enum import ChoiceMixin
from core.orm import Base


class AccountType(ChoiceMixin, Enum):
    default = 0


class Account(Base):
    __tablename__ = 'account'

    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    email = sql.Column(sql.String(255), index=True, nullable=False)
    phone = sql.Column(sql.String(15), index=True, nullable=False)
    agent_id = sql.Column(sql.ForeignKey('agent.id'), nullable=False)
    contract_number = sql.Column(sql.String(64), nullable=True)
    status = sql.Column(sql.Boolean, default=True, index=True)
    type = sql.Column(sql.Integer, default=AccountType.default.value)
    currency_id = sql.Column(sql.ForeignKey('currency.id'), nullable=True, index=True)
    region_id = sql.Column(sql.ForeignKey('region.id'), nullable=True, index=True)

    credit_limit = sql.Column(sql.Numeric(12, 3), nullable=True)
    trans_limit = sql.Column(sql.Numeric(12, 3), nullable=True)
    daily_limit = sql.Column(sql.Numeric(12, 3), nullable=True)

    tags = relationship(
        "Tag",
        secondary='account_tags',
        back_populates='accounts',
        order_by='account_tags.id'
    )

    __table_args__ = (
        sql.UniqueConstraint(agent_id, contract_number),
    )


class AccountTags(Base):
    __tablename__ = 'account_tags'

    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    account_id = sql.Column(sql.Integer, sql.ForeignKey(Account.id), nullable=True, index=True)
    tag_id = sql.Column(sql.Integer, sql.ForeignKey('tag.id'), nullable=True, index=True)

