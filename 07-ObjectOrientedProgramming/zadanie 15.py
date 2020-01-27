class Book():
    i = ''
    def __init__(self,title,author,genre):
        self.title = title
        self.author = author
        self.genre = genre
    def display(self):
        print(f'Title: {self.title}')
        print(f'Author: {self.author}')
        print(f'Genre: {self.genre}')
class Ebook(Book):
    def __init__(self,title,author,genre,file_name):
        super().__init__(title,author,genre)
        self.file_name = file_name
    def display(self):
        super().display()
        print(f'File name: {self.file_name}')
class Tbook(Book):
    def __init__(self,title,author,genre,length):
        super().__init__(title,author,genre)
        self.length = length
    def display(self):
        super().display()
        print(f'Length: {self.length}')

x = Ebook('Edgedancer','Brandon Sanderson','Fantasy','edgedancer.mobi')
x.display()
y = Tbook('Harry Potter and the Goblet of Fire','J.K.Rowling','Fantasy',636)
y.display()