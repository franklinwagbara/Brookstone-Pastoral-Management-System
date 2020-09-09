#from django.test import TestCase

# Create your tests here.

def func(**kwargs):
    for k in kwargs:
        print(kwargs[k])
    print("kwargs : ", kwargs)


func(FirtName="Franklin", LastName="Wagbara")