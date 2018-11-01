from django.shortcuts import render
from .models import Test , TestNew
# Create your views here.


def test_view(request):
    ctx = {}
    all_test  = Test.objects.all()
    ctx['all_test']  = all_test
    return render(request, 'all_test.html' , ctx)
      
def test_new_view(request):
    ctx = {}
    all_test_new  = TestNew.objects.all()
    ctx['all_test_new']  = all_test_new
    return render(request, 'all_test_new.html' , ctx)
