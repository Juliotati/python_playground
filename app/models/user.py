
class UserProfile:
    user_id: int
    name: str
    email: str = ''

    def __init__(self, user_id: int, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email

    def copy_with(self, name: str = None, email: str = None):
        self.name = name or self.name
        self.email = email or self.email
        return self

    def to_string(self):
        return f'''
        user_id: {self.user_id}
        name: {self.name}
        email: {self.email}
        '''
