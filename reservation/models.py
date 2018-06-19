from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.



def user_path(instance, filename):
    from random import choice
    import string
    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr)
    extension = filename.split('.')[-1]
    return '{}/{}.{}'.format(instance.author.username, pid, extension)

# 회의실 예약
class Reservation (models.Model):

    FirstTIME = 0
    SecondTIME = 1
    ThirdTIME = 2
    ForthTIME = 3
    FifthTIME = 4
    SixthTIME = 5
    SevenTIME = 6
    EighthTIME = 7
    NinethTIME = 8 
    TenthTIME = 9 
    EleventhTIME = 10
    STATUS = (
            (FirstTIME, ("9:00 ~ 10:00")),
            (SecondTIME, ("10:00 ~ 11:00")),
            (ThirdTIME, ("11:00 ~ 12:00")),
            (ForthTIME, ("12:00 ~ 13:00")),
            (FifthTIME, ("13:00 ~ 14:00")),
            (SixthTIME, ("14:00 ~ 15:00")),
            (SevenTIME, ("15:00 ~ 16:00")),
            (EighthTIME, ("16:00 ~ 17:00")),
            (NinethTIME, ("17:00 ~ 18:00")),
            (TenthTIME, ("18:00 ~ 19:00")),
            (EleventhTIME, ("19:00 ~ 20:00")),
         )    
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length = 10)    
    major = models.CharField(max_length = 30)
    tel_num = models.CharField(max_length = 11)
    num_people = models.IntegerField()

    rend_date = models.DateTimeField()
    
    rend_time = models.SmallIntegerField( default = 0)
    return_time = models.SmallIntegerField( default = 0)
    
    room_number = models.SmallIntegerField(default = 0)
    
    reservation_accept = models.SmallIntegerField(default = 0)
    updated_date = models.DateTimeField(blank = True, null = True)

    class Meta:
        ordering = ['-updated_date']
    
    def publish(self):
        self.updated_date = timezone.now()
        self.save()


    def __int__(self):
        return self.room_number

