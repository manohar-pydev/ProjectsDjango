from django.contrib import admin
from .models import Customer,Orders
from django import forms
# Register your models here.
#admin.site.register(Customer)
#admin.site.register(Orders)
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'address':forms.Textarea(attrs={'rows':30})
        }


class OrderInline(admin.TabularInline):
    model = Orders
    extra = 2
    
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    form = CustomerForm
    list_display = ("first_name",
                "last_name",
                "email",
                "phone_number",
                "address")
    search_fields = ('first_name','last_name','phone_number','email')
    inlines = [OrderInline]
    

@admin.register(Orders)   
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('customer','order_date','total_amount','status')
    search_fields = ['customer__first_name','customer__last_name']
    list_filter =('status',)
    autocomplete_fields =['customer']
    readonly_fields =('total_amount',)
    exclude =('order_date',)
    
    actions = ["mark_as_shipped",]
    
    def mark_as_shipped(self, request,queryset):
        queryset.update(status='Shipped')
    mark_as_shipped.short_description = "Mark selected orders as shipped"
        