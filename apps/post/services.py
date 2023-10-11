from apps.post.models import Post

manager = Post.objects


def get_posts_ordered_by_date():
    return manager.get_posts_ordered_by_date()


def get_post_by_id(post_id):
    return manager.get(pk=post_id)


def get_posts_by_user_id(user_id):
    return manager.get_posts_by_user_id(user_id)


def find_all():
    return manager.get_posts_ordered_by_date()
