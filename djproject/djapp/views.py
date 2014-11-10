from django.http import HttpResponse
from django.template import RequestContext, loader

from djapp.models import Enrollment


def list(request):
    """List all Enrollments."""
    enrollments_list = Enrollment.objects.order_by('-creation_date')[:5]
    template = loader.get_template('list.html')
    context = RequestContext(request, {
        'enrollments_list': enrollments_list,
    })
    return HttpResponse(template.render(context))
