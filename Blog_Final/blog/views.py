
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Comentario, Categoria, Perfil
from .forms import PostForm, ComentarioForm, CategoriaForm, PerfilForm

@login_required
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('listar_posts')
    else:
        form = PostForm()
    return render(request, 'crear_post.html', {'form': form})

@login_required
def listar_posts(request):
    posts = Post.objects.all()
    return render(request, 'listar_posts.html', {'posts': posts})

@login_required
def editar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('listar_posts')
    else:
        form = PostForm(instance=post)
    return render(request, 'editar_post.html', {'form': form})

@login_required
def eliminar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('listar_posts')
    return render(request, 'eliminar_post.html', {'post': post})
