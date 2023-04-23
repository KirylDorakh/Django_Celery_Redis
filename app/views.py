from django.shortcuts import render
import logging

from .task import text
from .models import Post

logger = logging.getLogger(__name__)


def index(request):
    logger.info('INFO')
    text.delay()
    return render(request, 'index.html')


# need to check
def posts(requset):
    try:
        posts = Post.objects.all()
    except Exception as E:
        logger.error(E)
    return render(requset, 'home.html', context={"posts": posts})
