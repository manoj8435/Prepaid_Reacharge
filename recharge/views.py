from django.shortcuts import render
from rest_framework.response import Response
from recharge.models import *
from recharge.serializers import *
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.

class SignUpUserView(APIView):
    '''This api is use for signup email,name,phone_number and password'''
    def post(self,requst):
        serializer = UserSignUpSerializers(data=requst.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(serializer.data['password'])
            user.save()
            return Response({
                'status':"success",'data':serializer.data,
                'message':"account has been created successfully",
            },status=status.HTTP_201_CREATED)
        else:
            return Response({'status':serializer.errors})


class LoginUserView(APIView):
    '''This api is use for login with email and password'''
    def post(self,request):
        serializer = UserLoginSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            user = authenticate(email=email, password=password)

            if user is not None:
                refresh = RefreshToken.for_user(user)
                return Response({'status':"success",'refresh':str(refresh),"access":str(refresh.access_token),
                },status=status.HTTP_200_OK)

            else:
                return Response({'status':serializer.errors,"messages":"invalid credential"})


class ShowAllPlans(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    
    def get(self,request):
        queryset = Plan.objects.all()
        serializer = PlanSerializers(queryset,many=True)

        return Response({'status':"successs",'plans': serializer.data})



class RechargeView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """It is use for Recharge as your given mobile number if you have a valid token"""
        user = request.user
        mobile = request.data.get('mobile')
        plan = request.data.get('plan')
        operator = request.data.get('operator')
        circle = request.data.get("circle")

      
        try:
            plan_obj = Plan.objects.get(price = plan)
        except Exception as e:
            print(e)
            plan_obj = ""
       
        try:
            operator_obj = Operator.objects.get(operator_name=operator)
        except Exception as e:
            operator_obj = ""
        
        try:
            circle_obj = AreaCircle.objects.get(area_name = circle)
        except Exception as e:
            circle_obj = ""
            
        if mobile :
            recharge_obj = Recharge.objects.create(plan = plan_obj,mobile=mobile,operator=operator_obj,circle=circle_obj,user=user)
            recharge_obj.save()
            serializer = RechargeSerializer(recharge_obj)
            return Response({"success":"Recharge successfully","data":serializer.data})
        else:
             return Response("Somthing went wrong!")

