class UserNotFoundException(Exception):
    pass


class UserAuth:
    users = []
    def login(self, login, password):
        if login not in self.users:
            raise UserNotFoundException('')