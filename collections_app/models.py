from django.db import models

class Customer(models.Model):
    """Stores customer information"""
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class CustomerTransaction(models.Model):
    """Stores customer transactions related to :model:`collections_app.Customer`"""
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='transactions')
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateField()

    def __str__(self):
        return f'{self.customer} - {self.transaction_amount}'

class CollectorNote(models.Model):
    """Stores notes related to :model:`collections_app.Customer`"""
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='notes')
    note = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer} - {self.note}'

class PaymentPlan(models.Model):
    """Stores payment plans related to :model:`collections_app.Customer`"""
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='payment_plans')
    payment_plan = models.CharField(max_length=255)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()

    def __str__(self):
        return f'{self.payment_plan} for {self.customer}'