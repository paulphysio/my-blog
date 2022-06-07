from django.forms import models
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import BlogPost, Profile, Comment
from .forms import PostForm, EditPostForm, CommentForm
from django.http import HttpResponseRedirect


# Create your views here.
def LikeView(request, pk):
    post = get_object_or_404(BlogPost, id = request.POST.get('blogpost_id'))
    liked = False

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True    
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))



class HomeView(ListView):
    model = BlogPost
    template_name = 'home.html'
    ordering = ['-post_date']
    



class ArticleDetailView(DetailView):
    model = BlogPost
    template_name = 'article_detail.html'
    def get_context_data(self, *args, **kwargs):

        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(BlogPost, id=self.kwargs[str('pk')])
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked=True
        total_likes = stuff.total_likes()
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

    
class AddPostView(CreateView):
    model = BlogPost
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comments.html'
    
    
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('home')


class UserEditView(UpdateView):
    model = BlogPost
    form_class = EditPostForm
    template_name = 'update_post.html'
    
class UserDeleteView(DeleteView):
    model = BlogPost
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

def CategoryView(request, cats):
    category_posts = BlogPost.objects.filter(category = cats.replace('-', ' '))
    return render(request, 'category.html', {'cats':cats.title().replace('-', ' '), 'category_posts': category_posts })
    