from django.db import models
import uuid

class Context(models.Model):
    """The purpose of this model is to unite users with shared
       assignments into a single entity,
       for instance a group of students."""
    name = models.CharField(max_length=120, unique=True, verbose_name="Context")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField(max_length=250)
    creator_tag = models.CharField(max_length=120, unique=False, verbose_name="Context")

    def __str__(self):
        return self.name


class Subject(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120, unique=True)
    context = models.ForeignKey(Context, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Event(models.Model):
    URGENCY_CHOICES = [
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low')
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120, unique=True, verbose_name="Event")
    urgency = models.CharField(max_length=25, choices=URGENCY_CHOICES)
    created_at = models.DateTimeField(auto_now=True)
    deadline = models.TextField(max_length=250)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class User(models.Model):
    id = models.CharField(max_length=120, unique=True, primary_key=True)
    name = models.CharField(max_length=120, unique=True, verbose_name="User")
    context = models.ForeignKey(Context, on_delete=models.CASCADE)
    events = models.ManyToManyField(Event, through='PersonalizedEvent')
    notifications = models.BooleanField(default=True)

    def __str__(self):
        return self.id


class PersonalizedEvent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.id
