from django.shortcuts import render
from .models import Thought, Comment
from django.views.generic import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView 
from django.shortcuts import get_object_or_404, redirect
from .forms import ShareThoughtForm
 


# Create your views here.

# VIEW FOR CREATE THOUGHT
class ThoughtCreateView(CreateView):
    model = Thought
    fields = ['title','content',  'img', 'is_private']

    success_url = '/thought/ThoughtListView/'

#  TO GET THE REQUESTED USER
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



# # VIEW FOR THOUGHT LIST
# class ThoughtListView(ListView):
#     model = Thought

# #GET QUERYSET OF PUBLIC THOUGHTS
#     def get_queryset(self):
#         return Thought.objects.all().filter(is_private = False).order_by('-created_at')



class ThoughtListView(ListView):
    model = Thought

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            object_list = Thought.objects.filter(title__icontains=query, is_private=False).order_by('-created_at')
        else:
            object_list = Thought.objects.filter(is_private=False).order_by('-created_at')
        return object_list

    


# VIEW FOR ALL MY THOUGHTS
class MyThoughts(ListView):
    model = Thought
    ordering = ['-created_at']

# GET QUERYSET OF LOGED IN USER 
    def get_queryset(self):
        return Thought.objects.filter(author=self.request.user).order_by('-created_at')



#  THOUGHT DETAIL VIEW
class ThoughtDetailView(DetailView):
    model = Thought

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        thought = context['object']  
        comments = Comment.objects.filter(thought=thought)
        context['comments'] = comments
        context['comments'] = thought.comment_set.order_by('-time')

        return context


# COMMENT ON THOUGHT VIEW
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



# UPDATE THE THOUGHT VIEW
class ThoughtUpdateView(UpdateView):
    model = Thought
    fields = ['title','content', 'img', 'is_private']

    success_url = '/thought/ThoughtListView/'
 

# SHARE THE THOUGHT VIEW
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



# TO CHECK THE SHARE THEOUGHT WITH ME 
class SharedWithMe(ListView):
    model = Thought

    template_name = 'shared_with_me.html'  
    context_object_name = 'thoughts'
    
    def get_queryset(self):
        return Thought.objects.filter(shared_with=self.request.user)
    


# DELETE THOUGHT VIEW
class ThoughtDeleteView(DeleteView):
    model = Thought
    
    success_url = '/thought/ThoughtListView/'




# def search(request):
#     search = request.GET.get('search')
#     if search:
#         if search == '' or search == None:
#             thoughts = Thought.objects.filter.all().order_by('-created_at')
#             return render(request, 'thought_list.html', {'thoughts': thoughts})
#         else:
#             thoughts = Thought.objects.filter(title__contains=search).all()
#             return render(request, 'thought_list.html', {'thoughts': thoughts})
                                                 