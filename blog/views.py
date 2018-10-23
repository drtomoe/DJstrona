from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post

# Create your views here./ coś jak 'routs' we flasku

#       przykład view'sa funkcyjnego
def home(request):
    context = {'post': Post.objects.all()}      #zapytanie o wszytskie posty jako obikety
    return render(request, 'blog/home.html', context)  # pierwszy argument zawsze 'request', potem templates
                                                        #zmienne zawsze przekazujemy jako bibliotekę

#       przykład view'sa obiektowego/class
class PostListView(ListView):
    model = Post
    #w tej formie obiekt bedzie szukał automatycznie templatu blog/post_list.html, można go przekierować na 'home.html'
    template_name = 'blog/home.html'
    context_object_name = 'posts'   #to nazwanie zmiennej 'posts', żeby template-home.html wiedział a czym operować
    ordering = ['-date_posted']  #'-' minus z poczatku odwraca kolejność sortowania
    paginate_by = 4


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')



class PostDetailView(DetailView):
    model = Post
    #domyślny template - blog/post_detail.html, context nazywa sie object (nie post)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user #formulrz.obecny.autor = self/aktualnie zarejestrowany.zapytaj_o.użytkownik
        return super().form_valid(form) #jeśli się validuje, to zapisz przekazany formularz
            #ta funkcja domyślnie zapisuje zvalidowany form, ale tutaj podstawiamy form zmodyfikowany
            # super() --> odnosi się do 'parent-class' czyli dla funkcji xx klasy-rodzica


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):    #test, jaki musi przejść user dla UserPassesTestMixin czy jest autorem posta
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'       #jak skasujesz to przekieruj na home = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})
