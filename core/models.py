import sqlalchemy
from sqlalchemy import DateTime

from core.database_settings import metadata

maxway = sqlalchemy.Table(
    "maxway",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("full_name", sqlalchemy.String),
    sqlalchemy.Column("location", sqlalchemy.String),
    sqlalchemy.Column("chat_id", sqlalchemy.BigInteger),
    sqlalchemy.Column("phone_number", sqlalchemy.String),
    sqlalchemy.Column('created_at', DateTime(timezone=True), nullable=True),
    sqlalchemy.Column('updated_at', DateTime(timezone=True), nullable=True)
)
