from django.views.generic import ListView
from .models import Post #同じフォルダという意味で.を加えている

class PostListView(ListView):
    model = Post
    template_name = "tweet/index.html"
    context_object_name = 'posts'
    ordering = ('-date_posted')
    paginate_by = 5

class PostCreatteView(CreateView):
    model = Post
    fields = ['content']
    template_name = 'tweet/post_create.html'
    success_url = '/'

# Create your views here.
