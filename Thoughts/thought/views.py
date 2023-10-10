from django.shortcuts import render
from .models import Thought, Comment
from django.views.generic import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView 
from django.shortcuts import get_object_or_404, redirect
from .forms import ShareThoughtForm



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
 

def share_thought(request, pk):
    thought = get_object_or_404(Thought, pk=pk)

    if request.method == 'POST':
        form = ShareThoughtForm(request.POST)
        if form.is_valid():
            shared_with_users = form.cleaned_data['shared_with']
            thought.shared_with.add(*shared_with_users)
            thought.save()               

            return redirect('ThoughtDetailView', pk=pk)
    else:
        form = ShareThoughtForm()

    return render(request, 'share_thought.html', {'thought': thought, 'form': form})




class SharedWithMe(ListView):
    model = Thought

    template_name = 'shared_with_me.html'  
    context_object_name = 'thoughts'
    
    def get_queryset(self):
        return Thought.objects.filter(shared_with=self.request.user)