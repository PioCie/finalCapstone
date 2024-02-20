class Email:
    has_been_read = False

    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.inbox = []

    def marks_as_read(self):
        # Check the status of email
        if not self.has_been_read:
            self.has_been_read = True
        else:
            print("The email has already been read")

    def populate_inbox(self):
        # Sample emails
        sample_email_1 = Email("sample1@gmail.com", "Car insurance", "The insurance will be renewed")
        sample_email_2 = Email("sample2@yahoo.co.uk", "Amazon parcel", "Your parcel is on its way")
        sample_email_3 = Email("sample3@icloud.com", "Application update", "Please see below the update on your "
                                                                           "application")
        # Add sample emails to the inbox
        self.inbox.extend([sample_email_1, sample_email_2, sample_email_3])


# Creating an Email object
my_email = Email("myemail@example.com", "Test Subject", "This is a test email.")
my_email.populate_inbox()
for email in my_email.inbox:
    print(f"From: {email.email_address}\nSubject: {email.subject_line}\nContent: {email.email_content}\n")