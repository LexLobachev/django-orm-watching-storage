from datacenter.models import Visit, get_duration_till_now, format_duration
from django.shortcuts import render

from django.utils.timezone import localtime


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at=None)

    non_closed_visits = []
    for visit in visits:
        duration = get_duration_till_now(visit)
        formatted_duration = format_duration(duration)

        entered_at = localtime(visit.entered_at).strftime("%d %B %Y г. %H:%M")

        non_closed_visits_data = {
            'who_entered': visit.passcard,
            'entered_at': entered_at,
            'duration': formatted_duration,
        }

        non_closed_visits.append(non_closed_visits_data)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
