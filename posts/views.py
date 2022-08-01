from django.shortcuts import render

# Create your views here.


from rest_framework.views import APIView
from rest_framework.response import Response

from posts.models import users,blogs

# method:get
class PostView(APIView):

    def get(self,request,*args,**kwargs):
        if "Limit" in request.query_params:
            limit=int(request.query_params.get("Limit"))
            data=blogs[0:limit]
            return Response(data=data)

        if "Liked_by" in request.query_params:
             id=int(request.query_params.get("Liked_by"))
             liked_post=[blog for blog in blogs if id in blog["Liked_by"]]
             return Response(data=liked_post)
        else:
            return Response({"data":blogs})


    # {"postId": 9, "userId": 4, "title": "good morning", "content": "hey peepzz"}
    # method:post

    def post(self,request,*args,**kwargs):

        blog=request.data
        blogs.append(blog)
        return Response(data=blog)


# url: social/posts/{pid}
# method:get

class PostDetailsView(APIView):
    def get(self,request,*args,**kwargs):
        pid=kwargs.get("pid")
        blog=[ b for b in blogs if b["postId"]==pid].pop()
        return Response(data=blog)

    def delete(self,*args,**kwargs):
        id=kwargs.get("pid")
        blog=[b for b in blogs if b["postId"]==id].pop()
        blogs.remove(blog)
        return Response(data=blog)

    def put(self,request,*args,**kwargs):
        id = kwargs.get("pid")
        post= [p for p in blogs if p["postId"] == id].pop()
        post.update(request.data)
        return  Response(data=post)

# url:social/post/likes/,int:post_id>
# method:post
# data{"userid:1"}

class AddLikeView(APIView):
    def post(self,request,*args,**kwargs):
        post_id=kwargs.get("pid")
        blog= [p for p in blogs if p["postId"] ==post_id].pop()
        user=request.data.get("userId")
        blog["liked_by"].append(user)
        return Response(data=blog)








