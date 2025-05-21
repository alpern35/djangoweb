from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Post

@shared_task
def send_new_post_email(post_id):
    post = Post.objects.get(pk=post_id)
    send_mail(
        f"New post: {post.title}",
        post.content,
        settings.DEFAULT_FROM_EMAIL,
        [email for _, email in settings.ADMINS]
    )
