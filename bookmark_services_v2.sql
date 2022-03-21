




create table bookmarkform(
	id int unsigned primary key not null auto_increment comment 'id',
	folder_name varchar(100) not null comment '分类名',
	detail varchar(800) comment '详情',
	status tinyint(1) default 1 comment '状态 0 弃用 1 使用',
	user_id int unsigned unique comment '用户id',
	created_time datetime comment '新增时间',
	updated_time datetime comment '更新时间',
	foreign key(user_id) references user(id)
);


create table bookmark(
	id int unsigned primary key not null auto_increment comment 'id',
	url varchar(500) not null comment 'url',
	title varchar(512) comment '网址标题',
	detail varchar(1000) comment '详情',
	name varchar(20) comment '名称',
	comment varchar(800) comment '备注',
	tags varchar(300) comment '标签,逗号间隔',
	category_id int unsigned comment '分类id',
	user_id int unsigned comment '用户id',
	status tinyint(1) default 1 comment '是否删除',
	created_time datetime comment '新增时间',
	updated_time datetime comment '更新时间',
	foreign key(category_id) references bookmarkform(id),
	foreign key(user_id) references user(id)
);



/* 用户表 */
create table user(
	id int unsigned primary key not null auto_increment comment 'id',
	name varchar(50) not null comment '用户名',
	password varchar(50) not null comment '密码',
	sex enum('男', '女', '保密') comment '性别',
	salt varchar(10) comment '盐',
	avatar varchar(500) comment '头像',
	mobile varchar(11) comment '手机号码',
	email varchar(50) comment '邮箱',
	created_time datetime comment '新增时间',
	updated_time datetime comment '更新时间'
);

/* 访问记录表 */
create table access_record(
    id int unsigned primary key not null auto_increment comment 'id',
    user_id int unsigned not null comment '访问用户id',
    referer_url varchar(255) not null comment '当前访问的url',
    ip varchar(32) not null comment 'ip地址',
    access_time datetime comment '访问时间',
    status tinyint(1) comment '状态',
    foreign key(user_id) references user(id)
);


/* 登录记录表 */
create table login_record(
	id int unsigned primary key not null auto_increment comment 'id',
	user_id int unsigned comment '访问用户id',
	ip varchar(32) comment 'ip地址',
	address varchar(100) comment 'ip所在地址',
	access_time datetime comment '登录时间',
	status tinyint(1) comment '状态',
	foreign key(user_id) references user(id)
);