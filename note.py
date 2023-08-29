class PostNode:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.next = None

class PostList:
    def __init__(self):
        self.head = None

    def add_post(self, title, content):
        new_post = PostNode(title, content)
        if not self.head:
            self.head = new_post
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_post

    def display_posts(self):
        current = self.head
        while current:
            print("Title:", current.title)
            print("Content:", current.content)
            print("---------------------")
            current = current.next

# Create a post list and add some posts
post_list = PostList()
post_list.add_post("Hello World", "This is my first post.")
post_list.add_post("Python Tips", "Here are some Python programming tips.")
post_list.add_post("Kivy Tutorial", "Learn how to create interactive apps with Kivy.")

# Display all posts
post_list.display_posts()
