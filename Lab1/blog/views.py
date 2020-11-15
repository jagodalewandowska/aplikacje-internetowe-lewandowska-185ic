from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
# wymaganie logowania by dodać post
from django.contrib.auth.decorators import login_required


# pobieranie request i zwracanie wartości -- blog/post_list.html
def post_list(request):
    # sortowanie postów (QuerySet)
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    # blog/post_list.html - szablon
    # {} - jakie elementy można dodać do szablonu
    return render(request, 'blog/post_list.html', {'posts':posts})

# w przypadku braku postów zostanie wyświetlony błąd
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

@login_required
def post_new(request):
    # 1 sytuacja - w przypadku dodania postu na pustej stronie; 2 sytuacja - kiedy chcemy zobaczyć listę postów
    if request.method == "POST":
        # powstanie formularza z danymi
        form = PostForm(request.POST)
        # sprawdzanie czy jest poprawny
        if form.is_valid():
            # commit = false w przypadku, kiedy nie chcemy zapisać a dodać autora
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            # powrót do post_detail/pk/
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')