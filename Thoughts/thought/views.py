from .models import Thought
from django.views.generic import CreateView
from django.views.generic.list import ListView

# Create your views here.


class ThoughtCreateView(CreateView):
    model = Thought
    fields = ['title','content',  'img', 'is_private']

    success_url = '/thought/ThoughtListView/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ThoughtListView(ListView):
    model = Thought
    ordering = ['-created_at'] 