from controllers.StoreController import StoreController
from models.Store.Store import Store
from views.StoreCreateView import StoreCreateView


name = input("Enter Store Name ")
store = Store(name)
c = StoreController(store, StoreCreateView())
c.showName()
