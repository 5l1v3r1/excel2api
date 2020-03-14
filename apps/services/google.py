import requests
from starlette import applications

from apps.abstracts import AbstractExcelToApi


class GoogleSheetService(AbstractExcelToApi):

    def __init__(self):
        self.__base_url = applications.conf['config']['google']['base_url']
        self.__api_key = applications.conf['config']['google']['credential_key']
        AbstractExcelToApi.__init__(self)

    def list_data(self, spreadsheet_id: str = None, spreadsheet_url: str = None, sheet_range: str = None) -> dict:
        """Query to get list data
        :param spreadsheet_url: str
        :param spreadsheet_id: str
        :param sheet_range: str
        :return: dict
        """
        _param = {'key': self.__api_key}
        _url = '{base_url}/{spreadsheet_id}/values/{sheet_range}'.format(
            base_url=self.__base_url, spreadsheet_id=spreadsheet_id, sheet_range=sheet_range
        )
        return requests.get(_url, params=_param).json()

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
