from django.shortcuts import render
from django.views import View
from .tasks import parse_otomoto_prices

class OtomotoParserView(View):
    def get(self, request):
        return render(request, 'otomoto_parser.html', {'task_id': None, 'prices_and_titles': None})

    def post(self, request):
        task_id = request.POST.get('task_id')
        if task_id is None:
            url = 'https://www.otomoto.pl/motocykle-i-quady/indian/scout'
            task = parse_otomoto_prices.delay(url)
            task_id = task.id

        task_result = parse_otomoto_prices.AsyncResult(task_id)
        if task_result.ready():
            prices_and_titles = task_result.get()
            return render(request, 'otomoto_parser.html', {'prices_and_titles': prices_and_titles, 'task_id': None})
        else:
            return render(request, 'otomoto_parser.html', {'task_id': task_id, 'prices_and_titles': None})





