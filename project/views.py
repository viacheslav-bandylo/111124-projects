# import some libraries
from django.db.models import F
from django.db.models.functions import Concat
from django.http import HttpResponse
from project.models import Project, Task
from project.serializers import TaskListSerializer, ProjectListSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator


# Create your views here.
# def test(request):
    # new_project = Project(name='new_project',
    #                       lang='py',
    #                       description='new_project')
    # new_project.save()

    # Project.objects.all().delete()

    # project1 = Project(name='ABC', description='ABC', language='c#')
    # project2 = Project(name='DEF', description='DEF', language='java')
    # project3 = Project(name='GHI', description='GHI', language='py')
    # projects = [project1, project2, project3]
    # Project.objects.bulk_create(projects)

    # Project.objects.update(name=F('name') + F('language'))

    # Project.objects.update(name=Concat(F('name'), Value(' '), F('language')))

    # return HttpResponse('<h1>Something happened...</h1>')


@api_view(['GET'])
def list_projects(request):
    project = Project.objects.all()
    if project.exists():
        serializer = ProjectListSerializer(project, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'No projects found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def list_tasks(request):
    task = Task.objects.all()
    if task.exists():
        serializer = TaskListSerializer(task, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'No tasks found'}, status=status.HTTP_404_NOT_FOUND)

def test(request):
#     pass
    # ____ create new object with save()
    # new_project = Project(name='new_project', lang='py', description='new_project test')
    # new_project.save()

    # ____ delete object
    # del_obj = Project.objects.filter(id__gt=4)
    # del_obj.delete()

    # ____ create new object with create()
    # Project.objects.create(name='Speicher', description="new_project", lang="ruby")

    # ____ create new objects with bulk and []
    # project_1 = Project(name='Project 1', lang='java', description='propro1')
    # project_2 = Project(name='Project 2', lang='py', description='propro2')
    # project_3 = Project(name='Project 3', lang='ruby', description='propro3')
    # projects = [project_1, project_2, project_3]
    # Project.objects.bulk_create(projects)

    # ____ update object data with bulk
    # data_projects = Project.objects.all()
    # for project in data_projects:
    #     project.lang = "py"
    # Project.objects.bulk_update(data_projects, ['lang'])

    # update object name with F
    # Project.objects.update(name=Concat(F('name'), Value(' '), F('lang')))


    ########################################### 27.06.2025 #############################################
    # annotate projects. set a day of week
    # projects = Project.objects.filter(created_at__lte="2025-06-25")
    # # print(projects)
    # for project in projects:
    #     print(f"Project name: {project.name} and created at: {project.created_at}")
    # print(f"Count of projects: {projects.count()}")


    # output an amount of tasks for every project
    # annotated_projects = Project.objects.annotate(weekday=ExtractWeekDay('created_at'))
    # project_per_day = annotated_projects.filter(weekday=2)
    # for n, project in enumerate(project_per_day, start=1):
    #     print(f"{n}, Project title: {project.name}")
    #print(f'The total number of projects is {Project.objects.all().count()}')


    # output the amount of tasks for every project
    # projects = Project.objects.all()
    # for project in projects:
    #     task_count = project.tasks.aggregate(count=Count('id'))
    #     print(f"Project: {project} -> number of tasks: {task_count['count']}")


    # annotated_users = User.objects.annotate(number_of_tasks=Count('tasks__id')).values_list('username', 'number_of_tasks')
    # for user in annotated_users:
    #     print(f"User {user[0]} has following number of tasks: {user[1]}")


    # importing model Task
    # # Напишите запрос, который сможет отсортировать всезадачи по нескольким полям:
    # # - приоритет
    # # - дедлайн
    # # Выведите название задачи, приоритет и дату завершения.
    # tasks = Task.objects.all().order_by('priority', 'due_date')
    # for task in tasks:
    #     print(f"Tasks title is: {task.name}, has priority: {task.priority} and has dead line at: {task.due_date}")


    # Сортировка пользователей по количеству задач
    # annot_users = User.objects.all().annotate(tasks_number=Count('tasks__id'))
    # ordered_users = annot_users.order_by('-tasks_number').values_list('username', 'tasks_number')
    # for user in ordered_users:
    #     print(f"\tFor {user[0]} NUMBER of tasks is \033[31m{user[1]}\033[m")


    # Task 9: Пагинация для задач
    all_tasks = Task.objects.all()
    paginator = Paginator(all_tasks, 2)
    tasks_per_page = paginator.get_page(1)
    for task in tasks_per_page:
        print(f"{'':-<60}")
        print(f"\tTask - {task}, \033[35m{task.due_date}\033[m")

    return HttpResponse('Hello my Bro')