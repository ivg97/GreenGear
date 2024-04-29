from django.db import models


class Post(models.Model):
    """Model for table blog_posts"""
    title = models.CharField(
        max_length=200,
        verbose_name='Title',
    )
    text = models.TextField(
        verbose_name='Text',
        blank=True,
        null=True,
        max_length=5000
    )
    slug = models.SlugField()
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        verbose_name='Author',
        related_name='posts',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created at',
    )
    image = models.ImageField(
        upload_to='images/posts/%Y/',
        blank=True,
        null=True,
        verbose_name='Image',
    )
    category = models.ForeignKey(
        'blog.Category',
        on_delete=models.CASCADE,
        verbose_name='Category',
        related_name='posts',
        blank=True,
        null=True,
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Active',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created_at']
        db_table = 'blog_posts'


class Category(models.Model):
    """Model for table blog_categories"""
    title = models.CharField(
        max_length=200,
        verbose_name='Title',
    )
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']
        db_table = 'blog_categories'
