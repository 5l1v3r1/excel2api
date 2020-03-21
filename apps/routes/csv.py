from http import HTTPStatus

from fastapi import APIRouter
from starlette.responses import JSONResponse

from apps.controllers import CsvController

router = APIRouter()


@router.get("/v1/api/csv")
def fetch_all(sheet_url: str, row_range: str = None, column_range: str = None):
    _data = CsvController()
    _result = _data.fetch(sheet_url, row_range, column_range)
    return JSONResponse({'status': HTTPStatus.OK, 'data': _result}, status_code=HTTPStatus.OK)
