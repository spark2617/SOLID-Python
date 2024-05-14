from notificator_interface import NotificatorInterface

class ClientService:
    def __init__(self,notfiicator:NotificatorInterface) -> None:
        self.notfiicator = notfiicator

    def send(self,message:str)->None:
        self.notfiicator.send_notification(message)