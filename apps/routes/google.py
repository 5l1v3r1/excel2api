from http import HTTPStatus

from fastapi import APIRouter
from starlette.responses import JSONResponse

from apps.controllers import GoogleSheetController

router = APIRouter()


@router.get("/v1/api/google")
def fetch_all(spreadsheet_id: str, sheet_range: str):
    _data = GoogleSheetController()
    _result = _data.fetch_list(spreadsheet_id, sheet_range)
    return JSONResponse({'status': HTTPStatus.OK, 'data': _result}, status_code=HTTPStatus.OK)
