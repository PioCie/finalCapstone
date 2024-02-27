class Email:
    has_been_read = False

    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    def mark_as_read(self):
        if not self.has_been_read:
            self.has_been_read = True
        else:
            print("The email has already been read")


def populate_inbox():
    # Sample emails
    email1 = Email("sender1@example.com", "Welcome to HyperionDev!", "Thank you for joining.")
    email2 = Email("sender2@example.com", "Great work on the bootcamp!", "Your efforts are commendable.")
    email3 = Email("sender3@example.com", "Your excellent marks!", "Congratulations on your achievements.")

    # Add sample emails to the inbox
    inbox = [email1, email2, email3]
    return inbox


def list_emails(inbox):
    # Print list of emails with numbers
    print("Inbox:")
    for i, email in enumerate(inbox):
        print(f"{i} {email.subject_line}")


def read_email(inbox, index):
    if 0 <= index < len(inbox):
        selected_email = inbox[index]
        print(f"\nEmail from {selected_email.email_address} with subject '{selected_email.subject_line}':")
        print(f"Content: {selected_email.email_content}\n")

        # Mark the selected email as read
        selected_email.mark_as_read()
    else:
        print("Invalid index. Please provide a valid index.")


# Created a welcome logo
def create_welcome_frame(title):
    border = "#" * 50
    frame = f"\n{border}\n#{' ' * 48}#\n#{title.center(48)}#\n#{' ' * 48}#\n{border}"
    print(frame)


# Main application logic
def main():
    create_welcome_frame("Welcome to Jmail")
    inbox = populate_inbox()

    while True:
        print("\nMenu:")
        print("1. Read an email")
        print("2. View unread email subjects")
        print("3. Quit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            list_emails(inbox)
            index = int(input("Enter the index of the email you want to read: "))
            read_email(inbox, index)
        elif choice == '2':
            unread_subjects = [email.subject_line for email in inbox if not email.has_been_read]
            if unread_subjects:
                print("\nUnread Email Subjects:")
                for subject in unread_subjects:
                    print(subject)
            else:
                print("\nNo unread emails.")
        elif choice == '3':
            print("Quitting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()