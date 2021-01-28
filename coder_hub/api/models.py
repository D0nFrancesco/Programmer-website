from django.db import models
from datetime import datetime as dt
import bcrypt


class User(models.Model):
    username = models.CharField(max_length=45, unique=True, blank=False)
    email = models.CharField(max_length=45, unique=True, blank=False)
    password_hash = models.BinaryField(blank=False)
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

    def __repr__(self) -> str:
        return f"<User {(self.id, self.username, self.email)}>"


class Tag(models.Model):
    name = models.CharField(max_length=45, unique=True, blank=False)

    def __repr__(self) -> str:
        return f"<Tag {(self.name)}>"


class Post(models.Model):
    title = models.CharField(max_length=45, blank=False)
    text = models.TextField(max_length=500)
    created = models.DateTimeField(blank=False)

    # relationships
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    # votes
    up_votes = models.ManyToManyField(User, related_name="up_voted_posts")
    down_votes = models.ManyToManyField(User, related_name="down_voted_posts")

    def __repr__(self) -> str:
        return f"<Post {(self.id, self.user.username, self.title, self.text[:10])}>"


class Comment(models.Model):
    text = models.TextField(max_length=500, blank=False)
    created = models.DateTimeField(blank=False)

    # relationships
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)

    # votes
    up_votes = models.ManyToManyField(User, related_name="up_voted_comments")
    down_votes = models.ManyToManyField(User, related_name="down_voted_comments")

    def __repr__(self) -> str:
        return f"<Post {(self.id, self.user.username, self.text[:10])}>"


class Project(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField(max_length=500)
    created = models.DateTimeField(blank=False)
    _updated = models.DateTimeField()

    # relationships
    users = models.ManyToManyField(User, related_name="projects")
    tags = models.ManyToManyField(Tag)

    # votes
    up_votes = models.ManyToManyField(User, related_name="up_voted_projects")
    down_votes = models.ManyToManyField(User, related_name="down_voted_projects")

    @property
    def updated(self):
        """
        Get value of field "__update" but if it is empty return the created date.
        """
        return self._updated if self._updated is not None else self.created

    def __repr__(self) -> str:
        return f"<Project {(self.id, self.name, self.description[:10])}>"


class Version(models.Model):
    database_version = models.CharField(max_length=45, blank=False)
    website_version = models.CharField(max_length=45, blank=False)

    def __repr__(self) -> str:
        return f"<Version db_version: {self.database_version}, website_version: {self.website_version}>"
