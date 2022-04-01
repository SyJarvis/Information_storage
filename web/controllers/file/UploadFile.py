# -*- coding: UTF-8 -*-
# @Time     : 2022/3/17 8:38
# @Author   : Runke Zhong
# @Software : PyCharm


from flask import Blueprint, g, request, jsonify, render_template, send_from_directory
from application import root_path, db, app
from common.models.FileRecord import FileRecord
from common.libs.Helper import getCurrentDate, ops_render
import os, datetime
from common.libs.Helper import getFileSalt


route_file = Blueprint("file_page", __name__)


@route_file.route("/uploadfile", methods=["GET", "POST"])
def UploadFile():
    if request.method == "GET":

        return render_template("file/uploadfile.html")
    
    elif request.method == "POST":
        resp = {'code': 200, 'msg': 'OK', 'data': {}}
        req = request.files
        file = req.get("name")

        file_path = "/data/files/" + datetime.datetime.now().strftime("%Y%m%d")


        if not os.path.exists(root_path + file_path):
            os.mkdir("." + file_path)

        ext = file.filename.split(".")[-1]

        file_path = file_path + "/" + getFileSalt() + "." + ext
        with open(root_path + file_path, 'wb+') as f:
            f.write(file.read())

        file_record = FileRecord()
        file_record.filename = file.filename
        file_record.filepath = file_path
        file_record.ext = ext
        file_record.status = 1
        file_record.created_time = getCurrentDate()
        file_record.updated_time = getCurrentDate()

        db.session.add(file_record)
        db.session.commit()
        return jsonify(resp)


@route_file.route("/downloadfile", methods=['GET', 'POST'])
def DownloadFile():

    if request.method == "GET":
        resp_data = {}

        items = FileRecord.query.filter_by(status=1).all()

        resp_data['items'] = items
        return ops_render("file/downloadfile.html", resp_data)
    elif request.method == "POST":
        resp = {'code':200, 'msg':'OK', 'data':{}}

        return jsonify(resp)


