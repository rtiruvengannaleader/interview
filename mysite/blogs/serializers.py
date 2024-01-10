# import serializer from rest_framework
from rest_framework import serializers
 
# import model from models.py
from .models import Entry, Tags, Category
 


# Create a model serializer
class CatSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Category
        fields = ('cat_name', )


# Create a model serializer
class TagsSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Tags
        fields = ('tag_name', )




# Create a model serializer
class EntrySerializer(serializers.ModelSerializer):
    #category_name = serializers.CharField(read_only= True)
    cat_name = CatSerializer(many=True, read_only=True)
    tag_name = TagsSerializer(many=True, read_only=True)
    # specify model and fields
    class Meta:
        model = Entry
        fields = "__all__"


