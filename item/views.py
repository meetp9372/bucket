from django.shortcuts import render
from django.views import View
from item.models import Item
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class ItemView(View):
    template_name = 'home.html'

    @method_decorator(login_required)
    def get(self, request):
        return render(request, self.template_name)

    @method_decorator(login_required)
    def post(self, request):

        total_cost = 0
        for item_number in range(1, int(request.POST["item_length"])+1):
            item_name = request.POST[f"item_{item_number}"]
            item_price = request.POST[f"price_{item_number}"]
            if item_name and item_price:
                Item.objects.create(name=item_name, price=item_price)
                total_cost += float(request.POST[f"price_{item_number}"])

        return render(request, 'summary_page.html', context={'items_total_cost': round(total_cost, 3)})


