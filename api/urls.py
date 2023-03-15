from django.urls import path
from .views.mango_views import Mangos, MangoDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword
from .views.profile_views import Profiles, ProfileDetail
from .views.link_views import Links, LinkDetail
from .views.theme_views import Themes, ThemeDetail

urlpatterns = [
  # Restful routing
  path('mangos/', Mangos.as_view(), name='mangos'),
  path('mangos/<int:pk>/', MangoDetail.as_view(), name='mango_detail'),
  path('sign-up/', SignUp.as_view(), name='sign-up'),
  path('sign-in/', SignIn.as_view(), name='sign-in'),
  path('sign-out/', SignOut.as_view(), name='sign-out'),
  path('change-pw/', ChangePassword.as_view(), name='change-pw'),
  path('profiles/', Profiles.as_view(), name='profiles'),
  path('profile/', ProfileDetail.as_view(), name='profile_detail'),
  path('links/', Links.as_view(), name='links'),
  path('links/<int:pk>', LinkDetail.as_view(), name='link_detail'),
  path('themes/', Themes.as_view(), name='themes'),
  path('theme/<int:pk>', ThemeDetail.as_view(), name='theme_detail')
]
