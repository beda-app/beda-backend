from tortoise import fields
from tortoise.models import Model


class User(Model):
    id: int = fields.IntField(pk=True)

    email: str = fields.CharField(255)
    password: bytes = fields.BinaryField()
