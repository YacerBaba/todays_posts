from django.contrib.auth.models import User, Group


def save_user(first_name, last_name, email, password):
    user = User.objects.create_user(username=email, email=email,
                                    password=password, first_name=first_name, last_name=last_name)
    default = Group.objects.get(pk=1)
    default.user_set.add(user)
    return user
