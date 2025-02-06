from django.contrib.auth.models import User


def create_user_if_not_exist(
    username: str, password: str, email: str, is_admin: bool = False
) -> None:
    if not User.objects.filter(username=username).exists():
        user = User.objects.create_user(
            username=username, password=password, email=email
        )
        user.is_superuser = is_admin
        user.save()


# Create normal users
create_user_if_not_exist("user1", "password1", "user1@example.com")
create_user_if_not_exist("user2", "password2", "user2@example.com")
