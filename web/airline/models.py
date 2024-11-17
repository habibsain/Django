from django.db import models

# Create your models here.

class passenger(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

#     def __str__(self):
#         return self.name
    
# class airport(models.Model):
#     name = models.CharField(max_length=50)
#     city = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name
    
# class airline(models.Model):
#     name = models.CharField(max_length=50)
#     country = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name
    
    

# class reservation(models.Model):
#     passenger = models.ForeignKey(passenger, on_delete=models.CASCADE)
#     airline = models.ForeignKey(airline, on_delete=models.CASCADE)
#     date = models.DateField()

#     def __str__(self):
#         return self.passenger
    
# class flight(models.Model):
#     name = models.ForeignKey(airline, on_delete=models.CASCADE)
#     departure = models.ForeignKey(airport, on_delete=models.CASCADE)
#     arrival = models.ForeignKey(airport, on_delete=models.CASCADE)
#     passengers = models.ForeignKey(reservation, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name
