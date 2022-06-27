from django.shortcuts import get_object_or_404, render

from  django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

from .models import Category, PostPlan , comment
from blog.forms import CommentForm


# Create your views here.

def post_list(request,category=None):
    
    posts = PostPlan.published.all().order_by("-publication")
    categories=Category.objects.all()
    if category:
        category =get_object_or_404(Category, slug=category)
        posts=posts.filter(category=category).order_by("-publication")
    paginator = Paginator(posts , 6)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger :
        posts = paginator.page(1)
    except EmptyPage :
            posts = paginator.page(paginator.num_pages)
    context = {
        'posts': posts,
        'page': page,
        'categories': categories
    }
    return render(request, 'blog/Post/List.html', context )

# class PostListView(generic.ListView):
#     queryset = PostPlan.objects.all()
#     paginate_by = 4 
#     template_name = 'blog/Post/List.html'
#     context_object_name= 'posts'
    
    
def post_detail (request, year :int,month :int,day :int, slug : str):
    post= get_object_or_404(PostPlan, slug=slug,status='publier',publication__year=year,publication__month=month,publication__day=day)
    categories=Category.objects.all()
   # return render (request,'blog/Post/Detail.html', {'post': post})
    comments =comment.objects.filter(post=post.id)
    new_comment = None
    if request.method=='POST' :
        comment_form =CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post= post
            new_comment.save()
    else:
        comment_form=CommentForm()
    try :
      post.nb_affichage=int(post.nb_affichage)+1
      
    except:
        post.nb_affichage="0"
    post.save()
    return render(request ,'blog/Post/Detail.html',{'post' : post,
                                                    'comments' : comments,
                                                    'new_comment':new_comment,
                                                    'categories': categories,
                                                    'comment_form':comment_form,
                                                    })
