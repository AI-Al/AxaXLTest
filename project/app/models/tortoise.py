from tortoise import models
from tortoise import fields

class TextSummary(models.Model):
    url = fields.TextField()
    summary = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "textsummary"

    def __str__(self):
        return self.url