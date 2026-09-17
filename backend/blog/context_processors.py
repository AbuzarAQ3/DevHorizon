from .models import Category, Socialaccounts

def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)

def get_socialaccounts(request):
    socialaccounts = Socialaccounts.objects.all()
    return dict(socialaccounts=socialaccounts)