class Process:
    def handle(self, username:str, password: str)->None:
        if self.__verify_input_data():
            self.__verify_input_in_database()
            self.__insert_new_user()

        else:
            self.__raise_error("Dados Invalid!")
         


# poderia ser com classe também, o verdadeiro objetivo seria que para alterar algo não precise alterar outra coisa

    def __verify_input_data(self,username:str, password: str) -> bool:
        return isinstance(username,str) and isinstance(password, str)


    def __verify_input_in_database(self,username:str, password: str):
        print("Acessando o banco de dados...")
        print("verificando existencia do usuario")

    def __insert_new_user(self,username:str, password: str)->None:
        print("cadastro de usuarios realizado com sucesso!")

    def __raise_error(self,message:str)->None:
        raise Exception(message)

# ----- ANTES

# class Process:
#     def handle(self, username:str, password: str)->None
#         if isinstance(username,str) and isinstance(password, str):
#             print("Acessando o banco de dados...")
#             print("verificando existencia do usuario")
#             print("cadastro de usuarios realizado com sucesso!")

#         else:
#             raise Exception("Dados Invalidos!")
         