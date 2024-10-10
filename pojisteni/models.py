from django.db import models
from django.contrib.auth.models import User

class Insured(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=25, default='')
    
    def __str__(self):
        return "Name: {0} | Address: {1} | Email: {2} | Phone: {3}".format(self.name, self.address, self.email, self.phone)
    
    class Meta:
        verbose_name = "Pojištěné osoby"
        verbose_name_plural = "Pojištěné osoby"


class Insurance(models.Model):
    insured_person = models.ForeignKey(Insured, on_delete=models.CASCADE, related_name='insurances')
    policy_type = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Insured person: {self.insured_person} | Policy type: {self.policy_type}"

    class Meta:
        verbose_name = "Pojištění"
        verbose_name_plural = "Pojištění"
    
class InsuranceEvent(models.Model):
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE)
    event_date = models.DateField()
    description = models.TextField()   
    
    def __str__(self):
        return "Insurance: {0} | Event date: {1}".format(self.insurance, self.event_date)   
    
    class Meta:
        verbose_name = "Pojistné události" 
        verbose_name_plural = "Pojistné události"


class UserRole(models.Model):
    ADMIN = 'admin'
    AGENT = 'agent'
    INSURED = 'insured'

    USER_ROLE_CHOICES = [
        (ADMIN, 'Administrátor'),
        (AGENT, 'Pojistitel'),
        (INSURED, 'Pojištěnec'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=20,
        choices=USER_ROLE_CHOICES,
        default=INSURED,
    )

    class Meta:
        verbose_name = "Uživatelská role"
        verbose_name_plural = "Uživatelské role"

    def __str__(self):
        return f'{self.user.username} - {self.get_role_display()}'
    
class Statistics(models.Model):   
    
    class Meta:
        verbose_name = "Statistiky" 
        verbose_name_plural = "Statistiky"
    pass
