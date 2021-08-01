class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.follower = 0
        self.following = 0

    def follow(self, user):
        user.follower +=1
        self.following +=1


user1 = User(1, "aquib")
user2 = User(2, "haris")

user1.follow(user2)

print(user1.follower)
print(user1.following)
print(user2.follower)
print(user1.following)

