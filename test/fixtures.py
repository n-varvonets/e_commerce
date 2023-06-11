import pytest

@pytest.fixture
def create_admin_user(django_user_model):
    """
    :param django_user_model:
    :return:  admin_user
    """
    return django_user_model.objects.create_superuser("nick-admin", "a@a,com", "111111")