import imp
from django.urls import path
from basic_app import views
# from learning_templates.basic_app.views import relative

# Template Tagging
app_name = 'basic_app'

urlpatterns = [
    path('other1',views.other_1,name='other1'),
    path('other2',views.other_2,name='other2'),
    path('other3',views.other_3,name='other3'),
    path('relative',views.relative,name='relative'),
]