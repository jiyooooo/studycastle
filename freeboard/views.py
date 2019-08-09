from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from . models import Freeboard, Comment, FreeboardLikepoint
from . forms import FreeboardForm, CommentForm, FreeboardLikepointForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from scproject import settings
from django.db.models import Count, Avg


class IndexView(generic.ListView):
    context_object_name = 'freeboards'
    paginate_by = 5 # 한 페이지에 5개 조회

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5  # 한 페이지에 5개의 번호
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        context['page_range'] = paginator.page_range[start_index:end_index]

        # 추천 수가 가장 높은 3개
        context['hot_boards'] = Freeboard.objects.annotate(average_like=Avg('freeboardlikepoint__like_point')).exclude(
            average_like=None).order_by('-average_like')[:3]
        return context

    def get_queryset(self):
        return Freeboard.objects.order_by('-created_at')\
                .annotate(comment_count=Count('comment'))\
                .annotate(average_like=Avg('freeboardlikepoint__like_point'))


# 게시글 작성
class WriteView(LoginRequiredMixin, generic.CreateView):
    login_url = settings.LOGIN_URL
    model = Freeboard
    form_class = FreeboardForm
    success_url = '/freeboard/'


# 게시글 수정
class UpdateView(LoginRequiredMixin, generic.UpdateView):
    login_url = settings.LOGIN_URL
    model = Freeboard
    form_class = FreeboardForm
    success_url = '/freeboard/'
    template_name_suffix = '_update'


# 게시글 삭제
class DeleteView(LoginRequiredMixin, generic.DeleteView):
    login_url = settings.LOGIN_URL
    model = Freeboard
    success_url = '/freeboard/'
    template_name_suffix = '_delete'


# 게시글 조회
class DetailView(generic.DetailView):
    model = Freeboard
    context_object_name = 'freeboard'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        freeboard_id = context['object'].id
        context['comments'] = Comment.objects.filter(freeboard_id=freeboard_id).all()
        point = FreeboardLikepoint.objects.filter(freeboard_id=freeboard_id, username=self.request.user.username)
        if point.count():
            context['point'] = point[0].like_point
        return context


# 게시글 추천
def board_like(request):
    if not request.user.is_authenticated:
        messages.error(request, '로그인이 필요합니다!')
        return redirect('user:login')
    username = request.POST.get('username')
    freeboard_id = request.POST.get('freeboard')
    query_set = FreeboardLikepoint.objects.filter(freeboard=freeboard_id, username=username)
    if query_set.count():
        query_set.delete()
    form = FreeboardLikepointForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('freeboard:index')


# 댓글 작성
def comment_write(request, freeboard_id):
    if not request.user.is_authenticated:
        messages.error(request, '로그인이 필요합니다!')
        return redirect('user:login')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('freeboard:detail', pk=freeboard_id)
    return redirect('freeboard:detail', pk=freeboard_id)


# 댓글 삭제
def comment_delete(request, freeboard_id, comment_id):
    item = get_object_or_404(Comment, pk=comment_id)
    item.delete()
    return redirect('freeboard:detail', pk=comment_id)

