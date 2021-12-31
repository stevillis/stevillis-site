from mysite.models import Formation


def get_all_formations():
    return Formation.objects.all().order_by('-end_date')
