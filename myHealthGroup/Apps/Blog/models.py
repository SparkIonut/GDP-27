from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
	User = models.ForeignKey(User)
	Title = models.CharField(max_length = 100)
	Description = models.TextField()
	Posted_Date = models.DateTimeField(default=timezone.now())

	categories = ((0, 'General Health'),
				  (1, 'Rare Diseases'),
				  (2, 'Supervision'),
				  (3, 'Other'))
	Category = models.PositiveSmallIntegerField(choices=categories,default=0)
	
	def __int__(self):
		return self.Post.Title

	def isLiked(self, userID):
		isLiked = 'Like';
		if (Like.objects.filter(User__pk = userID, Post = self).count() > 0):
			isLiked = 'Dislike';

		return isLiked

	def like(self, userID):
		like = Like()
		like.User = User.objects.filter(pk = userID)[0]
		like.Post = self
		like.save()
	
	def dislike(self, userID):
		Like.objects.filter(User = User.objects.filter(pk = userID)[0], Post = self).delete()


class Like(models.Model):
	User = models.ForeignKey(User)
	Post = models.ForeignKey('Post')
	unique_togheter = (("User", "Post"))

	def __str__(self):
		return str(self.User.username) + " - " + self.Post.Title

class Comment(models.Model):
	Author = models.ForeignKey(User)
	Post = models.ForeignKey('Post',related_name='comments')
	Comment = models.TextField()
	Parent_Comment = models.ForeignKey('Comment')
	Created_Date = models.DateTimeField(default=timezone.now)

class Video(models.Model):
	Post = models.ForeignKey('Post')

class Image(models.Model):
	Post = models.ForeignKey('Post')