from django.shortcuts import render
from django.views.generic import ListView , DetailView 
from django.views.generic.edit import CreateView , UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy



# Create your views here.
class BlogListView(ListView):
    paginate_by = 3
    model = Post
    template_name = 'blog/home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

class BlogCreateView(CreateView):
    model = Post
    template_name = "blog/post_new.html"
    fields = "__all__"

class BlogUpdateView(UpdateView):
    model = Post
    template_name = "blog/post_edit.html"
    fields = ['title' ,'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy('home')



def listing(request):
    Post_list = Post.objects.all()
    paginator = Paginator(Post_list, 3) # Show 25 Posts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/home.html', {'page_obj': page_obj})

def blogwrite(request):
    return render(request, 'blog/write.html')