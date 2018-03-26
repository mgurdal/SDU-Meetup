from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.renderers import JSONRenderer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
from event.models import Member
from datetime import datetime
from django.views import View


class Main(TemplateView):
    template_name = "index.html"

class Dashboard(TemplateView):
    template_name = "dashboard/index.html"

@method_decorator(csrf_exempt, name='dispatch')
class DashboardDataTable(LoginRequiredMixin, View):

    renderer_classes = (JSONRenderer, )

    def post(self, request, format = None):
        per_page = int(request.POST.get('pagination[perpage]', 5))

        page = int(request.POST.get('pagination[page]', 1))

        sort_field = request.POST.get('sort[field]', 'registeration_date')
        sort_order = str(request.POST.get('sort[sort]', 'asc'))
        sort = '{}{}'.format('-' if sort_order == 'desc' else '', sort_field)

        dashboard_data = Member.objects.all().order_by(sort)
        paginator = Paginator(dashboard_data, per_page)

        datatable_data = {
            'meta': {
                'page': page,
                'pages': paginator.num_pages,
                'perpage': per_page,
                'total': paginator.count,
                'sort': sort_order,
                'field': sort_field
            },
            'data': []}
        
        for student in paginator.page(page):
            datatable_data['data'].append(
                {
                    'id': student.id,
                    'student_no': student.student_no,
                    'title': student.title,
                    'name': student.name,
                    'lastname': student.last_name,
                    'university_branch': student.university_branch,
                    'selected_education': student.selected_education,
                    'registeration_date': student.registeration_date.strftime('%Y-%m-%d')
                }


            )
        return JsonResponse(datatable_data)

