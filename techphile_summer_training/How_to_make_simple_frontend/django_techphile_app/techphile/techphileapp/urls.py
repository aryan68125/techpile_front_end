from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_page, name="login"),
    path("edu", views.edu, name="edu"),
    path("facebook_login", views.facebook_login, name="facebook_login"),
    path("bootstrap_demo_page", views.bootstrap_demo_page, name="bootstrap_demo_page"),
    path("bootstrap_demo_page_two", views.bootstrap_demo_page_two, name="bootstrap_demo_page_two"),
    path("bootstrap_demo_page_three", views.bootstrap_demo_page_three, name="bootstrap_demo_page_three"),
    path("bootstrap_demo_page_four", views.bootstrap_demo_page_four,name="bootstrap_demo_page_four"),
    path("bootstrap_demo_five", views.bootstrap_demo_five,name="bootstrap_demo_five"),
    path("bootstrap_demo_form", views.bootstrap_demo_form,name="bootstrap_demo_form"),
    path("bootstrap_demo_form_homework", views.bootstrap_demo_form_homework,name="bootstrap_demo_form_homework"),
    path("demo_javascript", views.demo_javascript,name="demo_javascript"),
    path("bootstrap_mobile_divison_demo", views.bootstrap_mobile_divison_demo,name="bootstrap_mobile_divison_demo"),
    path("bootstarp_modal_demo", views.bootstarp_modal_demo,name="bootstarp_modal_demo"),
    path("bootstrap_homework_registration_1", views.bootstrap_homework_registration_1,name="bootstrap_homework_registration_1"),
    path("bootstrap_homework_registration_2", views.bootstrap_homework_registration_2,name="bootstrap_homework_registration_2"),
    path("bootstrap_homework_registration_3", views.bootstrap_homework_registration_3,name="bootstrap_homework_registration_3"),
    path("bootstrap_homework_registration_4", views.bootstrap_homework_registration_4,name="bootstrap_homework_registration_4"),
    path("bootstrap_homework_registration_5", views.bootstrap_homework_registration_5,name="bootstrap_homework_registration_5"),
    path("bootstrap_homework_webpage", views.bootstrap_homework_webpage,name="bootstrap_homework_webpage"),

    path("bootstrap_demo_home_work_news_portal_1", views.bootstrap_demo_home_work_news_portal_1,name="bootstrap_demo_home_work_news_portal_1"),

    path("bootstrap_demo_home_work_news_portal_news_details", views.bootstrap_demo_home_work_news_portal_news_details,name="bootstrap_demo_home_work_news_portal_news_details"),
]
