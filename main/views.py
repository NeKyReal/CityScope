from django.http import JsonResponse
from django.shortcuts import render
from .forms import ContactForm


def home(request):
    return render(request, 'main/home.html')


def contact_form(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            form.save()
            return JsonResponse({"name": name}, status=200)
        else:
            errors = form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)

    return render(request, "main/about.html", {"form": form})
