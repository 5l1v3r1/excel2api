import requests
import xlrd

from apps.abstracts import AbstractExcelToApi


class RawUrlService(AbstractExcelToApi):

    def __init__(self):
        AbstractExcelToApi.__init__(self)

    def list_data(self, spreadsheet_id: int = None, spreadsheet_url: str = None, sheet_range: str = None) -> dict:
        """Query to get list data
        :param spreadsheet_url: str
        :param spreadsheet_id: int
        :param sheet_range: str
        :return: dict
        """
        return xlrd.open_workbook(file_contents=requests.get(spreadsheet_url).content)

    def create_data(self, val: tuple) -> str:
        """Create new resource
        :param val: tuple
        :return: str
        """
        pass

    def create_bulk_data(self, val: list) -> str:
        """Create new resource
        :param val: list
        :return: str
        """
        pass

    def get_data(self, val: tuple) -> dict:
        """Get detail data
        :param val: tuple
        :return: dict
        """
        pass

    def update_data(self, id: str, val: tuple) -> dict:
        """Update resource based on id
        :param id: str
        :param val: tuple
        :return: dict
        """
        pass

    def delete_data(self, id: str, val: tuple) -> str:
        """Delete resource based on id
        :param id: str
        :param val: tuple
        :return: str
        """
        pass
