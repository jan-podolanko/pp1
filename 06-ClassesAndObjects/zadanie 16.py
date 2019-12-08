class ebook():
    def __init__(self):
        self.filename = r'C:\Users\Monster\Desktop\pp1\06-ClassesAndObjects\book.txt'
        self.book_list = []
        with open(self.filename, 'r') as book:
            for line in book:
                self.book_list.append(line)
        self.title = self.book_list[0]
        self.author = self.book_list[1]
        self.pages = int(self.book_list[2])
        self.current_page = 1
        self.open = False
    def open_book(self):
        self.open = True
    def next_page(self):
        if self.open: 
            if self.current_page <= self.pages and self.current_page >= 0:
                self.current_page += 1
            else:
                print("Can't go further")
        else:
            print("Can't turn page, the book is closed")
    def previous_page(self):
        if self.open:
            if self.current_page <= self.pages and self.current_page >= 0:
                self.current_page -= 1
            else:
                print("Can't go further")
        else:
            print("Can't turn page, the book is closed")
    def show_status(self):
        print(f'Title: {self.title.strip()}')
        print(f'Author: {self.author.strip()}')
        print(f'Number of pages: {self.pages}')
        print(f'Current page: {self.current_page}')

x = ebook()
x.next_page()
x.open_book()
x.next_page()
x.show_status()
x.next_page()
x.show_status()