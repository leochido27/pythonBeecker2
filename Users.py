from UserRoles import UserRole

class User(UserRole):
    # muestra el nombre
    def get_name(self,in_name):
        out_name = in_name
        return out_name
    # muestra el apellido
    def get_app(self,in_app):
        out_app = in_app
        return out_app
    # muestra la edad
    def get_edad(self,in_edad):
        out_edad = in_edad
        return out_edad
    
leo = User()
    
print(leo.get_name(in_name="leonardo"))