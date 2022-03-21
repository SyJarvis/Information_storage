# coding: utf-8
from flask_sqlalchemy import SQLAlchemy

from application import db



class LoginRecord(db.Model):
    __tablename__ = 'login_record'

    id = db.Column(db.Integer, primary_key=True, info='id')
    user_id = db.Column(db.ForeignKey('user.id'), index=True, info='访问用户id')
    ip = db.Column(db.String(32), info='ip地址')
    address = db.Column(db.String(100), info='ip所在地址')
    access_time = db.Column(db.DateTime, info='登录时间')
    status = db.Column(db.Integer, info='状态')
    user = db.relationship('User', primaryjoin='LoginRecord.user_id == User.id', backref='login_records')




