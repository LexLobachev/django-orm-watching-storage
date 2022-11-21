from datacenter.models import Visit
from django.shortcuts import render

from django.utils.timezone import localtime
from datetime import datetime, timezone


def get_duration(visit):
    enter_time = localtime(visit.entered_at)
    time_dif = datetime.now(timezone.utc) - enter_time
    return time_dif


def format_duration(duration):
    formatted_duration = str(duration)[:5]
    return formatted_duration


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at=None)

    non_closed_visits = []
    for i in range(len(visits)):
        duration = get_duration(visits)
        formatted_duration = format_duration(duration)

        entered_at = localtime(visits[i].entered_at).strftime("%d %B %Y г. %H:%M")

        non_closed_visits_data = {
            'who_entered': visits[i].passcard,
            'entered_at': entered_at,
            'duration': formatted_duration,
        }

        non_closed_visits.append(non_closed_visits_data)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
