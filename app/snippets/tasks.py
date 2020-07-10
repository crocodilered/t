from app.celery_app import celery_app
from app.snippets.libs import ExaminatorApi
from app.snippets.models import Snippet


@celery_app.task(ignore_results=True)
def examine_snippet(snippet_pk, snippet_code):
    er = ExaminatorApi()
    status = er.run(snippet_code=snippet_code)

    snippet = Snippet.objects.get(pk=snippet_pk)
    snippet.status = status
    snippet.save()
