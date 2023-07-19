from pydantic import BaseModel


class FeedBackModel(BaseModel):
    name: str = ""
    phone: str = ""
    period: str = ""
    business: str = ""

    def __str__(self):
        return f"Feedback: name: {self.name}, phone: {self.phone}, period: {self.period}, business: {self.business}"
