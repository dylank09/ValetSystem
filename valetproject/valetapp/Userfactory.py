from .models.users.membershiptype import MembershipType
from .models.users.staff import Staff
from .models.users.customer import Customer


class Userfactory():

    def createuser(self, form, user):
        email = form.cleaned_data.get('email')
        if "@valetsystem.ie" in email:
            newuser = Staff(user=user)
        else:
            newuser = Customer(user=user)
            colour = form.cleaned_data.get('colours')
            membership_type_id = colour.index(')') - 1

            membership_type_id = colour[membership_type_id]
            colours = MembershipType.objects.filter(pk=membership_type_id)[0]

            newuser.set_colour(colours)
            print(newuser)
        newuser.save()
        return newuser
