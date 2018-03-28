from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import ListView
from .models import Post, Comment ,Agora
from .forms import PostForm, CommentForm, CreateUserForm ,AgoraForm



def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = raw_password)
            login(request, user)
            return redirect('study:post_list')
    else:
        form = CreateUserForm()
    return render(request, 'registration/signup.html', {'form' : form})
##
##def home(request):
##    posts = Post.objects.all()
##    
##    return render(request, 'bsr/home.html',{'posts': posts})

class postLV(ListView):
	model = Post
	template_name = 'bsr/post_list.html'
	context_object_name = 'posts'
	paginate_by = 10

	def get_queryset(self):
		qs = Post.objects.all()
		q = self.request.GET.get('q', '') # GET request의 get 인자중에 q 가 있으면 가져오고, 없으면 빈 문자열

		if q:
			qs = qs.filter(title__icontains=q)

		return qs

class homeLV(ListView):
    model = Post
    template_name = 'bsr/home.html'
##    context_object_name = 'posts'
    paginate_by = 5

    def get_context_data(self,**kwargs):
        context = super(homeLV,self).get_context_data(**kwargs)
##        context['Post'] = Post.objects.order_by('title')
        context['Agora'] = Agora.objects.order_by('title')
        return context
    
##    def get_queryset(self):
##        return Post.objects.order_by('title')

##class homeLV2(ListView):
##    model = Agora
##    template_name = 'bsr/home.html'
##    context_object_name = 'agora'
##    paginate_by = 5
##
##    def get_queryset(self):
##        return Agora.objects.order_by('title')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        if request.user.is_anonymous():
            return redirect('login')
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
        return redirect('study:post_detail', pk=post.pk)
    else:
        form = CommentForm()
        return render(request, 'bsr/post_detail.html', {'post':post, 'form':form})

@login_required
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect(post)
	else:
		form = PostForm()
	return render(request, 'bsr/post_new.html', {'form': form})


@login_required
def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES, instance=post)
		if form.is_valid():
			post = form.save()
			return redirect(post)

	else:
		if post.author == request.user:
			form = PostForm(instance=post)
			return render(request, 'bsr/post_edit.html', {'form':form})
		else:
			return render(request, 'bsr/warning.html')


@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author == request.user:
        post.delete()
        return redirect('study:post_list')
    else:
        return render(request, 'bsr/warning.html')

####AGORA

class agoraLV(ListView):
	model = Agora
	template_name = 'bsr/agora_list.html'
	context_object_name = 'agoras'
	paginate_by = 10

	def get_queryset(self):
		qs = Agora.objects.all()
		q = self.request.GET.get('q', '') # GET request의 get 인자중에 q 가 있으면 가져오고, 없으면 빈 문자열

		if q:
			qs = qs.filter(title__icontains=q)

		return qs

def agora_detail(request, pk_2):
    agora = get_object_or_404(Agora, pk=pk_2)
    if request.method == "POST":
        if request.user.is_anonymous():
            return redirect('login')
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.agora = agora
            comment.save()
        return redirect('study:agora_detail', pk_2=agora.pk)
    else:
        form = CommentForm()
        return render(request, 'bsr/agora_detail.html', {'agora':agora, 'form':form})

@login_required
def agora_new(request):
    if request.method == "POST":
            form = AgoraForm(request.POST, request.FILES)
            if form.is_valid():
                    agora = form.save(commit=False)
                    agora.author = request.user
                    agora.save()
                    return redirect(agora)
    else:
            form = AgoraForm()
    return render(request, 'bsr/agora_new.html', {'form': form})


@login_required
def agora_edit(request, pk_2):
    agora = get_object_or_404(Agora, pk=pk_2)
    if request.method == 'POST':
            form = AgoraForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                    agora = form.save()
                    return redirect(agora)

    else:
            if agora.author == request.user:
                    form = AgoraForm(instance=agora)
                    return render(request, 'bsr/agora_edit.html', {'form':form})
            else:
                    return render(request, 'bsr/warning.html')


@login_required
def agora_remove(request, pk_2):
    agora = get_object_or_404(Agora, pk=pk_2)
    if agora.author == request.user:
        agora.delete()
        return redirect('study:agora_list')
    else:
        return render(request, 'bsr/warning.html')
	    


####coment

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if comment.author == request.user:
        post_pk = comment.post.pk
        comment.delete()
        return redirect('study:post_detail', pk=post_pk)
    else:
        return render(request, 'bsr/warning.html')

@login_required
def comment_edit(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post = get_object_or_404(Post, pk=comment.post.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.created_date = timezone.now()
            comment.save()
        return redirect('study:post_detail', pk=post.pk)
        
    else:
        form_edit = CommentForm(instance=comment)
        return render(request, 'bsr/post_detail.html', {'post':post, 'form_edit':form_edit, 'pk':comment.pk})


##@login_required
##def comment_remove(request, pk):
##    comment = get_object_or_404(Comment, pk=pk)
##    if comment.author == request.user:
##        agora_pk = comment.agora.pk
##        comment.delete()
##        return redirect('bsr/agora_detail.html', pk=agora_pk)
##    else:
##        return render(request, 'bsr/warning.html')
##
##@login_required
##def comment_edit(request, pk):
##    comment = get_object_or_404(Comment, pk=pk)
##    agora = get_object_or_404(Agora, pk=comment.agora.id)
##
##    if request.method == "POST":
##        form = CommentForm(request.POST, instance=comment)
##        if form.is_valid():
##            comment = form.save(commit=False)
##            comment.created_date = timezone.now()
##            comment.save()
##        return redirect('bsr/agora_detail.html', pk=agora.pk)
##
##    else:
##        form_edit = CommentForm(instance=comment)
##        return render(request, 'bsr/agora_detail.html', {'agora':agora, 'form_edit':form_edit, 'pk':comment.pk})
