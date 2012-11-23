from django.shortcuts import render_to_response
from events.models import Event


def home(request):
    events = Event.objects.all().order_by('start_date')
    return render_to_response('events/index.html', {'events': events})
