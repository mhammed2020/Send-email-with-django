from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post,Comment,Project
from django.contrib.auth.models import User

#comment form section

from .forms import NewComment

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

# class PostDetailView(DetailView):
#     model = Post


# class CommentDetailView(DetailView):
#     model = Comment
#     context_object_name = 'comments'



# function based views 

def post_detail(request,post_id) :
    
    post = get_object_or_404(Post,pk=post_id)
    comments = post.comments.all()
    # contributors = User.objects.all()
   

   
    if request.method == 'POST' :
        comment_form = NewComment(data = request.POST)

        if comment_form.is_valid() :
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            comment_form = NewComment()

    else :
        comment_form = NewComment()
    context ={
        'title':post,
        'post' : post,
        'comments':comments,
        'comment_form' :comment_form, 
    }


   
    return render(request,'blog/post_detail.html', context)



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

class ProjectListView(ListView):
    model = Project
    template_name = 'blog/allposts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'allposts'
    ordering = ['-created']
    paginate_by = 4

class ProjectDetailView(DetailView):
    model = Project


def allProjects(request):

    allPosts=Project.objects.all()

    context= {
        'allposts':allPosts,
    }
       
    return  render(request,'blog/allposts.html',context)
