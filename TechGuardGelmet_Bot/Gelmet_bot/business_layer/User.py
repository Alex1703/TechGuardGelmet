# Capa de negocio (business_layer/user.py)
from business_layer.User import UserRepository

class User:
    def __init__(self):
        self.user_repository = UserRepository()

    def create_user(self, user_data):
        # Validar los datos del usuario si es necesario
        ...

        # Llamar al método insert_user de UserRepository
        self.user_repository.insert_user(user_data)
