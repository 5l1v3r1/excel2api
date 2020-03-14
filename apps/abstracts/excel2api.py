from abc import ABC, abstractmethod


class ExcelToApi(ABC):

    @abstractmethod
    def list_data(self, spreadsheet_id: str = None, spreadsheet_url: str = None, sheet_range: str = None) -> dict:
        """Query to get list data
        :param spreadsheet_url: str
        :param spreadsheet_id: str
        :param sheet_range: str
        :return: dict
        """
        pass

    @abstractmethod
    def create_data(self, val: tuple) -> str:
        """Create new resource
        :param val: tuple
        :return: str
        """
        pass

    @abstractmethod
    def create_bulk_data(self, val: list) -> str:
        """Create new resource
        :param val: list
        :return: str
        """
        pass

    @abstractmethod
    def get_data(self, val: tuple) -> dict:
        """Get detail data
        :param val: tuple
        :return: dict
        """
        pass

    @abstractmethod
    def update_data(self, id: str, val: tuple) -> dict:
        """Update resource based on id
        :param id: str
        :param val: tuple
        :return: dict
        """
        pass

    @abstractmethod
    def delete_data(self, id: str, val: tuple) -> str:
        """Archive record based on id
        :param id: str
        :param val: tuple
        :return: str
        """
        pass
