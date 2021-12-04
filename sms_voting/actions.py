import random
from itertools import cycle
from io import StringIO
from django.template.loader import render_to_string
from django.http import FileResponse, HttpResponse
from django.core.mail import send_mail
from django.db.models.functions import Length
from .models import Poll, Bulletin, Word

def generate_yes_word(n=5):
    word = random.choice(Word.objects.annotate(word_len=Length('word')).filter(in_use=False,
        word_len=n))
    word.in_use = True
    word.save()
    return word

def generate_no_word():
    return generate_yes_word(n=7)

def emails(s):
    return [x.strip() for x in s.strip().split('\n') if x.strip()]

def generate_bulletins(poll):
    poll.bulletin_set.all().delete()
    for _ in range(poll.face_participants):
        Bulletin(
                yes_word=generate_yes_word(), 
                no_word=generate_no_word(), 
                face_participant=True,
                in_poll=poll
                ).save()
    for email in emails(poll.remote_participants):
        Bulletin(
                yes_word=generate_yes_word(), 
                no_word=generate_no_word(), 
                remote_participant=email,
                in_poll=poll
                ).save()

def send_memos(poll):
    for bulletin in poll.bulletin_set.filter(remote_participant__isnull=False):
        email = bulletin.remote_participant
        topic = "Памятка для тайного электронного голосования"
        body = render_to_string("sms_voting/memo.html",
                {"yes_word": str(bulletin.yes_word), "no_word": str(bulletin.no_word), "voting_number": "+7-977-000-46-92"}
                )
        send_email(email, topic, body)
def send_instructions(poll):
    for email in emails(poll.remote_participants):
        topic = "Инструкции для тайного электронного голосования"
        body = render_to_string("sms_voting/instructions.html", {})
        send_email(email, topic, body)
def download_report(poll):
    ctx = {
            'poll_date': poll.start,
            'person': poll.person,
            'jury_full_count': poll.jury_full_count,
            'jury_add_count': poll.jury_add_count,
            'jury_sum_count': poll.face_participants + len(emails(poll.remote_participants)),
            'jury_face_count': poll.face_participants,
            'jury_remote_count': len(emails(poll.remote_participants)),
            'jury_doctor_count': poll.doctor_count,
            'yes_votes': poll.yes_votes,
            'no_votes': poll.no_votes,
            }
    body = render_to_string("sms_voting/report.html", ctx)
    return HttpResponse(body)
    body = pypandoc.convert_text(body, 'pdf', format='html')
    return FileResponse(StringIO(body), filename=f'{poll.title}.pdf')
def download_memos(poll):
    ctx = {
            'bulletins': poll.bulletin_set.filter(face_participant=True),
            "voting_number": "+7-977-000-46-92",
            }
    body = render_to_string("sms_voting/memos_face.html", ctx)
    return HttpResponse(body)
    body = pypandoc.convert_text(body, 'pdf', format='html')
    return FileResponse(StringIO(body), filename=f'memos_{poll.title}.pdf')

def send_email(email, topic, body):
    send_mail(
            topic,
            "",
            None,
            [email],
            fail_silently=False,
            html_message=body
            )

def count_vote(sms):
    word = sms.text.strip().lower()
    word = Word.objects.get(word=word)
    #b = Bulletin.objects.get(yes_word__exact=word, checked_by__isnull=True)
    try:
        b = word.in_bulletin_yes.get()
    except:
        b = None
    if b and b.checked_by is None:
        b.checked_by = sms
        b.save()
        poll = b.in_poll
        poll.yes_votes += 1
        poll.save()
        print('YES:', word)
        print('report:', poll.yes_votes, poll.no_votes)
    else:
        #b = Bulletin.objects.get(no_word__exact=word, checked_by__isnull=True)
        try:
            b = word.in_bulletin_no.get()
        except:
            b = None
        if b and b.checked_by is None:
            b.checked_by = sms
            b.save()
            poll = b.in_poll
            poll.no_votes += 1
            poll.save()
            print('NO:', word)
            print('report:', poll.yes_votes, poll.no_votes)
