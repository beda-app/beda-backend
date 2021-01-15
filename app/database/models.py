from datetime import datetime

from tortoise import fields
from tortoise.models import Model


class User(Model):
    id: int = fields.IntField(pk=True)

    email: str = fields.CharField(255, unique=True)
    password: str = fields.CharField(60)


class Weight(Model):
    id: int = fields.IntField(pk=True)

    # TODO: ForeignKey
    related_user: int = fields.IntField()
    time: datetime = fields.DatetimeField()
    weight: float = fields.FloatField()
