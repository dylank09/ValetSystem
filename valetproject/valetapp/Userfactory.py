from .models.users.staff import Staff
from .models.users.customer import Customer


class Userfactory():

    def createuser(self, form, user):
        email = form.cleaned_data.get('email')
        if "@valetsystem.ie" in email:
            newuser = Staff(user=user)
        else:
            newuser = Customer(user=user)
        newuser.save()
        return newuser
