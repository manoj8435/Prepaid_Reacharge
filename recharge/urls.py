from django.urls import path
from recharge.views import *

urlpatterns = [
    path("signup/", SignUpUserView.as_view(), name="signup-user"),
    path("login/", LoginUserView.as_view(), name="login-user"),
    path("getplans/", ShowAllPlans.as_view(), name="show-all-plans"),
    path("do/recharges/", RechargeView.as_view(), name="do-recharge")
]
