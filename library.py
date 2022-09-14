class Library:
    def __init__(self) -> None:
        '''
        Se crea la libreria donde estaran los libros
        books: Lista de libros en la biblioteca
        
        '''
        self.books=[]
        pass

class Librarian:
    def __init__(self,name:str,library: Library) -> None:
        '''
        Name: nombre del bibliotecario
        library: Que Libreria trabaja y por ende en que libros tiene acceso
        '''
        self.name=name
        self.lib=library
        
    def upload(self,list: list):
        '''
        Monta una lista de libros disponibles a la biblioteca
        '''
        self.lib.books=list
        print("AÑADIO LOS SIFUIENTES LIBROS:")
        print(*self.lib.books, sep = "\n")
        print("")
        
    def add(self,book: str):
        '''
        Añade un libro al Inventario de la biblioteca
        '''
        self.lib.books.append(book)
        print("AÑADIO EL LIBRO: ",book, "AL INVENTARIO")
        print("")
    
    def delete(self,book: str):
        '''
        Elimina un libro del Inventario de la biblioteca
        '''
        if book in self.lib.books:
            self.lib.books.remove(book)
            print("ELIMINO EL LIBRO: ",book, "DEL INVENTARIO")
            print("")
        else:
            print("El libro ",book," no esta en el inventario")

class User:
    def __init__(self,name:str, library: Library) -> None:
        '''
        Name: nombre del bibliotecario
        library: A que libreria fue
        mybooks: Su lista de libros que tiene prestado
        '''
        self.name=name
        self.lib=library
        self.mybooks=[]
        
    def view_books(self):
        '''
        Imprime los libros disponibles al usuario
        '''
        print("LIBROS DISPONIBLES:")
        print("")
        print(*self.lib.books, sep = "\n")
    
    def view_mybooks(self):
        '''
        Imprime los libros prestados al usuario
        '''
        print("LIBROS En su Posecion:")
        print("")
        print(*self.mybooks, sep = "\n")
        print("")
    
    def borrow(self,book: str):
        '''
        Permite al usuario pedir prestado un libro si esta disponible
        '''
        if book in self.lib.books:
            self.mybooks.append(book)
            print("Obtuviste el libro: ", book)
            print("")
        else:
            print("El libro ", book ," no esta disponible en el momento")

    def dreturn(self,book: str):
        '''
        Permite al usuario regresar un libro que tenga en su posecion
        '''
        if book in self.mybooks:
            self.mybooks.remove(book)
            print("Regresaste el libro: ", book)
            print("")
        else:
            print("El libro ",book," no esta en tu posecion")
            