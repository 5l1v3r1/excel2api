import unittest

from starlette import applications
from starlette.testclient import TestClient

from app import app
# import setting
from setting import Setting

client = TestClient(app)


class TestGoogleServiceApi(unittest.TestCase):

    def setUp(self):
        _setting = Setting()
        applications.conf = dict()
        # get config
        applications.conf['config'] = _setting.load_config

    def test_positive(self):
        """Google api positive test"""
        _url = '/v1/api/google?spreadsheet_id={}&sheet_range={}'.format(
            '14klCxTe5iIa31bf2wQ-5qR0ctRXwW1jvuFLaIIOB4Po', 'example!A12:B22'
        )
        response = client.get(_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 200)

    def test_with_long_sheet_range(self):
        """Google api test long sheet range"""
        _url = '/v1/api/google?spreadsheet_id={}&sheet_range={}'.format(
            '14klCxTe5iIa31bf2wQ-5qR0ctRXwW1jvuFLaIIOB4Po', 'example!A120:B220'
        )
        response = client.get(_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 200)

    def test_only_first_alphabet_sheet_range(self):
        """Google api test only first alphabet sheet range"""
        _url = '/v1/api/google?spreadsheet_id={}&sheet_range={}'.format(
            '14klCxTe5iIa31bf2wQ-5qR0ctRXwW1jvuFLaIIOB4Po', 'example!A:B220'
        )
        response = client.get(_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 200)

    def test_only_last_alphabet_sheet_range(self):
        """Google api test only first alphabet sheet range"""
        _url = '/v1/api/google?spreadsheet_id={}&sheet_range={}'.format(
            '14klCxTe5iIa31bf2wQ-5qR0ctRXwW1jvuFLaIIOB4Po', 'example!A12:B'
        )
        response = client.get(_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 200)

    def test_only_alphabet_sheet_range(self):
        """Google api test only alphabet sheet range"""
        _url = '/v1/api/google?spreadsheet_id={}&sheet_range={}'.format(
            '14klCxTe5iIa31bf2wQ-5qR0ctRXwW1jvuFLaIIOB4Po', 'example!A:B'
        )
        response = client.get(_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 200)
