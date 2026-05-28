from abc import ABC, abstractmethod
from mixins.timestamp_mixin import TimestampMixin


class Item(ABC, TimestampMixin):
    def __init__(self, item_id, title):
        TimestampMixin.__init__(self)

        self.__item_id = item_id
        self._title = title

    # Getter
    def get_item_id(self):
        return self.__item_id

    def get_title(self):
        return self._title

    # Setter
    def set_title(self, new_title):
        self._title = new_title
        self.update_timestamp()

    @abstractmethod
    def display_info(self):
        pass