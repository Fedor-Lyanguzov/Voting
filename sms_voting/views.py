from datetime import datetime

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Poll, SMS
from .actions import *


class PollListView(LoginRequiredMixin, ListView):
    raise_exception = True
    model = Poll

class PollView(LoginRequiredMixin, UpdateView):
    raise_exception = True
    template_name = 'sms_voting/poll_detail.html'
    model = Poll
    fields = ['title', 'person', 'jury_full_count', 'jury_add_count', 'doctor_count', 'face_participants', 'remote_participants']
    def post(self, request, *args, **kwargs):
        res = super().post(request, *args, **kwargs)
        if res.status_code == 302:
            if 'start_poll' in request.POST:
                self.object.start = datetime.now()
                self.object.save()
                generate_bulletins(self.object)
                send_memos(self.object)
            elif 'end_poll' in request.POST:
                self.object.end = datetime.now()
                self.object.save()
                self.object.bulletin_set.all().delete()
            elif 'send_instructions' in request.POST:
                send_instructions(self.object)
            elif 'show_results' in request.POST:
                res = download_report(self.object)
            elif 'restart' in request.POST:
                self.object.restart()
                self.object.save()
            elif 'resend_memos' in request.POST:
                send_memos(self.object)
            elif 'download_memos' in request.POST:
                res = download_memos(self.object)
        return res

@csrf_exempt
def sms_endpoint(request):
    '''
    {'phone': ['79999999999'], 'mes': ['test'], 'id': ['200'], 'to': ['79138977777'], 'time': ['1636381583'], 'sent': ['1636381583'], 'smsc': ['7900000000'], 'sms_id': ['100']}
    '''
    print('got sms')
    try:
        if request.method=='POST':
            d = request.POST
            sms = SMS(number_from=d['phone'], text=d['mes'])
            sms.save()
            count_vote(sms)
            return HttpResponse("Thank you!")
    except:
        pass
    return HttpResponse("Thank you!")
