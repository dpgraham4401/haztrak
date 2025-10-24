from http import HTTPStatus

from django.http import Http404

from trak.apps.core.utils import exception_handler


class TestTrakExceptionHandler:
    def test_http404_to_not_found(self):
        http404_exec = Http404()
        context = {}
        response = exception_handler(http404_exec, context)
        assert response.status_code == HTTPStatus.NOT_FOUND
        assert "Not found" in response.data["detail"]
