class Email:
    has_been_read = False

    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.inbox = []

    def marks_as_read(self):
        if not self.has_been_read:
            self.has_been_read = True
        else:
            print("The email has already been read")

    def populate_inbox(self):
        sample_email_1 = Email("sample1@gmail.com", "Car insurance", "The insurance will be renewed")
        sample_email_2 = Email("sample2@yahoo.co.uk", "Amazon parcel", "Your parcel is on its way")
        sample_email_3 = Email("sample3@icloud.com", "Application update", "Please see below the update on your "
                                                                           "application")

