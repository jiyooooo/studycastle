from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from . models import Review
from . forms import ReviewForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from scproject import settings




class IndexView(generic.ListView):
    context_object_name = 'reviews'
    paginate_by = 10 # 한 페이지에 10개 조회

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
        return context
    def get_queryset(self):
        return Review.objects.order_by('-created_at')\

    # def test(self):
    #self.result = self.volume + self.runningtime + self.fun
    #self.result /= 3
      


# 게시글 작성
class WriteView(LoginRequiredMixin, generic.CreateView):
    login_url = settings.LOGIN_URL
    model = Review
    form_class = ReviewForm
    success_url = '/review/'


# 게시글 수정
class UpdateView(LoginRequiredMixin, generic.UpdateView):
    login_url = settings.LOGIN_URL
    model = Review
    form_class = ReviewForm
    success_url = '/review/'
    template_name_suffix = '_update'


# 게시글 삭제
class DeleteView(LoginRequiredMixin, generic.DeleteView):
    login_url = settings.LOGIN_URL
    model = Review
    success_url = '/review/'
    template_name_suffix = '_delete'


# 게시글 조회
class DetailView(generic.DetailView):
    model = Review
    context_object_name = 'review'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        review_id = context['object'].id
       
       
        return context



# 댓글 작성
def comment_write(request, review_id):
    if not request.user.is_authenticated:
        messages.error(request, '로그인이 필요합니다!')
        return redirect('user:login')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review:detail', pk=review_id)
    return redirect('review:detail', pk=review_id)



    