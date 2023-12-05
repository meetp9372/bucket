from django.shortcuts import render
from django.views import View


class ItemView(View):
    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):

        total_cost = 0
        for item_number in range(1, int(request.POST["item_length"])+1):
            total_cost += float(request.POST[f"price_{item_number}"])

        return render(request, 'summary_page.html', context={'items_total_cost': round(total_cost, 3)})


