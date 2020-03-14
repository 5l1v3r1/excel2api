import concurrent.futures

from apps.services import GoogleSheetServiceApi


class GoogleSheetController(GoogleSheetServiceApi):

    def __init__(self):
        GoogleSheetServiceApi.__init__(self)

    def _get_header(self, spreadsheet_id: str = None, sheet_range: str = None) -> dict:
        """Fix sheet range to always get
        :return: dict
        """
        tmp = sheet_range.split('!')
        tmp2 = tmp[1].split(':')
        x = tmp2[0][0] if len(tmp2[0]) > 1 else tmp2[0]
        y = tmp2[1][0] if len(tmp2[1]) > 1 else tmp2[0]
        sheet_range = '{sheet_name}!{x}1:{y}1'.format(sheet_name=tmp[0], x=x, y=y)
        return self.list_data(spreadsheet_id=spreadsheet_id, sheet_range=sheet_range)

    def fetch_list(self, spreadsheet_id: str = None, sheet_range: str = None) -> dict:
        """Fetch data from resource
        :param spreadsheet_id: str
        :param sheet_range: str
        :return: dict
        """
        _data = self.list_data(spreadsheet_id=spreadsheet_id, sheet_range=sheet_range)
        _header = self._get_header(spreadsheet_id=spreadsheet_id, sheet_range=sheet_range)
        # if any error from api
        if _data.get('error', None) is not None:
            return _data

        # everything alright
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            _result = _data.get('values')
            _header = _header.get('values').pop(0)
            return dict(
                range=_data.get('range'),
                data=list(executor.map(lambda x: dict(zip(_header, x)), _result))
            )
