from datetime import datetime
from uuid import uuid4

import human_readable_ids
from peewee import (
    CharField,
    DateTimeField,
    Model,
    SqliteDatabase,
    UUIDField,
)

DB_PATH: str = "/home/cr/Desktop/ba-cr/scripts/results/smard.db"
db: SqliteDatabase = SqliteDatabase(DB_PATH)

class BaseModel(Model):
    """All model classes have to inherit from this base class."""

    class Meta:
        """Set Database"""

        database: SqliteDatabase = db

    id = UUIDField(primary_key=True, default=uuid4)
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)
    readable_id = CharField()

    def save(self, force_insert=True, only=None):
        """Save the data in the model instance
        See https://docs.peewee-orm.com/en/latest/peewee/api.html#Model.save

        :param force_insert: Force INSERT query, defaults to True
        :param only: Only save the given Field instances, defaults to None
        """
        # As `save` is called from `create`, `updated_at` will also be set  when calling `create`.
        if self.readable_id is None:
            readable_id = human_readable_ids.get_new_id().lower().replace(" ", "-")
            while self.select().where(self.readable_id == readable_id).exists():
                readable_id = human_readable_ids.get_new_id().lower().replace(" ", "-")
            self.readable_id = readable_id
        self.updated_at = datetime.now()
        super().save(force_insert, only)


class SerializableBaseModel(BaseModel):
    """All model classes have to inherit from this base class
    if they want to have additional serialization features."""

    def to_dict(self) -> dict[str, any]:
        """serializes the model object to a dictionary.

        :return: the dictionary
        """
        return {
            "id": str(self.id),
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at),
            "readable_id": self.readable_id,
        }
