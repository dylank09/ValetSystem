from controllers.StoreController import StoreController
from controllers.CustomerController import CustomerController
from models.Store.Store import Store
from models.User.Customer import Customer
from models.membershipType.Membership import Membership
from views.StoreCreateView import StoreCreateView
from views.CustomerView import CustomerView


def initializeStores():

    # store = Store("First Store")
    # storeView = StoreCreateView()
    # c = StoreController(store, storeView)
    # c.showName()
    memberShipType = Membership("Red", 10)
    person1 = Customer("Arnas", "Juravicius", "arnas123",
                       "gmail", memberShipType)
    customerController = CustomerController(person1, CustomerView())
    customerController.getFirstName()
    customerController.getMembershipType()
    # stores = pd.read_csv("stores.csv")

    # for store in stores:
    # store = Store(name)
    # c = StoreController(store, StoreCreateView())


def main():
    print("launched server")
    initializeStores()


if __name__ == "__main__":
    main()
