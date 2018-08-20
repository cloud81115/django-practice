from django.contrib.auth.models import User
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import UpdateView, ListView
from django.utils import timezone
from .models import Board, Topic, Post
from .forms import NewTopicForm, PostForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Count
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.
"""def home(request):
	boards = Board.objects.all()
	return render(request,'home.html',{'boards':boards})"""
class BoardListView(ListView):
	model = Board
	context_object_name = 'boards'
	template_name = 'home.html'

def board_topics(request, pk):
	board = get_object_or_404(Board,pk=pk)
	queryset = board.topics.order_by('-last_updated').annotate(replies=Count('posts')-1)
	query = request.GET.get("q")
	if query:
		queryset = queryset.filter(
			Q(subject__icontains=query)|
			Q(posts__message__icontains=query))
	page_num = request.GET.get('page',1)
	paginator = Paginator(queryset ,10)
	#page= paginator.get_page(page_num)
	topics = paginator.get_page(page_num)

	return render(request, 'topics.html', {'board':board,'topics':topics})
# raw html form
"""def new_topic(request, pk):
	board = get_object_or_404(Board, pk=pk)
	if request.method=='POST':
		subject = request.POST['subject']
		message = request.POST['message']
		user = User.objects.first()
		topic = Topic.objects.create(
			subject=subject,
			board = board,
			starter=user
			)
		post = Post.objects.create(
			message=message,
			topic=topic,
			created_by=user
			)
		return redirect('board_topics', pk =board.pk)
	return render(request, 'new_topic.html', {'board':board})"""
@login_required
def new_topic(request, pk):
	board =get_object_or_404(Board, pk=pk)
	user = User.objects.first()
	if request.method=='POST':
		form=NewTopicForm(request.POST)
		if form.is_valid():
			topic = form.save(commit=False)
			topic.board = board
			topic.starter = request.user
			topic.save()
			post = Post.objects.create(
				message=form.cleaned_data.get('message'),
				topic=topic,
				created_by=request.user
				)
			return redirect('topic_posts', pk=pk, topic_pk=topic.pk)
	else:
		form=NewTopicForm()
	return render(request,'new_topic.html',{'board':board, 'form':form})


def topic_posts(request, pk, topic_pk):
	topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
	if not request.COOKIES.get('topic_%s_read'% topic_pk):
		topic.views+=1
		topic.save()
	queryset = topic.posts.order_by('-created_at','id')
	print(queryset)
	paginator = Paginator(queryset ,2)
	#print(paginator)
	page_num = request.GET.get('page',1)
	post_reply = paginator.get_page(page_num)
	#query = request.GET.get("q")
	#if query:
		#queryset = queryset.filter(subject__icontains=query)
	response = render(request, 'topic_posts.html', {'topic': topic,'post_reply':post_reply})
	response.set_cookie('topic_%s_read'% topic_pk,'true')
	return response

@login_required
def reply_topic(request, pk, topic_pk):
	topic =get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
	if request.method =='POST':
		form =PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.topic = topic
			post.created_by = request.user
			post.save()
			return redirect('topic_posts', pk=pk, topic_pk=topic_pk)
	else:
		form = PostForm()
	return render(request, 'reply_topic.html', {'topic':topic, 'form':form })

@method_decorator(login_required, name='dispatch')
class PostUpdateView(UpdateView):
	model = Post
	fields = ('message',)
	template_name = 'edit_post.html'
	pk_url_kwarg = 'post_pk'
	context_object_name = 'post'
	def get_queryset(self):
		queryset = super().get_queryset()
		return queryset.filter(created_by=self.request.user)

	def form_valid(self,form):
		post = form.save(commit=False)
		post.updated_by = self.request.user
		post.updated_at = timezone.now()
		post.save()
		return redirect('topic_posts', pk=post.topic.board.pk, topic_pk=post.topic.pk)
