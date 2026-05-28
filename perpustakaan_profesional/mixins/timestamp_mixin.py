from datetime import datetime


class TimestampMixin:
    def __init__(self):
        self._updated_at = datetime.now()

    def update_timestamp(self):
        self._updated_at = datetime.now()

    def get_timestamp(self):
        return self._updated_at