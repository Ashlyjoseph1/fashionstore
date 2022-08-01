from django.shortcuts import render






from rest_framework.views import APIView
from rest_framework.response import Response
import datetime



# get,post,put,patch,delete
class HelloWorldView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"hello world"})


class GoodMorningView(APIView):
    def get(self,request,*args,**qwargs):
        return Response({"msg":"good morning"})


class GoodNightView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg:good night"})


class GreetingsView(APIView):
    def get(self,request,*args,**kwargs):
        c_date=datetime.datetime.now()
        c_hour=c_date.hour
        msg=""
        if c_hour<12:
            msg="good morning"
        elif(c_hour<18):
            msg = "good afternoon"
        elif (c_hour < 24):
            msg = "good night"
        return Response({"data":msg})



class AddnumberView(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        n1=request.data.get("num1")
        n2= request.data.get("num2")
        res=n1+n2
        return Response({"msg":res})


class SubstractionView(APIView):
    def post(self,request,*args,**kwargs):
        n1=request.data.get("num1")
        n2=request.data.get("num2")
        res=n1-n2
        return Response({"msg":res})

class CubeView(APIView):
    def post(self,request,*args,**kwargs):
        n=request.data.get("num")
        res=n**3
        return Response({"msg":res})

class FactorialView(APIView):
    def post(self,request,*args,**kwargs):
        n=request.data.get("num")
        fact=1
        for i in range(1,n+1):
            fact*=i
        return Response({"msg":fact})

class WordCountView(APIView):
    def post(self,request,*args,**kwargs):
        text=request.data.get("text")
        wc={}
        words=text.split(" ")
        for w in words:
            if w in wc:
                wc[w]+=1
            else:
                wc[w]=1
        return Response({"data":wc})









