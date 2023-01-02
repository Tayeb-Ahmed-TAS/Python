# ----------
# ! Remove empty strings from the list of strings
# ? filter() function to remove None type from the list

list1 = [
    "Tony Stark",
    "Thor Odin son",
    "Captain Steve Rogers",
    "Vision",
    "",
    "Wanda Maximof",
    "Natasha Romanof",
    "Carol Danvers",
]

print(list(filter(None, list1)))
