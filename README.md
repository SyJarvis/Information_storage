`数据库文件导出ORM模型`
```shell
flask-sqlacodegen "mysql://root:mysql0220@127.0.0.1/bookmark_flask" --tables bookmarks --outfile "Bookmarks.py" --flask

```


/* (无需理会)删除具有外键约束的表 */
show create table tb_grade;
alter table tb_grade drop foreign key `tb_grade_ibfk_1`;
alter table tb_grade drop foreign key `tb_grade_ibfk_2`;


Redis文档p
http://redis.cn/clients.html


dates = get_excel_data("./jobs/21软件7班 早午晚检3.xlsx", 4, 1, 7, 36)
write_excel_data("./jobs/21软件7班早午晚检表9.xls", dates)