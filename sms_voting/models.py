from django.db import models
from django.urls import reverse

class SMS(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    number_from = models.CharField(max_length=20)
    text = models.CharField(max_length=255)

class Poll(models.Model):
    title = models.CharField(max_length=1000)
    person = models.CharField(max_length=255, blank=True)
    jury_full_count = models.IntegerField(default=0)
    jury_add_count = models.IntegerField(default=0)
    face_participants = models.IntegerField(default=0)
    remote_participants = models.TextField(default='')
    doctor_count = models.IntegerField(default=0)
    start = models.DateTimeField(null=True, default=None, blank=True, editable=False)
    end = models.DateTimeField(null=True, default=None, blank=True, editable=False)
    yes_votes = models.IntegerField(default=0, editable=False)
    no_votes = models.IntegerField(default=0, editable=False)
    def get_absolute_url(self):
        return reverse('poll-update', kwargs={'pk': self.pk})
    def is_planned(self):
        return self.start is None and self.end is None
    def is_started(self):
        return self.start is not None and self.end is None
    def is_ended(self):
        return self.start is not None and self.end is not None
    def restart(self):
        self.start = None
        self.end = None
        self.yes_votes = 0
        self.no_votes = 0
        self.bulletin_set.all().delete()
    def __str__(self):
        return self.title
        

class Bulletin(models.Model):
    yes_word = models.ForeignKey('Word', on_delete=models.CASCADE, related_name='in_bulletin_yes')
    no_word = models.ForeignKey('Word', on_delete=models.CASCADE, related_name='in_bulletin_no')
    face_participant = models.BooleanField(default=False)
    remote_participant = models.CharField(max_length=255, null=True, default=None)
    in_poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    checked_by = models.ForeignKey(SMS, on_delete=models.CASCADE, null=True, default=None)
    def __str__(self):
        p = 'face' if self.face_participant else self.remote_participant
        return f'{self.in_poll} {p}'

class Word(models.Model):
    word = models.CharField(max_length=20, db_index=True)
    in_use = models.BooleanField(default=False)
    def __str__(self):
        return self.word
