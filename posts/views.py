from rest_framework import generics # new

from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly # new

# Create your views here.

class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,) # permisssion_Classes consists of instance of 
    # of IsAuthorOrReadyOnly class to which only has_object method/func is only called and handles get and post
    # and only when user is authenticated returns true or else false 
    # post request only ListModelMixin → Handles GET requests (listing objects)
    # CreateModelMixin → Handles POST requests (creating objects)
    # GenericAPIView → Provides .queryset, .serializer_class, and request handling
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,) # new
    # permission_classes = (permissions.IsAdminUser,) # new
    
    # DRF expects permission_classes to be an iterable (like a list or tuple) so you can write:
    # permission_classes = (IsAuthenticated, IsAdminUser)
    
    # this however deals with get,put,delete, . First always has_permission is called since object if not created hence
    # then if object exisits and user requesting get,put or delete then has_object_permission is called
    queryset = Post.objects.all()
    serializer_class = PostSerializer
