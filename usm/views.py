from django.shortcuts import render,redirect
from django.contrib.auth import logout,login,authenticate
from .forms import RegisterForm,PostForm
from .models import Post
from django.contrib.auth.models import Group,User
from django.contrib.auth.decorators import login_required, permission_required


@login_required(login_url='/login')
def home(request):
    posts = Post.objects.all()
    
    if request.method == 'POST':
        post_id = request.POST.get('post-id')
        print(post_id)
        user_id = request.POST.get('user-id')
        print(user_id)
        
        if post_id:
            post = Post.objects.filter(id=post_id).first()
            if post and (post.author == request.user or request.user.has_perms('usm.delete_post')):
                post.delete()
        elif user_id:
            user = User.objects.filter(id = user_id).first()
            if user and request.user.is_staff:
                try:
                    group = Group.objects.get(name = 'default')
                    group.user_set.remove(user)
                except:
                    pass
                
                try:
                    group = Group.objects.get(name = 'mod')
                    group.user_set.remove(user)
                except:
                    pass
                
    return render(request,'home.html',{'posts': posts})


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/home')
    else:
        form = RegisterForm()
    return render(request,'registration/sign_up.html',{'form':form})
        


def custom_logout(request):
    logout(request)
    return redirect('/login') 

@login_required(login_url='/login')
@permission_required('usm.add_post', login_url='/login',raise_exception= True)
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect ('/home')
    
    else:
        form = PostForm()
        
    return render(request,'create_post.html',{'form':form})