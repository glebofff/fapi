import sqlalchemy as sql
from core.orm import Base


class Agent(Base):
    __tablename__ = 'agent'

    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    abbr = sql.Column(sql.String(12), nullable=False, index=True, unique=True)
    name = sql.Column(sql.String(64), nullable=False)


