from django.shortcuts import render
from .forms import OrderCreateForm


def main_page(request):
    return render(request, 'main_page.html')


def order_create(request):
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'order_created.html')
    form = OrderCreateForm()
    return render(request, 'order.html', {'form': form})
