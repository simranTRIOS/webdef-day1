college={"name": "trios", "course":"computer program","year":2020}
print(college)

my_self={"height":6.1, "favorite sport":"vollyball", "belong to":"gurdaspur"}
print(my_self)
print(college['course'])
a=my_self.get('height')
print(a)
college["year"]="january"
my_self.update({"height":6.4})
print(len(college))
college.pop("name")
my_self.popitem()
del college["course"]