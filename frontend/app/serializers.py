# create ArticleSerializer class
from rest_framework import serializers
from .models import Articles

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = "__all__"
        # read_only_fields = ('id','text','updated_at')
