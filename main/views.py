from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import *


class HomeView(View):
    def get(self, request):
        top = Article.objects.filter(top=True)
        articles_by_views = Article.objects.filter(top=False, published=True).order_by('-views')[:10]
        if top.exists():
            top = top.first()
        else:
            top = articles_by_views.first()
            articles_by_views = articles_by_views[1:]

        context = {
            'top': top,
            'articles_by_views': articles_by_views,
            'moments': Moment.objects.all().order_by('-datetime')[:10],
        }
        return render(request, 'home.html', context)

    def post(self, request):
        email = request.POST.get('email')
        if email is not None:
            Newsletter.objects.create(email=email)
            return redirect('thanks')
        return render(request, 'home.html')


class ArticleDetailView(View):
    def get(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        also_like_articles = Article.objects.filter(category=article.category)
        context = {
            'article': article,
            'articles': also_like_articles,
        }
        return render(request, 'detail-page.html', context)

    def post(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        Comment.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            text=request.POST.get('text'),
            article=article,
        )
        return redirect('article-details', slug=slug)


class ThanksView(View):
    def get(self, request):
        return render(request, 'thanks.html')


class ThanksContactView(View):
    def get(self, request):
        return render(request, 'thanks_for_contact.html')


class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        Contact.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone_number=request.POST.get('phone_number'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message'),
        )
        return redirect('thanks-for-contact')