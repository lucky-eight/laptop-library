class Address:
    def __init__(self, line_1, city, post_code):
        self.line_1 = line_1
        self.city = city
        self.post_code = post_code


class User:
    def __init__(self, first_name, last_name, email_address, date_requested, address):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.date_requested = date_requested
        self.address = address

class Laptop:
    def __init__(self, id, name, location, is_available):
        self.id = id
        self.name = name
        self.location = location
        self.is_available = is_available