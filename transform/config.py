target_columns_names = ["name", "id", "cuisine", "open1", "close1", "days1", "price", "rating", "location",
                        "description", "open2", "close2", "days2"]

config_sources = {
    "src1": {
        "columns_names": ["Restaurant name", "Restaurant ID", "Cuisine", "Opens", "Closes",
                          "Days Open", "Price", "Rating", "Location", "Description"],
        "src_dir": "sources/src1",
        "extensions": ["csv"]
    },
    "src2": {
        "columns_names": [],
        "src_dir": "sources/src2",
        "extensions": ["csv"]
    }
}
