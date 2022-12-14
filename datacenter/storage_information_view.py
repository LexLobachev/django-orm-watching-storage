from datacenter.models import Visit, get_duration, format_duration
from django.shortcuts import render


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at=None)

    non_closed_visits = []
    for visit in visits:
        duration = get_duration(visit)
        formatted_duration = format_duration(duration)

        non_closed_visits_data = {
            'who_entered': visit.passcard,
            'entered_at': visit.entered_at,
            'duration': formatted_duration,
        }

        non_closed_visits.append(non_closed_visits_data)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
