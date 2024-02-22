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


class EmailSimulator:
    def __init__(self):
        self.inbox = []

    def populate_inbox(self):
        # Sample emails
        email1 = Email("sample1@gmail.com", "Car insurance", "The insurance will be renewed")
        email2 = Email("sample2@yahoo.co.uk", "Amazon parcel", "Your parcel is on its way")
        email3 = Email("sample3@icloud.com", "Application update", "Please see below the update on your application")

        # Add sample emails to the inbox
        self.inbox.extend([email1, email2, email3])

    def list_emails(self):
        # Print list of emails with numbers
        print("Inbox:")
        for i, email in enumerate(self.inbox):
            print(f"{i} {email.subject_line}")

    def read_email(self, index):
        if 0 <= index < len(self.inbox):
            selected_email = self.inbox[index]
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
    print(frame, "\n")


# Main application logic
def main():
    create_welcome_frame("Welcome to Jmail")
    email_simulator = EmailSimulator()
    email_simulator.populate_inbox()

    while True:
        print("\nMenu:\n")
        print("1. Read an email")
        print("2. View unread email subjects")
        print("3. Quit\n")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            email_simulator.list_emails()
            index = int(input("Enter the index of the email you want to read: "))
            email_simulator.read_email(index)
        elif choice == '2':
            unread_subjects = [email.subject_line for email in email_simulator.inbox if not email.has_been_read]
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


# Check whether the Python script is being run as the main program or if it is being imported as a module.
if __name__ == "__main__":
    main()
