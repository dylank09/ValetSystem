from abc import ABC

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
            return item.getPrice()
        if isinstance(item, Customer):
            return item.getEmail()
        if isinstance(item, ChainStore):
            name = item.getName()
            return name
        if isinstance(item, Valet):
            name = item.getName()
            return name
        if isinstance(item, MembershipType):
            return item.getColour()
        if isinstance(item, Staff):
            return item.getStaffEmail()
