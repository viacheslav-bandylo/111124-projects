from django.db.models import F
from django.db.models.functions import Concat
from django.http import HttpResponse
from project.models import Project

# Create your views here.
def test(request):
    # new_project = Project(name='new_project',
    #                       lang='py',
    #                       description='new_project')
    # new_project.save()


    # Project.objects.all().delete()


    project1 = Project(name='ABC', description='ABC', language='c#')
    project2 = Project(name='DEF', description='DEF', language='java')
    project3 = Project(name='GHI', description='GHI', language='py')
    projects = [project1, project2, project3]
    Project.objects.bulk_create(projects)

    # Project.objects.update(name=F('name') + F('language'))

    # Project.objects.update(name=Concat(F('name'), Value(' '), F('language')))

    return HttpResponse('<h1>Something happened...</h1>')