from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PostForm, ProfileForm
from .models import Profile
from .models import Post


def home(request):
    posts = Post.objects.all()
    return render(request, 'core/home.html', {'posts': posts})

@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'core/add_post.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'core/register.html', {'form': form})


@login_required
def profile_detail(request):
    # get_or_create will fetch the existing Profile or create a new one
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'core/profile_detail.html', {'profile': profile})


@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'core/profile_form.html', {'form': form})

@user_passes_test(lambda u: u.is_staff)
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'core/post_confirm_delete.html', {'post': post})

@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'core/post_form.html', {'form': form})







