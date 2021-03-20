from django.db import models

# Create your models here.
class Members(models.Model):
    username=models.CharField(max_length=250)
    password=models.CharField(max_length=500)
    email=models.EmailField(max_length=250)



    def register(self):
        self.save()

    @staticmethod
    def get_member_by_email(email):
        try:
            return Members.objects.get(email=email)
        except:
            return False

    @staticmethod
    def get_member_by_uname(username):
        try:
            return Members.objects.get(username=username)
        except:
            return False

    def doExists(self):
        if Members.objects.filter(email=self.email):
            return True

        return False

    def validateEmail(self):
        email=self.email
        from django.core.validators import validate_email
        from django.core.exceptions import ValidationError
        try:
            validate_email(email)
            return True
        except ValidationError:
            return False

    def __str__(self):
        return self.username

class Trains(models.Model):
    tno=models.CharField(primary_key=True,max_length=50)
    tname=models.CharField(max_length=50)
    rid=models.ForeignKey('Route',on_delete=models.CASCADE)

    def __str__(self):
        return self.tno

class Route(models.Model):
    rid=models.CharField(max_length=50)
    ostation=models.CharField(max_length=50)
    dstation=models.CharField(max_length=50)
    def __str__(self):
        return self.rid
class Station(models.Model):
    sid=models.CharField(primary_key=True,max_length=50)
    sname=models.CharField(max_length=50)
    def __str__(self):
        return self.sid


class RouteStation(models.Model):
    tno=models.ForeignKey('Trains',on_delete=models.CASCADE)
    sid=models.ForeignKey('Station',on_delete=models.CASCADE)
    rid=models.ForeignKey('Route',on_delete=models.CASCADE)
    order=models.IntegerField()
    atime=models.CharField(max_length=50)

class Reservation(models.Model):
    tno=models.ForeignKey('Trains',on_delete=models.CASCADE)
    user=models.CharField(max_length=50)
    nos=models.IntegerField()
    date=models.CharField(max_length=50)
    amt=models.IntegerField()
    cls=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
    pnr=models.CharField(max_length=50)
    src=models.CharField(max_length=50)
    des=models.CharField(max_length=50)




class Payment(models.Model):
    pnr=models.CharField(max_length=50)
    user=models.CharField(max_length=50)
    amt=models.IntegerField()
    mtd=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
    cancel=models.CharField(max_length=50)




