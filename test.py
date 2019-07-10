ls=[
    {"name":"D","price":1},
    {"name":"D","price":2},
    {"name":"C","price":1},
    {"name":"C","price":2},
    {"name":"D","price":3}
]
for v in ls:
    if v['name'] == "C":
        ls.remove(v)
print(ls)