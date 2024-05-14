# SOLID com Python

## Introdução
SOLID é um acrônimo que representa cinco princípios de design de software destinados a facilitar a manutenção e a escalabilidade de sistemas. Originalmente propostos por Robert C. Martin, esses princípios são amplamente aplicados no desenvolvimento orientado a objetos (OO). Neste README, exploraremos cada um desses princípios no contexto da linguagem Python.

## Princípios SOLID

### 1. Single Responsibility Principle (SRP)
**Princípio da Responsabilidade Única**

**Definição:** Uma classe deve ter um, e somente um, motivo para mudar. Em outras palavras, uma classe deve ter apenas uma responsabilidade ou tarefa.

**Exemplo:**
```python
class Process:
    def handle(self, username:str, password: str)->None:
        if self.__verify_input_data():
            self.__verify_input_in_database()
            self.__insert_new_user()

        else:
            self.__raise_error("Dados Invalid!")

    def __verify_input_data(self,username:str, password: str) -> bool:
        return isinstance(username,str) and isinstance(password, str)


    def __verify_input_in_database(self,username:str, password: str):
        print("Acessando o banco de dados...")
        print("verificando existencia do usuario")

    def __insert_new_user(self,username:str, password: str)->None:
        print("cadastro de usuarios realizado com sucesso!")

    def __raise_error(self,message:str)->None:
        raise Exception(message)
```

### 2. Open/Closed Principle (OCP)

**Princípio Aberto/Fechado**

**Definição:** As entidades de software (classes, módulos, funções, etc.) devem estar abertas para extensão, mas fechadas para modificação.

**exemplo**
```python
class Programmer:
    def make(self):
        print("Programmer creating code")

class Seller:
    def make(self):
        print("Seller selling the product")

class Human:
    def make(self):
        print("Human Resources hiring new devs")

# --------//---------//----------//---------
class Company:
    def do_work(self, worker:any)->None:
       worker.make()

```

### 3. Liskov Substitution Principle (LSP)

**Princípio da Substituição de Liskov**

**definição:** Subtipos devem ser substituíveis por seus tipos base sem alterar as propriedades desejáveis do programa.

**exemplo**
```python

class Animal:
    def comer(self):
        print("O animal esta comendo")

    def andar(self):
            print("O animal esta andando na jaula")


class Felino(Animal):
    def lamber(self):
        print("O felino esta lambendo seu pelo")


class Leao(Felino):
     def rugir(self):
          print("O leão esta rugindo")


class Pessoa:
     def observa(self, animal:Animal):
          animal.comer()

``` 

### 4. Interface Segregation Principle (ISP)
 

**Princípio da Segregação de Interfaces**

**definição:** Uma classe não deve ser forçada a implementar interfaces que não usa.

**exemplo**
```python

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

```

### 5. Dependency Inversion Principle (DIP)

**Princípio da Inversão de Dependência**

**definição:** Dependa de abstrações, não de implementações. Módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de abstrações.

**exemplo**

```python


from abc import ABC, abstractmethod

class NotificatorInterface(ABC):

    @abstractmethod
    def send_notification(self,message:str):
        pass



class NotificatorEmail(NotificatorInterface):
    
    def send_notification(self,message:str):
        print(f"sending Email: {message}")


class NotificatorSMS(NotificatorInterface):
    
    def send_notification(self,message:str):
        print(f"sending SMS: {message}")



class ClientService:
    def __init__(self,notfiicator:NotificatorInterface) -> None:
        self.notfiicator = notfiicator

    def send(self,message:str)->None:
        self.notfiicator.send_notification(message)

```

### Conclusão

**Os princípios SOLID são essenciais para escrever um código de qualidade, flexível e fácil de manter. Compreendê-los e aplicá-los no desenvolvimento em Python pode melhorar significativamente a estrutura e a robustez de seu software.**

