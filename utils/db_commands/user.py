import logging

from core.database_settings import database
from core.models import maxway
from datetime import datetime

async def add_user(data: dict) -> int | None:
    try:
        query = maxway.insert().values(
            full_name=data.get("full_name"),
            phone_number=data.get("phone_number"),
            chat_id=int(data.get("chat_id")),
            location=data.get("location"),
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        new_user_id = await database.execute(query=query)
        return new_user_id
    except Exception as e:
        print(f"Error appeared when adding user: {e}")
        return None

async def get_user(chat_id: int):
    try:
        query = maxway.select().where(
            maxway.c.chat_id == chat_id
        )
        user = await database.fetch_one(query=query)
        return user
    except Exception as e:
        error_text = f"Error appeared when getting user: {e}"
        logging.error(error_text)
        return None