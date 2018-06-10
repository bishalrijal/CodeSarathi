from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse 
from django.contrib.auth import authenticate, login
from .form import LoginForm ,UserRegistrationForm,PostForm,CommentForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Profile
from .models import Post,User,BlogPost
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
# Create your views here.
"""def user_login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponse('Authentication successfully')

                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalied Login')
        
    else:
        form = LoginForm()
            
    return render(request, 'account/login.html', {'form' : form })
    """


def firstpage(request):
    return render(request,'01landingpage.html',{})


def Dashboard(request):
    logged_in_user = request.user
    pic=Profile.objects.get(user=logged_in_user)
    picture=pic.photos
    logged_in_user_posts = Post.objects.filter(user=logged_in_user)
    if request.method == 'POST':
        Post_form = PostForm(data=request.POST)
        if Post_form.is_valid():
            new_Post = Post_form.save(commit=False)
            new_Post = Post_form.save()
            #new_Post.post = logged_in_user.posts
            #feed.user.add(*[request.user])
           # print(logged_in_user)
           # if request.user.is_authenticated:
            #    new_Post.created_by=request.user
            new_Post.user_id=request.user.id
            new_Post.save()
    return render(request,'account/dashboard.html',{'posts': logged_in_user_posts,'post_form':PostForm,'media_url':settings.MEDIA_URL})
    
def Register(request):
    if request.method == 'POST':
        user_form=UserRegistrationForm(request.POST)
        if user_form.is_valid():

            new_user=user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])


            new_user.save()
            
            return render(request,
                         'account/registration_done.html',
                         {'new_user':new_user}
                         )
                        
    else:
        user_form=UserRegistrationForm()
    return render(request,
                        'account/register.html',
                        {'user_form':user_form})

@login_required
def post_list(request):

    # posts=Post.published.all()
    object_list = BlogPost.published.all()
    paginator = Paginator(object_list, 2)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:

        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,'account/blog.html',{'posts':posts,'page':page})
    #return render(request, 'blog/post/list.html', {'posts': posts, 'page': page})


def post_detail(request,year,month,day,slug):
    post=get_object_or_404(BlogPost,
                           status='published',
                           publish__year=year,
                           publish__month=month,
                           publish__day=day,
                           slug=slug)
    comments=post.comments.filter(active=True)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post=post
            new_comment.save()
    else:
        comment_form=CommentForm()
    return render(request,'account/index.html',{'post':post,'comments':comments,'comment_form':comment_form,'slug':slug})



# Create your views here.
