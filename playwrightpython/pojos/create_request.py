from playwrightpython.pojos.request import Address, User

address = Address(city="New York", state="NY", zip="10001")
user = User(name="John Doe", job="Software Developer", address=address, skills=["Python", "Java", "JavaScript"])

# Convert to dictionary
user_dict = user.to_dict()
print(user_dict)