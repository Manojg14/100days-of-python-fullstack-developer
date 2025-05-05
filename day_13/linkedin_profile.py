class User:
    def __init__(self, user_id, user_name, email):
        self.user_id = user_id
        self.user_name = user_name
        self.email = email

    def display_user_info(self):
        print(f"User ID : {self.user_id}")
        print(f"Name    : {self.user_name}")
        print(f"Email   : {self.email}")


class LinkedinProfile(User):
    def __init__(self, user_id, user_name, email, headline=""):
        super().__init__(user_id, user_name, email)
        self.headline = headline
        self.posts = []

    def update_headline(self, new_headline):
        self.headline = new_headline
        print("Headline updated successfully.")

    def add_post(self, content):
        self.posts.append(content)
        print("Post added successfully.")

    def show_profile(self):
        self.display_user_info()
        print(f"Headline: {self.headline}")
        print("Posts:")
        if self.posts:
            for i, post in enumerate(self.posts, 1):
                print(f" {i}. {post}")
        else:
            print(" No posts yet.")

def function():
    print("Welcome to Linkedin Profile Page!...")
    user_id = input("Enter User ID: ")
    user_name = input("Enter Name: ")
    email = input("Enter Email: ")

    user = LinkedinProfile(user_id,user_name, email)

    while True:
        print("\n--- Menu ---")
        print("1. Show Profile")
        print("2. Update Headline")
        print("3. Add Post")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            user.show_profile()
        elif choice == '2':
            headline = input("Enter new headline: ")
            user.update_headline(headline)
        elif choice == '3':
            content = input("Write your post: ")
            user.add_post(content)
        elif choice == '4':
            print("Thank you for using LinkedIn!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    function()
