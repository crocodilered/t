import requests
import time
from app.snippets.models import Snippet


class ExaminatorApi:
    API_URL = 'http://127.0.0.1:8000/examinator/'
    SECONDS_BETWEEN_RETIES = 0.5

    def __init__(self):
        self.sess = requests.session()

    def run(self, **kwargs):
        resp = None

        if kwargs.get('snippet_code'):
            resp = self.sess.post(self.API_URL, json={'snippet_code': kwargs.get('snippet_code')})

        elif kwargs.get('task_id'):
            task_id = kwargs['task_id']
            resp = self.sess.get(f'{self.API_URL}{task_id}/')

        if resp and resp.status_code == 200:
            status = resp.json().get('exec_status')

            if status == 'correct':
                return Snippet.STATUS_SUCCESS

            if status == 'wrong':
                return Snippet.STATUS_FAILURE

            if status == 'evaluation':
                time.sleep(self.SECONDS_BETWEEN_RETIES)
                task_id = resp.json().get('exec_id')
                return self.run(task_id=task_id)

        return Snippet.STATUS_ERROR
