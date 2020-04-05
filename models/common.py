import sqlalchemy as sql
from sqlalchemy.orm import relationship
from core.orm import Base


class Currency(Base):
    __tablename__ = 'currency'

    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    abbr = sql.Column(sql.String(3), nullable=False, unique=True)
    code = sql.Column(sql.SmallInteger, unique=True)

    description = sql.Column(sql.String(128), nullable=True)

    # just to proof that we can set index type
    __table_args__ = (
        sql.Index('currency_abbr_idx', 'abbr', postgresql_using='hash'),
        sql.Index('currency_code_idx', 'code', postgresql_using='hash'),
    )


class Region(Base):
    __tablename__ = 'region'
    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    code = sql.Column(sql.String(3), index=True, unique=True)
    name = sql.Column(sql.String(200), nullable=True)
    currency_id = sql.Column(sql.ForeignKey('currency.id'), nullable=True)
    currency = relationship('Currency')


class Tag(Base):
    __tablename__ = 'tag'
    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    tag = sql.Column(sql.String(64), index=True, unique=True)

