import pandas as pd


class InventoryFactory:
    def __init__(self, config, items):
        self.__config = config
        self.__engine = config.database_engine
        self.__items = items

    def add_to_inventory(self):
        inventory = []
        for item in self.__items:
            inventory_item = pd.DataFrame([{"name": item,
                                            "dateAdded": pd.to_datetime(dt.datetime.now()),
                                            "dateLeft": None}])
            inventory.append(inventory_item)

        inventory = pd.concat(inventory)
        return inventory

    def commit_inventory_to_database(self, inventory):
        try:
            inventory.to_sql("inventory", self.__engine.engine, if_exists="append", index=False)
        except Exception as e:
            print(f"Error: {e}")
