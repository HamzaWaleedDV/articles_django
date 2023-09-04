from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import Authors
from myapp.models import Article
from django.core.exceptions import ObjectDoesNotExist
from myapp.forms import ArticleForm, AuthorForm
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator

# Create your views here.

def hello_world(request):
    return render(request, 'hello.html', {
        'name': 'Hamza',
        'age': '16',
        'gender': 'Male',
        'categories': [
            'Category 1',
            'Category 2',
            'Category 3'
        ],
        'message': 'hello how are you, no this is a taleek app this is not octucode this is learncode easily, hello hello hello'
    })




def home(request):
# authors = Authors()
# authors.name = 'Hamza'
# authors.email = 'hamza@example.com'
# authors.save()
# Authors.objects.create(
#     name='Noor', email='noor@example.com'
# )
# Authors.objects.create(
#     name='ahmed', email='ahmed@example.com'
# )
# Authors.objects.create(
#     name='ahmed17', email='ahmed17@example.com'
# )
# Authors.objects.create(
#     name='ahmed16', email='ahmed16@example.com'
# )
# Authors.objects.create(
#     name='ahmed15', email='ahmed15@example.com'
# )
# Authors.objects.create(
#     name='ahmed14', email='ahmed14@example.com'
# )
# Authors.objects.create(
#     name='ahmed13', email='ahmed13@example.com'
# )
# Authors.objects.create(
#     name='ahmed12', email='ahmed12@example.com'
# )
# Authors.objects.create(
#     name='ahmed11', email='ahmed11@example.com'
# )
# Authors.objects.create(
#     name='Noor10', email='noor10@example.com'
# )
# Authors.objects.create(
#     name='ahmed9', email='ahmed9@example.com'
# )
# Authors.objects.create(
#     name='ahmed8', email='ahmed8@example.com'
# )
# Authors.objects.create(
#     name='ahmed7', email='ahmed7@example.com'
# )
# Authors.objects.create(
#     name='ahmed6', email='ahmed6@example.com'
# )
# Authors.objects.create(
#     name='ahmed5', email='ahmed5@example.com'
# )
# Authors.objects.create(
#     name='ahmed4', email='ahmed4@example.com'
# )
# Authors.objects.create(
#     name='ahmed3', email='ahmed3@example.com'
# )
# Authors.objects.create(
#     name='ahmed2', email='ahmed2@example.com'
# )
# Authors.objects.create(
#     name='ahmed1', email='ahmed1@example.com'
# )

    return render(request, 'home.html')





def about(request):
    return render(request, 'about.html')




class ArticleListView(ListView):
    model = Article
    template_name = 'article/list.html'
    paginate_by = 6
    queryset = Article.objects.select_related('author').prefetch_related('tags')




class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/show.html'




class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article/create.html'
    success_url = reverse_lazy('article_list')




class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article/update.html'
    success_url = reverse_lazy('article_list')




class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article/delete.html'
    success_url = reverse_lazy('article_list')
    




class AuthorListView(ListView):
    model = Authors
    template_name = 'author/list.html'
    paginate_by = 4
    queryset = Authors.objects.all()




class AuthorDetailView(DetailView):
    model = Authors
    template_name = 'author/show.html'
    queryset = Authors.objects.all()
    context_object_name = 'author'




class AuthorCreateView(CreateView):
    model = Authors
    form_class = AuthorForm
    template_name = 'author/create.html'
    success_url = reverse_lazy('author_list')




class AuthorUpdateView(UpdateView):
    model = Authors
    form_class = AuthorForm
    template_name = 'author/update.html'
    success_url = reverse_lazy('author_list')



class AuthorDeleteView(DeleteView):
    model = Authors
    template_name = 'author/delete.html'
    success_url = reverse_lazy('author_list')

