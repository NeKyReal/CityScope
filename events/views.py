from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin
from .json import json_reader, json_writer
from .models import Events, Featured, Review, Wishlist
from django.db.models import Q
from .forms import EventForm, ReviewForm
from django.views.generic import DetailView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required


class EventsDetailView(DetailView, FormMixin):
    model = Events
    template_name = 'events/details_view.html'
    context_object_name = 'event'
    form_class = ReviewForm

    def get_success_url(self, **kwargs):
        return reverse_lazy('events-detail', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.name = self.request.user
        self.object.event = self.get_object()
        self.object.save()
        return super().form_valid(form)


class EventsUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'events.change_events'
    model = Events
    template_name = 'events/create.html'
    form_class = EventForm


class EventsDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'events.delete_events'
    model = Events
    success_url = '/events/'
    template_name = 'events/delete_event.html'


class SearchResultsView(ListView):
    model = Events
    template_name = 'events/search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Events.objects.filter(Q(title__icontains=query) | Q(announcement__icontains=query) | Q(description__icontains=query))
        return object_list


@login_required
def wishlist(request, pk):
    add = json_reader("wishlist.json")
    wish = {'user': request.user.id, 'wish': pk}
    add.append(wish)
    json_writer("wishlist.json", add)
    return redirect('home')


def all(request):
    events = Events.objects.order_by('-date')
    return render(request, 'events/all.html', {'events': events})


@login_required
@permission_required('events.add_events', raise_exception=True)
def create(request):
    error = ''
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all')
        else:
            error = 'Форма была неверной'

    form = EventForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'events/create.html', data)

