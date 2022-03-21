# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


from application import db



class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, info='id')
    name = db.Column(db.String(50), nullable=False, info='用户名')
    password = db.Column(db.String(50), nullable=False, info='密码')
    sex = db.Column(db.Enum('男', '女', '保密'), info='性别')
    salt = db.Column(db.String(10), info='盐')
    avatar = db.Column(db.String(500), info='头像')
    mobile = db.Column(db.String(11), info='手机号码')
    email = db.Column(db.String(50), info='邮箱')
    created_time = db.Column(db.DateTime, info='新增时间')
    updated_time = db.Column(db.DateTime, info='更新时间')


