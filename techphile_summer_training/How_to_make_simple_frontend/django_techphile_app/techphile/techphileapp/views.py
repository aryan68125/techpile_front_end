
from django.shortcuts import render, redirect
# pip: -r requirements.txt to install
def index(request):
    return render(request, 'home_page/index.html')

def login_page(request):
    return render(request, 'home_page/login.html')

def edu(request):
    return render(request, 'home_page/edu.html')

def facebook_login(request):
    return render(request, 'home_page/facebook_login.html')

def bootstrap_demo_page(request):
    return render(request, 'home_page/bootstrap_demo_one.html')

def bootstrap_demo_page_two(request):
    return render(request, 'home_page/bootstrap_demo_two.html')

def bootstrap_demo_page_three(request):
    return render(request, 'home_page/bootstrap_demo_page_three.html')

def bootstrap_demo_page_four(request):
    return render(request, 'home_page/bootstrap_demo_page_four.html')

def bootstrap_demo_five(request):
    return render(request, 'home_page/bootstrap_demo_five.html')

def bootstrap_demo_form(request):
    return render(request, 'home_page/bootstrap_demo_form.html')

def bootstrap_demo_form_homework(request):
    return render(request, 'home_page/bootstrap_demo_form_homework.html')

def demo_javascript(request):
    return render(request, 'home_page/demo_javascript.html')

def bootstrap_mobile_divison_demo(request):
    return render(request, 'home_page/bootstrap_mobile_divison_demo.html')

def bootstarp_modal_demo(request):
    return render(request, 'home_page/bootstarp_modal_demo.html')

def bootstrap_homework_registration_1(request):
    return render(request, 'home_page/bootstrap_homework_registration_1.html')

def bootstrap_homework_registration_2(request):
    return render(request, 'home_page/bootstrap_homework_registration_2.html')

def bootstrap_homework_registration_3(request):
    return render(request, 'home_page/bootstrap_homework_registration_3.html')

def bootstrap_homework_registration_4(request):
    return render(request, 'home_page/bootstrap_homework_registration_4.html')

def bootstrap_homework_registration_5(request):
    return render(request, 'home_page/bootstrap_homework_registration_5.html')

def bootstrap_homework_webpage(request):
    return render(request, 'home_page/bootstrap_homework_webpage.html')

def bootstrap_demo_home_work_news_portal_1(request):
    return render(request, 'home_page/bootstrap_demo_home_work_news_portal_1.html')

def bootstrap_demo_home_work_news_portal_news_details(request):
    return render(request, 'home_page/bootstrap_demo_home_work_news_portal_news_details.html')
