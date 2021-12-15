class User:
    next_user_id = 0
    def __init__(self, name):
        self.id = User.next_user_id
        User.next_user_id += 1

        self.name = name

        self.messages_list = []


    def posts(self, text):
        self.messages_list.append(Message(self, text))
        print("{} wrote message {}".format(self.to_string(), self.get_last_message().to_string()))

    def likes(self, message):
        print("{} liked message {}".format(self.to_string(), message.to_string()))
        message.adds_fan(self)
    
    def to_string(self):
        return "{} (id:{})".format(self.name, self.id)

    def get_last_message(self):
        return self.messages_list[-1]

class Message:
    next_message_id = 0
    def __init__(self, user, text):
        self.id = Message.next_message_id
        Message.next_message_id += 1

        self.text = text 
        self.author = user

        self.fans_list = []

    def adds_fan(self, user):
        self.fans_list.append(user)

    def to_string(self):
        return "'{}' (id:{})".format(self.text, self.id)

class SocialNetwork:
    def __init__(self):
        self.users_dict = {}

    def create_user(self, name):
        user = User(name)
        self.users_dict[user.id] = user
        print("Created user {}".format(user.to_string()))
        return user

def main():
    social_network = SocialNetwork()

    print("Create users:")


    john = social_network.create_user('John')
    paul = social_network.create_user('Paul')
    claire = social_network.create_user('claire')

    print()

    print("Users talk:")

    john.posts("Hi there!")
    paul.posts("Hi!")
    john.likes(paul.get_last_message())
    paul.posts("Anyone learning Python?")
    john.posts("I am learning it now")
    claire.posts("I am also learning it!")

    print()
    
    print("Current state:")

    for user_id, user in social_network.users_dict.items():
        print(user_id, user.to_string())
        for message in user.messages_list:
            print("\tMessage:", message.to_string())
            for fan in message.fans_list:
                print("\t\tliked by:", fan.to_string())
        print()



if __name__ == "__main__":
    main()



    
