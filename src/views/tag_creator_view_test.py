from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError
from .tag_creator_view import TagCreatorView

class MockCreator:
    def __init__(self, status_code, body: dict) -> None:
        self.status_code = status_code
        self.body = body


def test_creator_view():
    resp = MockCreator(
        status_code={float},
          body = {"str"}
        )

def test_creator_with_error():
    resp = MockCreator(
        status_code={int}, 
        body = {"dict"}
        )

    try:
        test_creator_view()
        assert False
    except Exception as exception:
        assert isinstance(exception,HttpUnprocessableEntityError)