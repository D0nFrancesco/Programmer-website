from django.db import models
import bcrypt

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password_hash = models.BinaryField()
    image = models.CharField(max_length=45)

    class Meta:
        db_table = "user"
    
    def __init__(self, username: str, email: str, password: str, image):
        """
        Create a new user object.
        To save the user to the database call the function User.save()
        """
        salt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(password, salt)
        super().__init__(username=username, email=email, password_hash=password_hash, image=image)

    def auth(self, password: str) -> bool:
        """
        Returns True if the password matches and False if the password doesn't match.
        """
        return bcrypt.checkpw(password, self.password_hash)



