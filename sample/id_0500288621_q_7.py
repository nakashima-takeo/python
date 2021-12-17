import random
import math

#####################################
class Message():
    """ Define the message on the social network
    """
    msg_id = 0
    def __init__(self, user):
        self.mid = Message.msg_id
        Message.msg_id += 1
        self.user = user
        self.score = 0

#####################################
class User():
    """Define a user
    """
    user_id = 0
    def __init__(self, social_network):
        self.social_network = social_network

        self.uid = User.user_id
        User.user_id += 1

        self.taste = random.random(), random.random()

        self.satisfaction = 20

        self.display_info("created")

    def read(self, msg):
        self.display_info("reading message {}".format(msg.mid))
        if self.like(msg):
            msg.score += 1
            # 
            if self == msg.user:
                self.satisfaction -= 1
            else:
                self.satisfaction += msg.score
            self.display_info("liking message {}".format(msg.mid))
        else:
            self.satisfaction -= 1
            if self.satisfaction < 0:
                self.unregister()

    def like(self, msg):
        d = math.sqrt((self.taste[0] - msg.user.taste[0])**2
                    + (self.taste[1] - msg.user.taste[1])**2)
        return d < 0.33

    def post(self):
        msg = Message(self)
        self.display_info("posting message {}".format(msg.mid))
        return msg

    def unregister(self):
        self.display_info("asking to unregister")
        self.social_network.unregister_user(self)

    def display_info(self, txt):
        print("Step {} User {}: {}".format(self.social_network.step, self.uid, txt))

#####################################
class SocialNetwork():
    """Social network simulation
    Random creation of new user
    Random posting of messages by users
    Random reading of messages by users
    """
    def __init__(self, max_users, max_msgs):
        self.step = 0

        # Keep track of users and msgs
        self.max_users = max_users
        self.max_msgs = max_msgs
        self.users = []
        self.msgs = []

    def new_user_register(self):
        """ Create and register a new user with a probability of 0.1
        When called
        """
        if len(self.users) < self.max_users:
            if random.random() > 0.9:
                self.users.append(User(self))

    def user_posting(self):
        if len(self.msgs) < self.max_msgs:
            user = self.get_random_user()
            if user:
                if random.random() > 0.9:
                    self.msgs.append(user.post())

    def user_reading(self):
        user = self.get_random_user()
        msg = self.get_random_msg()
        if user and msg:
            if random.random() > 0.1:
                user.read(msg)

    def get_random_user(self):
        if len(self.users) > 0:
            i = random.randint(0, len(self.users)-1)
            return self.users[i]
        else:
            return None

    def get_random_msg(self):
        if len(self.msgs) > 0:
            i = random.randint(0, len(self.msgs)-1)
            return self.msgs[i]
        else:
            return None

    def unregister_user(self, user):
        self.users.remove(user)

    def report(self):
        print("Step {}: {} users {} msgs".format(self.step, len(self.users), len(self.msgs)))

    def run(self):
        try:
            while True:
                self.step += 1

                self.new_user_register()

                for i in range(10):
                    self.user_posting()
                    self.user_reading()

                if self.step % 10 == 0:
                    self.report()
                    dummy = input("Press [Enter] to step (Ctrl-C to quit)")

        except KeyboardInterrupt:
            print("\nStoping simulation")

def main():
    social_network = SocialNetwork(10, 100)
    social_network.run()

if __name__ == "__main__":
    main()