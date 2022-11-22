from datacenter.models import Passcard, Visit, get_duration, is_visit_long
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import localtime


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []

    for visit in visits:
        duration = get_duration(visit)

        entered_at = localtime(visit.entered_at).strftime("%d %B %Y г. %H:%M")

        this_passcard_visits_data = {
            'entered_at': entered_at,
            'duration': duration,
            'is_strange': is_visit_long(visit)
        }
        this_passcard_visits.append(this_passcard_visits_data)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
