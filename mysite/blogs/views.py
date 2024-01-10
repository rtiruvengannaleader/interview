from django.shortcuts import render
from rest_framework import generics
from rest_framework import filters
# Create your views here.
from rest_framework import viewsets
from .serializers import EntrySerializer, TagsSerializer
from blogs.models import Entry, Tags, Category


class EntryViewSet(viewsets.ModelViewSet):
    # define queryset
    search_fields = ['tags__tag_name', 'category__cat_name']
    filter_backends = (filters.SearchFilter,)
    queryset = Entry.objects.all()
 
    # specify serializer to be used
    serializer_class = EntrySerializer



class CatViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Category.objects.all()
 
    # specify serializer to be used
    serializer_class = EntrySerializer


class TagsAPIView(generics.ListCreateAPIView):
    search_fields = ['tag_name']
    filter_backends = (filters.SearchFilter,)
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer