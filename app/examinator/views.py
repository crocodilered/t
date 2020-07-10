import json

from django.http import JsonResponse
from django.views import View

from .libs import get_submission, post_submission


class MainView(View):
    def __init__(self, **kwargs):
        self.exec_id = None
        self.exec_status = None
        super().__init__(**kwargs)

    def _make_exec_response(self):
        return JsonResponse({
            'exec_id': self.exec_id,
            'exec_status': self.exec_status,
        })

    def get(self, *args, **kwargs):
        exec_id = kwargs.get('exec_id')
        self.exec_id, self.exec_status = get_submission(exec_id)
        return self._make_exec_response()

    def post(self, *args, **kwargs):
        params = json.loads(self.request.body)
        snippet_code = params.get('snippet_code')
        self.exec_id, self.exec_status = post_submission(snippet_code)
        return self._make_exec_response()
