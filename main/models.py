from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    intro = models.TextField()
    image = models.ImageField(upload_to='articles/')
    read_time = models.DurationField(blank=True, null=True)
    views = models.PositiveIntegerField(default=0)
    comments = models.PositiveIntegerField(default=0)
    author = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    top = models.BooleanField(default=False)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            count = 1
            while Article.objects.filter(slug=slug).exists():
                slug = base_slug + str(count)
                count += 1
            self.slug = slug
        super().save(*args, **kwargs)


class Content(models.Model):
    text = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.text


class Comment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    text = models.TextField()
    published = models.BooleanField(default=False)
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True)

    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.email)


class Moment(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='moments/')
    author = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    connected = models.BooleanField(default=False)
    result = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}: {self.phone_number}"
