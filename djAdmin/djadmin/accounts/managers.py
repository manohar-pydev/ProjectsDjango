from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    
    def create_user(self, phone_number, password=None,**extra_fields):
        if not phone_number:
            raise ValueError("Phone Number is required")
        
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("superuser must have is_super= True")
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError("staff user must have is_staff= True")
        
        if extra_fields.get('is_active') is not True:
            raise ValueError("active user must have is_active= True")

        return self.create_user(phone_number, password, **extra_fields)
        
        