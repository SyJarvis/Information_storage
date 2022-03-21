# coding: utf-8
from application import db


class FileRecord(db.Model):
    __tablename__ = 'file_record'

    id = db.Column(db.Integer, primary_key=True, info='id')
    filename = db.Column(db.String(20), info='文件名')
    filepath = db.Column(db.String(200), info='文件存储路径')
    detail = db.Column(db.String(300), info='详情')
    tags = db.Column(db.String(20), info='标签')
    ext = db.Column(db.String(10), info='后缀名')
    status = db.Column(db.Integer, info='状态 1启用 0弃用')
    created_time = db.Column(db.DateTime, info='创建时间')
    updated_time = db.Column(db.DateTime, info='更新时间')
