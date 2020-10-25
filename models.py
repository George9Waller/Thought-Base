from peewee import *
from flask_login import UserMixin
from flask_bcrypt import generate_password_hash
import datetime

DATABASE = SqliteDatabase('moodboard.db')


class User(UserMixin, Model):
    """User Model"""
    id = PrimaryKeyField()
    UserName = CharField(unique=True)
    Email = CharField(unique=True)
    PasswordHash = CharField(max_length=100)
    UserType = IntegerField(default=0)

    class Meta:
        database = DATABASE
        order_by = ('UserID',)

    def get_boards(self):
        """returns all the boards with a user matching the supplied user, ordered by soonest first"""
        return Board.select().where(Board.User == self).order_by(Board.EventDate)

    @classmethod
    def create_user(cls, username, email, password, usertype=0):
        """class method to create new instance of user"""
        try:
            cls.create(
                UserName=username,
                Email=email,
                PasswordHash=generate_password_hash(password),
                UserType=usertype
            )
        except IntegrityError:
            raise ValueError("User already exists")


class Board(Model):
    """Board Model"""
    id = PrimaryKeyField()
    User = ForeignKeyField(User, related_name='boards')
    Name = CharField(max_length=30)
    VenueSize = CharField(default='Small')
    EventDate = DateField(default=datetime.date.today)
    Created = DateField(default=datetime.date.today)

    class Meta:
        database = DATABASE
        order_by = ('User',)

    def get_board(self):
        """returns the board matching the supplied id"""
        return Board.get(Board.id == self)

    def get_ideas(self):
        """returns all the ideas associated with the board"""
        try:
            return Idea.select().where(Idea.Board == self)
        except DoesNotExist:
            return None

    @classmethod
    def create_board(cls, user, name, venuesize='Small', eventdate=datetime.date.today):
        """class method to create a new board"""
        try:
            cls.create(
                User=user,
                Name=name,
                VenueSize=venuesize,
                EventDate=eventdate
            )
        except IntegrityError:
            raise ValueError('Invalid details')


class Idea(Model):
    """Idea Model"""
    id = PrimaryKeyField()
    Board = ForeignKeyField(Board, related_name='ideas')
    Name = CharField(max_length=30)
    Content = TextField()
    """tags"""
    Colour = CharField(max_length=7, default='black')
    FixtureType = CharField(max_length=20, default='')
    FixtureAngle = CharField(max_length=20, default='')
    Red = CharField(max_length=20, default='')
    Green = CharField(max_length=20, default='')
    Blue = CharField(max_length=20, default='')
    Yellow = CharField(max_length=20, default='')

    class Meta:
        database = DATABASE
        order_by = ('Board',)

    def get_idea(self):
        """returns the idea matching the supplied id"""
        return Idea.get(Idea.id == self)

    def get_owner(self):
        """returns User who owns the idea"""
        idea = Idea.get_idea(self)
        return idea.Board.User.id

    def get_boardid(self):
        """returns the id of the board it is on"""
        idea = Idea.get_idea(self)
        return idea.Board.id


def initialise():
    DATABASE.connect()
    DATABASE.drop_tables([Idea])
    DATABASE.create_tables([User, Board, Idea], safe=True)
    DATABASE.close()
