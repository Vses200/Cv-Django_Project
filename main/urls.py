from re import template
from unicodedata import name
from django.urls import path
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import views as auth_view
from . import views


app_name = "main"

urlpatterns = [
	path('', views.IndexView.as_view(), name="home"),
	path('contact/', views.ContactView.as_view(), name="contact"),
	path('portfolio/', views.PortfolioView.as_view(), name="portfolios"),
	path('portfolio/<slug:slug>', views.PortfolioDetailView.as_view(), name="portfolio"),
	path('blog/', views.BlogView.as_view(), name="blogs"),
	path('blog/<slug:slug>', views.BlogDetailView.as_view(), name="blog"),
	path('register/', views.RegisterView, name="register"),
	path('login/',views.login,name="login"),
	path('profile/',views.profileView,name="profile"),
	path('logout/',views.logout, name="logout"),
	path('editprofile/',views.editprofileView.as_view(),name="editprofile"),
	path('password/',views.PasswordsChangeView.as_view(template_name='main/change-password.html'),name="password"),
	path('changedp/',views.editDPView,name="changedp"),
	path('updateDP/',views.dpChangeView.as_view(),name="updateDP"),
	path('deletedp/',views.SetUserImageDefault,name="deletedp"),
	path('donate/',views.donate,name="donate"),
	path('adminpanel/',views.admin,name="adminpanel"),
	path('editsuperuser/',views.editprofileView.as_view(),name="editsuperuser"),
	path('editblog/',views.allBlogs,name="editblog"),
	path('allportfolios/',views.allportfolio,name="allportfolios"),
	path('allcertificates/',views.allcertificate,name="allcertificates"),
	path('allcontactprofiles/',views.allcontactprofile,name="allcontactprofiles"),
	path('allskills/',views.allskill,name="allskills"),
	path('alltestimonials/',views.alltestimonial,name="alltestimonials"),
	path('alluserprofiles/',views.alluserprofile,name="alluserprofiles"),
	path('allmedias/',views.allmedia,name="allmedias"),
	]