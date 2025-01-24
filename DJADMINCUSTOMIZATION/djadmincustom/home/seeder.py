from .models import *
from faker import Faker
import random
from home.models import Customer, Orders

def handle():
    fake = Faker()
    #to clear existing data
    Customer.objects.all().delete()
    Orders.objects.all().delete()
    
    # To Generate Fake customers
    customers = []
    for _ in range(60):
        customer = Customer(
            first_name=fake.first_name(),
            last_name = fake.last_name(),
            email = fake.email(),
            phone_number = fake.phone_number(),
            address = fake.address(),
        )
        customer.save()
        customers.append(customer)
    
    statuses  = ['Pending','Processing','Shipped','Delivered','Cancelled']
    for _ in range(200):
        order = Orders(
            customer = random.choice(customers),
            order_date = fake.date_this_year(),
            total_amount = round(random.uniform(50.0,500.0),2),
            status = random.choice(statuses)
        )
        order.save()