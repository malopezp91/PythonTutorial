import shelve

with shelve.open("books") as books:

    books = {"recipes": {"blt": ["bacon", "lettuce", "tomato", "bread"],
                         "beansOnToast": ["beans", "bread"],
                         "scrambledEggs": ["eggs", "butter", "milk"],
                         "soup": ["tin of soup"],
                         "pasta": ["pasta", "cheese"]},
             "maintenance": {"stuck": ["oil"],
                             "loose": ["gaffer tape"]}
             }

    print(books["recipes"]["soup"])
