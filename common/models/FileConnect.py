# coding: utf-8
from application import db



class FileConnect(db.Model):
    __tablename__ = 'file_connect'

    id = db.Column(db.Integer, primary_key=True, info='id')
    file_id = db.Column(db.ForeignKey('file_record.id'), index=True, info='文件id')
    cif_id = db.Column(db.ForeignKey('file_cat.id'), index=True, info='分类id')
    status = db.Column(db.Integer, info='状态 1启用 0弃用')
    created_time = db.Column(db.DateTime, info='创建时间')
    updated_time = db.Column(db.DateTime, info='更新时间')

    cif = db.relationship('FileCat', primaryjoin='FileConnect.cif_id == FileCat.id', backref='file_connects')
    file = db.relationship('FileRecord', primaryjoin='FileConnect.file_id == FileRecord.id', backref='file_connects')




