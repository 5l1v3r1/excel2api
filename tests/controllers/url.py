import unittest

from starlette import applications
from starlette.testclient import TestClient

from app import app
# import setting
from setting import Setting

client = TestClient(app)


class TestUrlServiceApi(unittest.TestCase):

    def setUp(self):
        _setting = Setting()
        applications.conf = dict()
        # get config
        applications.conf['config'] = _setting.load_config

    def test_positive(self):
        """Url api positive test"""
        _url = '/v1/api/url?spreadsheet_url={}&sheet_range={}'.format(
            'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/data.xlsx', 'Sheet1!A12:C22'
        )
        response = client.get(_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 200)

    def test_with_long_sheet_range(self):
        """Url api test long sheet range
            TODO: doing validation when record < than sheet range
        """
        with self.assertRaises(Exception):
            _url = '/v1/api/url?spreadsheet_url={}&sheet_range={}'.format(
                'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/data.xlsx', 'Sheet1!A120:C220'
            )
            client.get(_url)

    def test_only_first_alphabet_sheet_range(self):
        """Url api test only first alphabet sheet range
            TODO: doing validation when record < than sheet range
        """
        with self.assertRaises(Exception):
            _url = '/v1/api/url?spreadsheet_url={}&sheet_range={}'.format(
                'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/data.xlsx', 'Sheet1!A:C220'
            )
            client.get(_url)

    def test_only_last_alphabet_sheet_range(self):
        """Url api test only first alphabet sheet range"""
        _url = '/v1/api/url?spreadsheet_url={}&sheet_range={}'.format(
            'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/data.xlsx', 'Sheet1!A12:C'
        )
        response = client.get(_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 200)

    def test_only_alphabet_sheet_range(self):
        """Url api test only alphabet sheet range"""
        _url = '/v1/api/url?spreadsheet_url={}&sheet_range={}'.format(
            'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/data.xlsx', 'Sheet1!A:C'
        )
        response = client.get(_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 200)
