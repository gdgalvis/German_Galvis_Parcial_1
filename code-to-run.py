from library import Librarian,User,Library

Alexandria= Library()
#Bibliotecario
librarian= Librarian(name= "Aurelio",library=Alexandria)
book_of_the_months=["Omerta","El Ultimo Don","El Siciliano","I Heard you paint Houses"]
print("Bienvendio Bibliotecario: ", librarian.name)
librarian.upload(list= book_of_the_months)
librarian.delete(book="I Heard you paint Houses")
librarian.add( book="El Padrino")
#Usuario
user1=User(name="Cesar",library=librarian.lib)
print("Bienvenido ",user1.name)
user1.view_books()
user1.borrow("Padrino")
user1.borrow("El Padrino")
user1.view_mybooks()
user1.dreturn("Padrino")
user1.dreturn("El Padrino")