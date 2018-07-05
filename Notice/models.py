from django.conf import settings
from django.urls import reverse
from django.db import models
from django_summernote import models as summer_model
from django_summernote import fields as summer_fields


class Agora(summer_model.Attachment):
	author = models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	content = summer_fields.SummernoteTextField(default='')
	created_at = models.DateTimeField(auto_now_add=True, null=True)

	class Meta:
		ordering = ['-created_at']

	def get_absolute_url(self):
		return reverse('study:agora_detail', args=[self.id])

	def __str__(self):
		return self.title
	
def user_path(instance, filename):
    from random import choice
    import string
    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr)
    extension = filename.split('.')[-1]
    return '{}/{}.{}'.format(instance.author.username, pid, extension)
