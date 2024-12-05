from django.shortcuts import render
from .models import Supplier

def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, "supplier_list.html", {"suppliers": suppliers})

from .models import Material

def material_list(request):
    materials = Material.objects.all()
    return render(request, "material_list.html", {"materials": materials})

from .models import Supply

def supply_list(request):
    supplies = Supply.objects.all()
    return render(request, "supply_list.html", {"supplies": supplies})