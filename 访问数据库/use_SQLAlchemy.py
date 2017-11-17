#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  Created by xingl on 2017/11/9.

# 第一步，导入SQLAlchemy，并初始化DBSession：

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类
Base = declarative_base()

# 定义User对象
class User(Base):
    # 表的名字
    __tablename__ = 'user'

    # 表的结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接：
# create_engine()用来初始化数据库连接。SQLAlchemy用一个字符串表示连接信息：
# '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+pymysql://root:123@localhost:3306/test')
# 创建DBSession类型
DBSession = sessionmaker(bind=engine)


# 由于有了ORM，我们向数据库表中添加一行记录，可以视为添加一个User对象：
# 创建session对象
# session = DBSession()
# 创建新User对象
# new_user = User(id=4, name='xingl')
# # 添加到session
# session.add(new_user)
# # 提交即保存到数据库
# session.commit()
# # 关闭session
# session.close()

# SQLAlchemy提供的查询接口
session = DBSession()
# 创建Query查询，filter是where条件，最后调用 one() 返回唯一行，如果调用 all() 则返回所有行
user = session.query(User).filter(User.id=='3').one()
# 打印类型和对象的name属性
print('type:', type(user))
print('name:', user.name)
# 关闭session
session.close()

