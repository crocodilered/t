import json

from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404
from django.views import View

from app.snippets.tasks import examine_snippet
from app.snippets.models import Snippet


class FormView(View):
    template = 'snippets/form.html'

    def get(self, request):
        return render(request, self.template)


class SnippetSerializerMixin:
    @staticmethod
    def serialize(snippet):
        return {
            'pk': snippet.pk,
            'status': snippet.status,
            'code': snippet.code,
        }


class SnippetGeneralView(View, SnippetSerializerMixin):
    def get(self, *args, **kwargs):
        snippet_pk = kwargs.get('snippet_pk', 0)
        snippet = get_object_or_404(Snippet, pk=snippet_pk)
        return JsonResponse(self.serialize(snippet))

    def post(self, *args, **kwargs):
        params = json.loads(self.request.body)
        code = params.get('code')

        if code:
            snippet = Snippet(code=code)
            snippet.save()

            examine_snippet.delay(snippet.pk, snippet.code)

            return JsonResponse(self.serialize(snippet))

        else:
            return HttpResponseBadRequest()


class SnippetLatestView(View, SnippetSerializerMixin):
    def get(self, *args, **kwargs):
        snippet = Snippet.objects.order_by('-id')[0]
        return JsonResponse(self.serialize(snippet))
