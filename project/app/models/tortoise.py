from tortoise import models, fields
from tortoise.contrib.pydantic import pydantic_model_creator


class TextSummary(models.Model):
    url = fields.TextField()
    summary = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "textsummary"

    def __str__(self):
        return self.url


SummarySchema = pydantic_model_creator(TextSummary)
