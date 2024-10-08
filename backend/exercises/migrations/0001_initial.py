# Generated by Django 5.1 on 2024-08-29 21:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('communities', '0001_initial'),
        ('subjects', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statement', models.TextField(blank=True, null=True)),
                ('statement_img_url', models.CharField(blank=True, max_length=80, null=True)),
                ('explanation', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('theme', models.CharField(blank=True, max_length=100, null=True)),
                ('answered_by', models.ManyToManyField(related_name='questions_answered', to=settings.AUTH_USER_MODEL)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='questions_authored', to=settings.AUTH_USER_MODEL)),
                ('community', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='communities.community')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='subjects.subject')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionVotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positive', models.BooleanField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercises.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_votes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('theme', models.CharField(blank=True, max_length=100, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tests', to=settings.AUTH_USER_MODEL)),
                ('community', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tests', to='communities.community')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tests', to='subjects.subject')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='tests',
            field=models.ManyToManyField(blank=True, related_name='questions', to='exercises.test'),
        ),
        migrations.CreateModel(
            name='TestVotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positive', models.BooleanField()),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercises.test')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_votes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
                ('content_img_url', models.CharField(blank=True, max_length=80, null=True)),
                ('is_correct', models.BooleanField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='exercises.question')),
            ],
            options={
                'constraints': [models.CheckConstraint(condition=models.Q(models.Q(('content__isnull', False), ('content_img_url__isnull', True)), models.Q(('content__isnull', True), ('content_img_url__isnull', False)), _connector='OR'), name='content_or_content_img_url_constraint')],
            },
        ),
        migrations.AddConstraint(
            model_name='test',
            constraint=models.CheckConstraint(condition=models.Q(models.Q(('subject__isnull', False), ('community__isnull', True)), models.Q(('subject__isnull', True), ('community__isnull', False)), _connector='OR'), name='test_subject_or_community_constraint'),
        ),
        migrations.AddConstraint(
            model_name='test',
            constraint=models.CheckConstraint(condition=models.Q(('subject__isnull', False), ('theme__isnull', True), _connector='OR'), name='test_theme_only_in_community_constraint'),
        ),
        migrations.AddConstraint(
            model_name='question',
            constraint=models.CheckConstraint(condition=models.Q(models.Q(('statement__isnull', False), ('statement_img_url__isnull', True)), models.Q(('statement__isnull', True), ('statement_img_url__isnull', False)), _connector='OR'), name='statement_or_statement_img_url_constraint'),
        ),
        migrations.AddConstraint(
            model_name='question',
            constraint=models.CheckConstraint(condition=models.Q(models.Q(('subject__isnull', False), ('community__isnull', True)), models.Q(('subject__isnull', True), ('community__isnull', False)), _connector='OR'), name='question_subject_or_community_constraint'),
        ),
        migrations.AddConstraint(
            model_name='question',
            constraint=models.CheckConstraint(condition=models.Q(('subject__isnull', False), ('theme__isnull', True), _connector='OR'), name='question_theme_only_in_community_constraint'),
        ),
    ]
