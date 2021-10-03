# Generated by Django 3.2.7 on 2021-10-03 16:40

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Context',
            fields=[
                ('name', models.CharField(max_length=120, unique=True, verbose_name='Context')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.TextField(max_length=250)),
                ('creator_tag', models.CharField(max_length=120, unique=True, verbose_name='Context')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120, unique=True, verbose_name='Event')),
                ('urgency', models.CharField(choices=[('H', 'High'), ('M', 'Medium'), ('L', 'Low')], max_length=25)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('deadline', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalizedEvent',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_completed', models.BooleanField(default=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.event')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=120, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=120, unique=True, verbose_name='User')),
                ('context', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.context')),
                ('events', models.ManyToManyField(through='api.PersonalizedEvent', to='api.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120, unique=True)),
                ('context', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.context')),
            ],
        ),
        migrations.AddField(
            model_name='personalizedevent',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user'),
        ),
        migrations.AddField(
            model_name='event',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.subject'),
        ),
    ]
