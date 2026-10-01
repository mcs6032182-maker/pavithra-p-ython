# Blog Management System
# Single Python File

posts = []
comments = []

post_id_counter = 1
comment_id_counter = 1


# -----------------------------
# CREATE POST
# -----------------------------
def create_post():
    global post_id_counter

    print("\n--- Create Blog Post ---")

    title = input("Enter title: ")
    content = input("Enter content: ")
    author = input("Enter author name: ")

    post = {
        "id": post_id_counter,
        "title": title,
        "content": content,
        "author": author
    }

    posts.append(post)
    post_id_counter += 1

    print("\nPost created successfully!")


# -----------------------------
# VIEW ALL POSTS
# -----------------------------
def view_posts():
    print("\n--- Blog Posts ---")

    if not posts:
        print("No posts available.")
        return

    for post in posts:
        print("\n" + "=" * 50)
        print("Post ID :", post["id"])
        print("Title   :", post["title"])
        print("Author  :", post["author"])
        print("Content :", post["content"])

        print("\nComments:")

        post_comments = [
            c for c in comments
            if c["post_id"] == post["id"]
            and c["status"] == "Approved"
        ]

        if not post_comments:
            print("No approved comments.")

        else:
            for comment in post_comments:
                print(
                    f"- {comment['name']}: "
                    f"{comment['text']}"
                )


# -----------------------------
# VIEW SINGLE POST
# -----------------------------
def view_post():
    print("\n--- View Post ---")

    try:
        post_id = int(input("Enter post ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    for post in posts:

        if post["id"] == post_id:

            print("\n" + "=" * 50)
            print("Title   :", post["title"])
            print("Author  :", post["author"])
            print("Content :", post["content"])

            print("\n--- Approved Comments ---")

            found = False

            for comment in comments:

                if (
                    comment["post_id"] == post_id
                    and comment["status"] == "Approved"
                ):
                    print(
                        f"{comment['name']}: "
                        f"{comment['text']}"
                    )
                    found = True

            if not found:
                print("No approved comments.")

            return

    print("Post not found.")


# -----------------------------
# EDIT POST
# -----------------------------
def edit_post():
    print("\n--- Edit Post ---")

    try:
        post_id = int(input("Enter post ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    for post in posts:

        if post["id"] == post_id:

            print("Leave blank to keep the existing value.")

            title = input(
                f"Title [{post['title']}]: "
            )

            content = input(
                f"Content [{post['content']}]: "
            )

            if title:
                post["title"] = title

            if content:
                post["content"] = content

            print("\nPost updated successfully!")
            return

    print("Post not found.")


# -----------------------------
# DELETE POST
# -----------------------------
def delete_post():
    print("\n--- Delete Post ---")

    try:
        post_id = int(input("Enter post ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    for post in posts:

        if post["id"] == post_id:

            posts.remove(post)

            # Delete comments belonging to this post
            global comments

            comments = [
                c for c in comments
                if c["post_id"] != post_id
            ]

            print("\nPost deleted successfully!")
            return

    print("Post not found.")


# -----------------------------
# ADD COMMENT
# -----------------------------
def add_comment():
    global comment_id_counter

    print("\n--- Add Comment ---")

    try:
        post_id = int(input("Enter post ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    post_exists = any(
        post["id"] == post_id
        for post in posts
    )

    if not post_exists:
        print("Post not found.")
        return

    name = input("Enter your name: ")
    text = input("Enter your comment: ")

    comment = {
        "id": comment_id_counter,
        "post_id": post_id,
        "name": name,
        "text": text,
        "status": "Pending"
    }

    comments.append(comment)
    comment_id_counter += 1

    print(
        "\nComment submitted successfully!"
    )
    print(
        "Your comment is waiting for admin approval."
    )


# -----------------------------
# ADMIN LOGIN
# -----------------------------
def admin_login():
    print("\n--- Admin Login ---")

    username = input("Username: ")
    password = input("Password: ")

    if username == "admin" and password == "admin123":
        print("\nLogin successful!")
        admin_menu()
    else:
        print("\nInvalid username or password.")


# -----------------------------
# ADMIN MODERATION
# -----------------------------
def moderate_comments():
    print("\n--- Comment Moderation ---")

    pending = [
        c for c in comments
        if c["status"] == "Pending"
    ]

    if not pending:
        print("No pending comments.")
        return

    for comment in pending:

        print("\n" + "-" * 50)

        print("Comment ID :", comment["id"])
        print("Post ID    :", comment["post_id"])
        print("Name       :", comment["name"])
        print("Comment    :", comment["text"])

        print("\n1. Approve")
        print("2. Reject")
        print("3. Skip")

        choice = input("Choose action: ")

        if choice == "1":
            comment["status"] = "Approved"
            print("Comment approved.")

        elif choice == "2":
            comment["status"] = "Rejected"
            print("Comment rejected.")

        else:
            print("Comment skipped.")


# -----------------------------
# VIEW ALL COMMENTS
# -----------------------------
def view_all_comments():
    print("\n--- All Comments ---")

    if not comments:
        print("No comments available.")
        return

    for comment in comments:

        print("\n" + "-" * 50)

        print("Comment ID :", comment["id"])
        print("Post ID    :", comment["post_id"])
        print("Name       :", comment["name"])
        print("Comment    :", comment["text"])
        print("Status     :", comment["status"])


# -----------------------------
# ADMIN MENU
# -----------------------------
def admin_menu():

    while True:

        print("\n")
        print("=" * 50)
        print("             ADMIN PANEL")
        print("=" * 50)

        print("1. View Posts")
        print("2. Edit Post")
        print("3. Delete Post")
        print("4. Moderate Comments")
        print("5. View All Comments")
        print("6. Logout")

        print("=" * 50)

        choice = input("Enter your choice: ")

        if choice == "1":
            view_posts()

        elif choice == "2":
            edit_post()

        elif choice == "3":
            delete_post()

        elif choice == "4":
            moderate_comments()

        elif choice == "5":
            view_all_comments()

        elif choice == "6":
            print("Admin logged out.")
            break

        else:
            print("Invalid choice.")


# -----------------------------
# MAIN MENU
# -----------------------------
def main():

    while True:

        print("\n")
        print("=" * 50)
        print("          BLOG MANAGEMENT SYSTEM")
        print("=" * 50)

        print("1. Create Post")
        print("2. View All Posts")
        print("3. View Single Post")
        print("4. Edit Post")
        print("5. Delete Post")
        print("6. Add Comment")
        print("7. Admin Login")
        print("8. Exit")

        print("=" * 50)

        choice = input("Enter your choice: ")

        if choice == "1":
            create_post()

        elif choice == "2":
            view_posts()

        elif choice == "3":
            view_post()

        elif choice == "4":
            edit_post()

        elif choice == "5":
            delete_post()

        elif choice == "6":
            add_comment()

        elif choice == "7":
            admin_login()

        elif choice == "8":
            print("\nThank you for using Blog Management System!")
            break

        else:
            print("\nInvalid choice. Please try again.")


# -----------------------------
# PROGRAM START
# -----------------------------
if __name__ == "__main__":
    main()

