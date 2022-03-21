# coding: utf-8
from flask_sqlalchemy import SQLAlchemy

from application import db


class Bookmarkform(db.Model):
    __tablename__ = 'bookmarkform'

    id = db.Column(db.Integer, primary_key=True, info='id')
    folder_name = db.Column(db.String(100), nullable=False, info='分类名')
    detail = db.Column(db.String(800), info='详情')
    status = db.Column(db.Integer, server_default=db.FetchedValue(), info='状态 0 弃用 1 使用')
    user_id = db.Column(db.ForeignKey('user.id'), unique=True, info='用户id')
    created_time = db.Column(db.DateTime, info='新增时间')
    updated_time = db.Column(db.DateTime, info='更新时间')

    user = db.relationship('User', primaryjoin='Bookmarkform.user_id == User.id', backref='bookmarkforms')



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
