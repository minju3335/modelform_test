from django.shortcuts import render
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()

    context = {
        'articles':articles
    }

    return render(request, 'index.html', context)

def create(request):

    if request.method == 'POST':
        form = ArticleForm(request.POST)

        if form.is_valid:
            artice = form.save()
            return redirect('article:index')

        else:
            context = {
                'form':form
            }
        return render(request, 'create.html', context)

    else:
        form = ArticleForm()

        context = {
            'form':form
        }

        return render(request, 'create.html', context)