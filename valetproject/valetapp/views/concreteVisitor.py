from valetapp.models.users.membershiptype import MembershipType
from valetapp.models.users.staff import Staff
from .visitor import Visitor
from ..models.booking import Booking
from ..models.chainstore import ChainStore
from ..models.users.customer import Customer
from ..models.valet import Valet
from ..models.users.staff import Staff
from ..models.users.membershiptype import MembershipType


class ConcreteVisitor(Visitor):

    def visit(self, item):
        if isinstance(item, Booking):
            cost = item.getPrice()
            return cost
        if isinstance(item, Customer):
            email = item.getEmail()
            return email
        if isinstance(item, ChainStore):
            name = item.getName()
            return name
        if isinstance(item, Valet):
            name = item.getName()
            return name
        if isinstance(item, MembershipType):
            membershipType = item.getColour()
            return membershipType
        if isinstance(item, Staff):
            staffEmail = item.getStaffEmail()
            return staffEmail
