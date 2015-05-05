 #!/usr/bin/python
from gi.repository import Gtk
from contact import Contact
from contactsSerializer import ContactsSerializer

class Buglump:

    def on_windowMain_destroy(self, object, data=None):
        print "quit with cancel"
        Gtk.main_quit()

    def on_imagemenuitemQuit_activate(self, menuitem, data=None):
        print "quit from menu"
        Gtk.main_quit()

    def on_treeviewContacts_row_activated(self, object, path, data=None):
        pass

    def foreachContactMethod(self, treemodel, path, iter):
        print("contact selected: ", iter)

    def on_treeview_selection_changed(self, object, data=None):
        object.selected_foreach(self.foreachContactMethod)
        self.window.show()

    def on_imagemenuitemAll_activate(self, object, data=None):
        pass

    def __init__(self):
        self.gladefile = "ContactBookGUI.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.gladefile)
        self.builder.connect_signals(self)
        self.window = self.builder.get_object("windowMain")
        self.window.show()

    def fillListStore(self, contacts):
        self.listStore = self.builder.get_object("liststoreContacts")
        print ("liststore: ", self.listStore)
        for contact in contacts:
            self.listStore.append(contact.getDataInArray())

if __name__ == "__main__":
    serializer = ContactsSerializer()
    contacts = []
    contacts.append(Contact("Roman", "1234567", "Roman Adress here"))
    contacts.append(Contact("Grisha", "9873451", "Grisha Adress here"))
    contacts.append(Contact("Andru", "7352531", "Andru Adress here"))
    serializer.serializeContacts(contacts)

    main = Buglump()

    main.fillListStore(contacts)

    Gtk.main()

