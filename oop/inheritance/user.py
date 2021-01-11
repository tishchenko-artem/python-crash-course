class User():

    def __init__(self, first_name, last_name, user_age, user_email):
        self.first_name = first_name
        self.last_name = last_name
        self.user_age = user_age
        self.user_email = user_email

    def describe_user(self):
        print('User first name: ' + self.first_name.title() + '\nUser last name: ' + self.last_name.title() +
              '\nUser age: ' + self.user_age + '\nUser e-mail: ' + self.user_email)

    def greet_user(self):
        print('Hello, ' + self.first_name.title() + ' ' + self.last_name.title())


class Privileges():
    def __init__(self, privileges=['allowed to ban users', 'allowed to delete users']):
        self.privileges = privileges

    def show_privileges(self):
        print('The admin has the following privileges:')
        for privilege in self.privileges:
            print(privilege)


class Admin(User):

    def __init__(self, first_name, last_name, user_age, user_email):
        super().__init__(first_name, last_name, user_age, user_email, )
        self.privileges = Privileges()


adm = Admin('Artem', 'Tishchenko', '20', 'artem@gmail.com')
adm.privileges.show_privileges()

# user1 = User('Artem', 'tishchenko', '20', 'artem@gmail.com')
# user2 = User('Lilia', 'sheremet', '21', 'lilia@gmail.com')

# print(user1.describe_user())
# print(user1.greet_user())

# print(user2.describe_user())
# print(user2.greet_user())
