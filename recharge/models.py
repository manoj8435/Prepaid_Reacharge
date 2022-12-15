from django.db import models
from django.core.exceptions import ValidationError
import re
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from recharge.managers import UserManager
# Create your models here.


class User(AbstractBaseUser,PermissionsMixin):
    def validateEmail(email):
        if len(email) > 6:
            if re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email) != None:
                return email
            else:
                raise ValidationError("Email entered is Incorrect.")
        raise ValidationError("Email is Incorrect")

    def validate_phone_number(value):
        if re.compile(r"\d{10}").match(value):
            return value
        else:
            raise ValidationError("Phone number entered is incorrect.")

    name = models.CharField(max_length=100,blank=True,null=True)
    email = models.EmailField(validators=[validateEmail],unique=True)
    phone_number = models.CharField(validators=[validate_phone_number], max_length=10, blank=True, null=True,)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "phone_number"]
    objects = UserManager()

    class Meta:
        ordering = ["-id"]
    
    def __str__(self):
        return f"{self.email}--{self.name}"

class Operator(models.Model):
    operator_name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return str(self.operator_name)

class AreaCircle(models.Model):
    area_name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return str(self.area_name)

class CategoryPlan(models.Model):
    category_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return str(self.category_name)

class Plan(models.Model):
    DATATYPE_CHOICES = (("MB", "MB"), ("GB", "GB"), ("MB/Day", "MB/Day"), ("GB/Day", "GB/Day"))
    VALIDITY_CHOICES = (("Days","Days"),)
    plan_type = models.ForeignKey(CategoryPlan, on_delete=models.CASCADE, related_name="category_plan_type")
    operator = models.ForeignKey(Operator,on_delete=models.CASCADE, related_name='operator_based_plan',default="----")
    price = models.PositiveIntegerField(unique=True)
    validity = models.PositiveIntegerField()
    validity_type = models.CharField(max_length=20,choices=VALIDITY_CHOICES)
    data = models.FloatField(max_length=5)
    data_type = models.CharField(choices=DATATYPE_CHOICES, max_length=30)
    
    description = models.TextField(max_length=250)

    def __str__(self):
        return str(self.price) + "--" + str(self.data) + "/" + self.data_type+"--"+(str(self.plan_type))
 

class Recharge(models.Model):
    def validate_mobile_number(mobile):
        if re.compile(r"\d{10}").match(mobile):
            return mobile
        else:
            raise ValidationError("Phone number entered is incorrect.")

    mobile = models.CharField(max_length=10,validators=[validate_mobile_number])
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field="email")
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE, to_field="operator_name")
    circle = models.ForeignKey(AreaCircle, on_delete=models.CASCADE, to_field="area_name")
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, to_field="price", related_name="plan_detail")
    recharge_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return str(self.mobile) + "--" + str(self.plan) + "--" + str(self.operator) + "--" + str(self.user.email)