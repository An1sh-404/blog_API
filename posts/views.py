from django.contrib.auth import get_user_model
#from rest_framework import generics # new
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly # new

# Create your views here.

# class PostList(generics.ListCreateAPIView):
#     permission_classes = (IsAuthorOrReadOnly,) # permisssion_Classes consists of instance of 
#     # of IsAuthorOrReadyOnly class to which only has_object method/func is only called and handles get and post
#     # and only when user is authenticated returns true or else false 
#     # post request only ListModelMixin → Handles GET requests (listing objects)
#     # CreateModelMixin → Handles POST requests (creating objects)
#     # GenericAPIView → Provides .queryset, .serializer_class, and request handling
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthorOrReadOnly,) # new
#     # permission_classes = (permissions.IsAdminUser,) # new
    
#     # DRF expects permission_classes to be an iterable (like a list or tuple) so you can write:
#     # permission_classes = (IsAuthenticated, IsAdminUser)
    
#     # this however deals with get,put,delete, . First always has_permission is called since object if not created hence
#     # then if object exisits and user requesting get,put or delete then has_object_permission is called
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class UserList(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer



# Using VIEWSETS
class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
