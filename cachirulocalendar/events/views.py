from django.shortcuts import render_to_response
from django import forms
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from events.models import Event, Community
from datetime import datetime
import vobject
import scrappers


def home(request):

    class CommunitiesForm(forms.Form):
        select = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple)

    communities = Community.objects.all().order_by('name')
    choices = map(lambda c: (c.id, c.name), communities)
    ids = map(lambda c: c.id, communities)

    if request.method == 'POST':
        form = CommunitiesForm(request.POST)
        form.fields['select'].choices = choices
        if form.is_valid():
            selected = form.cleaned_data['select']
        output = request.POST['output']
    else:
        form = CommunitiesForm()
        form.fields['select'].choices = choices
        form.fields['select'].initial = ids
        selected = ids
        output = 'html'

    events = Event.objects.filter(community_id__in=selected).order_by('start_date')

    if output == 'iCal':
        cal = vobject.iCalendar()
        cal.add('method').value = 'PUBLISH'
        for event in events:
            vev = cal.add('vevent')
            vev.add('dtstart').value = event.start_date
            vev.add('dtend').value = event.end_date
            vev.add('dtstamp').value = event.pub_date or datetime.now()
            vev.add('summary').value = event.name
            vev.add('description').value = event.description or ''
            vev.add('location').value = event.place or ''
            vev.add('url').value = event.url or ''
            vev.add('organizer').value = event.community.name
        response = HttpResponse(cal.serialize(), mimetype='text/calendar')
        response['Filename'] = 'calendar.ics'
        response['Content-Disposition'] = 'attachment; filename=calendar.ics'
        return response
    else:
        return render_to_response('events/index.html', {'events': events, 'form': form}, context_instance = RequestContext(request))


def scrap(request):
    scrappers.scrap_zgzactiva()
    return HttpResponseRedirect('/')


