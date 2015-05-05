__author__ = 'roman'

import pickle

class ContactsSerializer:
    def serializeContacts(self, contacts):
        with open('book.pickle', 'wb') as f:
	        pickle.dump(contacts, f)

    def deserializeContacts(self):
        with open('book.pickle', 'rb') as f:
	        return pickle.load(f)



