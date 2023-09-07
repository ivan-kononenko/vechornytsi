from django.shortcuts import HttpResponse, render
from .models import Event
from django.views import generic

class MainView(generic.ListView):
    template_name = "event/main.html"
    context_object_name = "latest_event_list"
    def get_queryset(self):
        """Return the last five published events."""
        return Event.objects.order_by("-publication_date")[:5]



class EventView(generic.DetailView):
    model = Event
    template_name = "event/post.html"
~                                     
