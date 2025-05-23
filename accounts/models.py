from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    
    name = models.CharField(max_length=100, blank= True,null=True)
    
    def __str__(self):
        return self.username
    # The default __str__ in AbstractUser is:

    # def __str__(self):
    #     return self.username


    # return self.name only raises error because for the superuser
    # we haven't set name and name = None as this name field is added later 
    # after having a superuser i.e admin

        #     1. Why is self.name becoming None even though users are created?

        #     You said you already have 2 users and you've given them name values.

        #     BUT → is it possible that some users were created before you added the name field in your CustomUser model?

        #         Maybe through createsuperuser or migration before you added name?

        #         In the database, older users may have name = NULL.

        # ➡️ In such cases:

        #     Django tries to call user.__str__(), which does return self.name.

        #     If for that user, self.name is NULL in the DB → it becomes Python's None.

        #     Hence __str__ returns None, which breaks Django admin with:

        #         __str__ returned non-string (type NoneType)



            