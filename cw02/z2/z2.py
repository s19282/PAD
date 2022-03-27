myMap = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': 2, 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
print(myMap)
sort = lambda map,by: sorted(map, key=lambda x:x.get(by),reverse=False)
print(sort(myMap,'color'))