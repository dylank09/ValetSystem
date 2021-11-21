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
            return item.get_price()
        if isinstance(item, Customer):
            return item.getEmail()
        if isinstance(item, ChainStore):
            name = item.get_name()
            return name
        if isinstance(item, Valet):
            name = item.get_name()
            return name
        if isinstance(item, MembershipType):
            return item.get_colour()
        if isinstance(item, Staff):
            return item.get_staff_email()
