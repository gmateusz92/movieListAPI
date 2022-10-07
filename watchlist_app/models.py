from django.db import models

class StreamPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name

class WatchList(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=500)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name='watchlist', null=True) # realted_name = 'watchlist' musi byc watchlist w selializer
    active = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title







# class Movie(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.CharField(max_length=500)
#     active = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.name
