# Generated by Django 5.2.3 on 2025-06-22 16:01

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('profile', models.URLField(blank=True, null=True, verbose_name='Profile URL')),
                ('is_deleted', models.BooleanField(default=False, help_text='When the author is deleted is set False', verbose_name='Is Deleted')),
                ('rating', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Rating in AWS')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Category Title')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Library Title')),
                ('location', models.CharField(blank=True, max_length=100, null=True, verbose_name='Location')),
                ('website', models.URLField(blank=True, null=True, verbose_name='Website')),
            ],
            options={
                'verbose_name_plural': 'Libraries',
            },
        ),
        migrations.CreateModel(
            name='AuthorDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biography', models.TextField(verbose_name='Biography')),
                ('city', models.CharField(blank=True, max_length=50, null=True, verbose_name='City')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=20, verbose_name='Gender')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.author', verbose_name='Author')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Book Title')),
                ('publication_date', models.DateField(null=True, verbose_name='Publication Date')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Summary')),
                ('Genre', models.CharField(blank=True, choices=[('Fiction', 'Fiction'), ('Non Fiction', 'Non-Fiction'), ('Sci-Fy', 'Science Fiction'), ('Fantasy', 'Fantasy'), ('Mystery', 'Mystery'), ('Biography', 'Biography'), ('Default', 'not_set')], max_length=100, null=True, verbose_name='Genre')),
                ('amount_pages', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(10000)], verbose_name='Amount of Pages')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.author', verbose_name='Author')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books', to='library.category', verbose_name='Category')),
                ('libraries', models.ManyToManyField(related_name='books', to='library.library', verbose_name='Library')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Event name')),
                ('description', models.TextField(verbose_name='Event description')),
                ('timestamp', models.DateTimeField(verbose_name='Event date')),
                ('book', models.ManyToManyField(related_name='events', to='library.book', verbose_name='Books')),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.library', verbose_name='Library')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=20, verbose_name='Gender')),
                ('date_of_birth', models.DateField(verbose_name='Date of Birth')),
                ('age', models.PositiveIntegerField(editable=False, verbose_name='Age')),
                ('role', models.CharField(choices=[('A', 'Administrator'), ('B', 'Reader'), ('E', 'Employee')], max_length=30, verbose_name='Role')),
                ('active', models.BooleanField(default=True, verbose_name='Is_active')),
                ('libraries', models.ManyToManyField(related_name='members', to='library.library', verbose_name='Library')),
            ],
        ),
        migrations.CreateModel(
            name='EventParticipant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register_date', models.DateField(auto_now_add=True, verbose_name='Register date')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.event', verbose_name='Event name')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.member', verbose_name='Member')),
            ],
        ),
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_take_date', models.DateField(auto_now_add=True, verbose_name='Book Take Date')),
                ('book_return_date', models.DateField(verbose_name='Book Return Date')),
                ('is_returned', models.BooleanField(default=False, verbose_name='Is returned?')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book', verbose_name='Book')),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.library', verbose_name='Library')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.member', verbose_name='Member')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.member', verbose_name='Publisher'),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(verbose_name='Created at')),
                ('title', models.CharField(max_length=255, unique_for_date='created_at', verbose_name='Title')),
                ('text', models.TextField(verbose_name='Text')),
                ('moderated', models.BooleanField(default=False, verbose_name='Moderated?')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.member', verbose_name='Author')),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.library', verbose_name='Library')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Rating')),
                ('review', models.TextField(verbose_name='Review')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='library.book', verbose_name='Book')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.member', verbose_name='Reviewer')),
            ],
        ),
    ]
