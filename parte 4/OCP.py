class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje

    def notificar(self):
        raise NotImplementedError

class NotificadorEmail(Notificador):
    def Notificar(self):
        print(f"Enviando mensaje por EMIAL a {self.usuario.email}")

class NotificadorSMS(Notificador):
    def Notificar(self):
        print(f"Enviando mensaje por SMS a {self.usuario.sms}")

class NotificadorWhastapp(Notificador):
    def Notificar(self):
        print(f"Enviando Whastapp a {self.usuario.whastapp}")

class NotificadorTwitter(Notificador):
    def Notificar(self):
        print(f"Enviando Tweet a {self.usuario.twitter}")