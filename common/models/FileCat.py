# coding: utf-8
from application import db




class FileCat(db.Model):
    __tablename__ = 'file_cat'

    id = db.Column(db.Integer, primary_key=True, info='id')
    cifname = db.Column(db.String(20), info='分类名')
    detail = db.Column(db.String(200), info='详情')
    status = db.Column(db.Integer, info='状态 1启用 0弃用')
    created_time = db.Column(db.DateTime, info='创建时间')
    updated_time = db.Column(db.DateTime, info='更新时间')
