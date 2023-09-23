from django.urls import path, include
from .views import user_login, dashboard, registration, account_edit
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView


urlpatterns = [
    # path('login/', user_login, name='login'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # password change urls
    path('password-change/', PasswordChangeView.as_view(), name="password_change"),
    path('password-change/done/', PasswordChangeDoneView.as_view(), name="password_change_done"),

    #password reset urls
    path('password-reset/',PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password-reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('', include('django.contrib.auth.urls')),
    path('register/', registration, name="register"),
    path('edit/', account_edit, name='edit'),

    path('dashboard/', dashboard, name="dashboard"),
  
]