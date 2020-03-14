from http import HTTPStatus

from fastapi import APIRouter
from starlette.responses import JSONResponse

from apps.controllers import RawUrlController

router = APIRouter()


@router.get("/v1/api/url")
def fetch_all(spreadsheet_url: str, sheet_range: str):
    _data = RawUrlController()
    _result = _data.fetch_list(spreadsheet_url, sheet_range)
    return JSONResponse({'status': HTTPStatus.OK, 'data': _result}, status_code=HTTPStatus.OK)
