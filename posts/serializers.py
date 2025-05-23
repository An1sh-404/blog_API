from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    # When DRF serializes a ForeignKey field, it shows the 
    # primary key (id) of the related object by default. 
    # so to fix this we can set author to :-
  #  author = serializers.StringRelatedField()
    
#     title = models.CharField(...) → Defines the actual field.

#     class Meta → Only gives config info, not defining fields.

# DRF doesn’t look inside Meta for field definitions.

# The DRF get_fields() method looks at:

#     Class attributes of the serializer.

#     Auto-generates fields based on Meta.model + Meta.fields.
    
    class Meta:

        fields = (
            "id",
            "author",
            "title",
            "body",
            "created_at",
        )
        read_only_fields = ['author',]
        model = Post


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ("id",
                  "username",
                  )