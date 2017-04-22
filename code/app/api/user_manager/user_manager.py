from flask import g, session
from app.extensions import db
from app.models.user import User, UserDetails
from app.models.role import RoleEnum, RoleFactory


class UserManager(object):

    @staticmethod
    def get_user(email):
        user = User.query.filter_by(email=email).first()
        return user

    @staticmethod
    def get_user_by_id(id):
        user = User.query.filter_by(id=id).first()
        return user

    @staticmethod
    def get_anonymous_user():
        '''
        Null design pattern
        '''
        user = User(None)
        user.role = RoleFactory.get_role(RoleEnum.ANONYMOUS)
        return user

    @staticmethod
    def create_user(email, password, role=RoleEnum.GUEST):
        if User.query.filter_by(email=email).first():
            return False

        user = User(email)
        user.password = password
        user.role = RoleFactory.get_role(role)
        db.session.add(user)
        db.session.commit()
        return True

    @staticmethod
    def update_details(user, first_name, last_name, contact_number):
        if user.details is None:
            user.details = UserDetails()
        user.details.first_name = first_name
        user.details.last_name = last_name
        user.details.contact_number = contact_number
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def create_staff(email, password, role):
        if User.query.filter_by(email=email).first():
            return False
        if role =='1':
            role = RoleEnum.GUEST
        elif role =='2':
            role = RoleEnum.ADMIN
        user = User(email)
        user.password = password
        user.role = RoleFactory.get_role(role)
        db.session.add(user)
        db.session.commit()
        return True
