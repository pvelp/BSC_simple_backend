from database.db_connection import get_session
from database.db_models.db_models import Feedback
from core.models.models import FeedBackModel

from typing import List
from loguru import logger


def add_new_feedback(feedback: FeedBackModel):
    with get_session() as session:
        try:
            feedback = Feedback(**(feedback.dict()))
            session.add(feedback)
            session.commit()

        except Exception as ex:
            logger.critical(ex)


def get_all_feedbacks() -> List[Feedback]:
    with get_session() as session:
        feedbacks = session.query(Feedback).all()
        return feedbacks

