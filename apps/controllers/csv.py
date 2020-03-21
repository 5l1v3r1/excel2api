import json

from apps.services import ExcelServiceApi


class CsvController(ExcelServiceApi):

    def __init__(self):
        ExcelServiceApi.__init__(self)

    def fetch(self, sheet_url: str, row_range: str, column_range: str) -> dict:
        """Convert all data from pandas to dictionary
        :param sheet_url: str
        :param row_range: str
        :param column_range: str
        :return: dict
        """
        df = self.fetch_csv(sheet_url)
        if row_range is not None:
            df = df[row_range]
        if column_range is not None:
            df = df[column_range]

        return json.loads(df.to_json(orient='records'))
