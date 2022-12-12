from rest_framework import serializers
from recharge.models  import *
import phonenumbers
from phonenumbers import carrier
from rest_framework.serializers import SerializerMethodField

## define here serializers class

class UserSignUpSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'name',
            'phone_number',
            'password',
        )

class UserLoginSerializers(serializers.ModelSerializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128)
    
    class Meta:
        model = User
        fields = (
            'email','password',
        )

class CategoryPlanSerializer(serializers.ModelSerializer):
    class Meta :
        model = CategoryPlan
        fields = ['category_name']


class PlanSerializers(serializers.ModelSerializer):
    plan_type = SerializerMethodField()
    class Meta:
        model = Plan
        fields = (
            "price",
            'validity',
            "validity_type",
            'data',
            'data_type',
            'description',
            'plan_type',
        )

    def get_plan_type(self,obj):
        data = obj.plan_type.category_name
        category = CategoryPlan.objects.get(category_name = data)
        serializer = CategoryPlanSerializer(category)
        return serializer.data


############ Resposible for Recharge #################

class RechargeSerializer(serializers.ModelSerializer):
    plan_details = serializers.SerializerMethodField("get_plan_detail")

    class Meta:
        model = Recharge
        fields = ["mobile", "user", "operator", "circle", "plan","recharge_date","plan_details"]

    def get_plan_detail(self, obj):
        data = Plan.objects.filter(price=obj.plan.price)
        serializer = PlanSerializers(data, many=True)
        return serializer.data

    def validate(self, attrs):
        mobile = attrs.get("mobile")
        operator = attrs.get("operator")
        if len(mobile) < 10 or len(mobile) > 10:
            raise serializers.ValidationError("Invailed mobile number, Please enter your 10 digit of mobile number")
        mobile = "+91" + mobile
        phoneNumber = phonenumbers.parse(mobile)
        print(phoneNumber)
        Carrier = carrier.name_for_number(phoneNumber, 'en')

        if str(Carrier) != str(operator):
            raise serializers.ValidationError("Please enter the valid operator!")
        return attrs