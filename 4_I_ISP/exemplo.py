# pdf, txt, excel

from abc import ABC, abstractmethod


# class Document(ABC):

#     @abstractmethod
#     def load(self): pass

#     @abstractmethod
#     def view(self): pass

#     @abstractmethod
#     def format(self): pass

#     @abstractmethod
#     def calculate(self): pass

# interface grande em pequena

class PDF(ABC):

    @abstractmethod
    def load(self):pass

    @abstractmethod
    def view(self):pass

class DocumentTXT(ABC):

    @abstractmethod
    def format(self):self

    @abstractmethod
    def load(self):pass
    