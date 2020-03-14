from functools import lru_cache
from string import ascii_lowercase

import xlrd

from apps.services import RawUrlServiceApi


class RawUrlController(RawUrlServiceApi):

    def __init__(self):
        RawUrlServiceApi.__init__(self)

    @staticmethod
    def _get_sheet_idx_based_name(workbook: object = xlrd, sheet_name: str = None) -> list:
        """Search index sheet based on name
        :param workbook: object
        :return: list
        """
        return [idx for idx, val in enumerate(workbook.sheet_names()) if val == sheet_name]

    @lru_cache()
    def _get_index_from_alphabet(self, alphabet: str) -> list:
        """Get index based on alphabet
        :param alphabet: str
        :return: list
        """
        return [idx for idx, val in enumerate(ascii_lowercase) if alphabet.lower() == val]

    def _unpack_param(self, sheet_range: str) -> tuple:
        """Get param based on sheet range
        :param sheet_range: str
        :return: tuple
        """
        tmp = sheet_range.split('!')
        sheet_name = tmp[0]
        tmp2 = tmp[1].split(':')
        x_1 = x_2 = y_1 = y_2 = 0
        if len(tmp2[0]) == 1:
            x_1, x_2 = int(self._get_index_from_alphabet(tmp2[0])[0]), None
        if len(tmp2[0]) > 1:
            x_1, x_2 = int(self._get_index_from_alphabet(tmp2[0][0])[0]), int(tmp2[0][1:])
        if len(tmp2[1]) == 1:
            y_1, y_2 = int(self._get_index_from_alphabet(tmp2[1])[0]), None
        if len(tmp2[1]) > 1:
            y_1, y_2 = int(self._get_index_from_alphabet(tmp2[1][0])[0]), int(tmp2[1][1:])
        return sheet_name, x_1, x_2, y_1, y_2

    def fetch_list(self, spreadsheet_url: str = None, sheet_range: str = None) -> dict:
        """Query to get list data
        :param spreadsheet_url: str
        :param sheet_range: str
        :return: dict
        """
        _workbook = self.list_data(spreadsheet_url=spreadsheet_url, sheet_range=sheet_range)
        _sheet_name, x_1, x_2, y_1, y_2 = self._unpack_param(sheet_range)
        _sheet_idx = self._get_sheet_idx_based_name(_workbook, _sheet_name)
        # everything alright
        _sheet = _workbook.sheet_by_index(_sheet_idx[0])  # get first sheet
        _header = [_sheet.cell_value(0, i) for i in range(_sheet.ncols)]
        if x_2 is None and y_2 is not None:
            x_2 = y_2
        if y_2 is None and x_2 is not None:
            y_2 = x_2

        if x_2 is None or y_2 is None:
            return dict(
                range=sheet_range, data=[dict(zip(_header, _sheet.row_values(i))) for i in range(1, _sheet.nrows)]
            )

        return dict(
            range=sheet_range, data=[
                dict(zip(_header, [c.value for c in _sheet.row_slice(row, start_colx=x_1, end_colx=x_2 + 1)]))
                for row in range(y_1 - 1, y_2)
            ]
        )
