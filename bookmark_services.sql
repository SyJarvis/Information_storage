

create table tag(
	id int unsigned primary key not null auto_increment comment 'id',
	name varchar(64) comment '标签名',
	is_delete tinyint(1) default 1 comment '是否删除',
	created_time datetime comment '新增时间',
	updated_time datetime comment '更新时间'
);


create table bookmarkform(
	id int unsigned primary key not null auto_increment comment 'id',
	folder_name varchar(100) not null comment '分类名',
	detail varchar(800) comment '描述详情',
	is_delete tinyint(1) default 1 comment '是否删除',
	user_id int unsigned unique comment '用户id',
	created_time datetime comment '新增时间',
	updated_time datetime comment '更新时间',
	foreign key(user_id) references user(id)
);


create table bookmarks(
	id int unsigned primary key not null auto_increment comment 'id',
	url varchar(500) not null comment 'url',
	title varchar(80) not null comment '标题',
	detail varchar(800) comment '描述详情',
	website_title varchar(512) comment '网址标题',
	website_detail varchar(1000) comment '详情',
	category_id int unsigned unique comment '分类id',
	user_id int unsigned unique comment '用户id',
	is_delete tinyint(1) default 1 comment '是否删除',
	created_time datetime comment '新增时间',
	updated_time datetime comment '更新时间',
	foreign key(category_id) references bookmarkform(id),
	foreign key(user_id) references user(id)
);

/* 标签与书签建立连接 */
create table tag_to_bookmark(
	id int unsigned primary key not null auto_increment comment 'id',
	tag_id int unsigned,
	bookmark_id int unsigned,
	created_time datetime comment '新增时间',
	updated_time datetime comment '更新时间'
);

/* 用户表 */
create table user(
	id int unsigned primary key not null auto_increment comment 'id',
	name varchar(50) not null comment '用户名',
	password varchar(50) not null comment '密码',
	sex enum('男', '女', '保密') comment '性别',
	salt varchar(10) comment '盐',
	avatar varchar(100) comment '头像',
	mobile varchar(20) comment '手机号码',
	email varchar(100) comment '邮箱',
	created_time datetime comment '新增时间',
	updated_time datetime comment '更新时间'
);

/* 访问记录表 */
create table access_record(
    id int unsigned primary key not null auto_increment comment 'id',
    user_id int unsigned not null comment '访问用户id',
    referer_url varchar(255) not null comment '当前访问的url',
    ip varchar(32) not null comment 'ip地址',
    access_time datetime comment '访问时间'
);