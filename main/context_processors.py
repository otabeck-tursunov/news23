from .models import *
from django.db.models import *


def categories(request):
    context = {
        'categories' : Category.objects.annotate(article_count=Count('article')).order_by('-article_count', 'name')
    }
    return context