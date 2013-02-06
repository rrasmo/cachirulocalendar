from django.shortcuts import render_to_response
from django import forms
from django.template import RequestContext
from events.models import Event, Community


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
    else:
        form = CommunitiesForm()
        form.fields['select'].choices = choices
        form.fields['select'].initial = ids
        selected = ids

    events = Event.objects.filter(community_id__in=selected).order_by('start_date')

    return render_to_response('events/index.html', {'events': events, 'form': form}, context_instance = RequestContext(request))

