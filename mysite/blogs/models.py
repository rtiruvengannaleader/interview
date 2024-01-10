from django.db import models



class Tags(models.Model):
  tag_name = models.CharField(max_length=255)

  def __str__(self):
        return str(self.tag_name)
  



class Category(models.Model):
  cat_name = models.CharField(max_length=255)

  def __str__(self):
        return str(self.cat_name)
  


class Entry(models.Model):
  blog_title = models.CharField(max_length=255)
  description = models.TextField()
  tags = models.ManyToManyField(Tags)
  category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name='items')

  def __str__(self):
        return self.blog_title