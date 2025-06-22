from django.db import models

# Create your models here.
LANG_CHOICES = {
    ('py', 'Python'),
    ('java', 'Java'),
    ('c#', 'C#'),
}


TAG_CHOICES = [
    ('back', 'Backend'),
    ('front', 'Frontend'),
    ('qa', 'Q&A'),
    ('ui', 'Design'),
    ('devops', 'DevOPS'),
]


GRADE_CHOICES = [
    ('junior', 'Junior'),
    ('middle', 'Middle'),
    ('senior', 'Senior'),
]


class Project(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    language = models.CharField(choices=LANG_CHOICES)

    def __str__(self):
        return f'{self.name}: {self.description}. Language: {self.language}'


class Tag(models.Model):

    name = models.CharField(max_length=255, choices=TAG_CHOICES)
    project = models.ManyToManyField('Project', related_name='tags', blank=True)


class Developer(models.Model):

    name = models.CharField(max_length=255)
    grade = models.CharField(choices=GRADE_CHOICES)
    project = models.ManyToManyField('Project', related_name='developers', blank=True)