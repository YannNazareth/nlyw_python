from src.views.http_types.http_response import HttpResponse
from.error_types.http_unprocessable_entity import HttpUnprocessableEntityError

def handle_erros(error: Exception) -> HttpResponse:
    if isinstance(error, HttpUnprocessableEntityError):
        return HttpResponse(
            status_code=error.status_code,
            body = {
                "errors": [{
                    "tittle": error.name,
                    "detail": error.message
                }]
            }
        )

    return HttpResponse(
        status_code = 500,
        body={
            "errors": [{
                "tittle": "Server Error",
                "detail": str(error)
            }]
        }
    )