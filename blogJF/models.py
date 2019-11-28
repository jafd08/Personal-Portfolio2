from django.db import models
import django.utils

# 1. Create a Blog model
# title
# pub_date
# body
# image

# 2. add the blog app to the settings
# 3. Create a migration
# 4. Migrate
# 5. Add to the admin

class Blog(models.Model):  # this model.Model lest us create a class and save it on database
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField(default=django.utils.timezone.now)
    body = models.TextField()
    image = models.ImageField(upload_to='img/')

    def __str__(self):
        return self.title

    def summary(self):
        if len(self.body)>100:
            return self.body[:100]+'...'
        else:
            return self.body

    def pub_date_pretty(self):
        return self.pub_date.strftime(' %b %e %Y')
