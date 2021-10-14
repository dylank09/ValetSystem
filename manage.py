from controllers.StoreController import StoreController
from models.Store.Store import Store
from views.StoreCreateView import StoreCreateView

def main():
    print("launched server")

if __name__ == "__main__":
    main()

def initializeStores():

    store = Store("First Store")
    storeView = StoreCreateView()
    c = StoreController(store, storeView)
    c.showName()

    # stores = pd.read_csv("stores.csv")

    # for store in stores:
        # store = Store(name)
        # c = StoreController(store, StoreCreateView())
