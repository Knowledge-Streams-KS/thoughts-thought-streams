from .models import Thought, Comment
from django.views.generic import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView 


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



#  DETAIL VIEW
class ThoughtDetailView(DetailView):
    model = Thought

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        thought = context['object']  # Get the thought object
        comments = Comment.objects.filter(thought=thought)
        context['comments'] = comments
        context['comments'] = thought.comment_set.order_by('-time')

        return context




class CommentCreateView(CreateView):
    model = Comment
    fields = ['text']

    # success_url = '/thought/ThoughtListView/'

    def form_valid(self, form):
        thought_id = self.kwargs['thought_id']  
        thought = Thought.objects.get(id=thought_id)
        form.instance.thought = thought
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('ThoughtDetailView', kwargs={'pk': self.kwargs['thought_id']})




class ThoughtUpdateView(UpdateView):
    model = Thought
    fields = ['title','content', 'img', 'is_private']

    success_url = '/thought/ThoughtListView/'
