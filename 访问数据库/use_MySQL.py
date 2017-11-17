#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  PythonRepository
#  Created by xingl on 2017/11/9.
#  Filename: use_MySQL


import pymysql


# config = {
#     'host': '127.0.0.1',
#     'port': 3306,
#     'user': 'root',
#     'passwd': '123',
#     'charset':'utf8mb4',
#     'cursorclass':pymysql.cursors.DictCursor
#     }
# conn = pymysql.connect(**config)
# conn.autocommit(1)
# cursor = conn.cursor()
#
# try:
#     print("创建数据库成功---")
#     # 创建数据库
#     DB_NAME = 'test1'
#     cursor.execute('DROP DATABASE IF EXISTS %s' %DB_NAME)
#     cursor.execute('CREATE DATABASE IF NOT EXISTS %s' %DB_NAME)
#     conn.select_db(DB_NAME)
#
#     #创建表
#     TABLE_NAME = 'user'
#     cursor.execute('CREATE TABLE %s(id int primary key,name varchar(30))' %TABLE_NAME)
#
#     # 批量插入纪录
#     values = []
#     for i in range(20):
#         values.append((i,'kk'+str(i)))
#     cursor.executemany('INSERT INTO user values(%s,%s)',values)
#
#     # 查询数据条目
#     count = cursor.execute('SELECT * FROM %s' %TABLE_NAME)
#     print('total records:', cursor.rowcount)
#
#     # 获取表名信息
#     desc = cursor.description
#     print("%s %3s" % (desc[0][0], desc[1][0]))
#
#     cursor.scroll(10,mode='absolute')
#     results = cursor.fetchall()
#     for result in results:
#         print(result)
#
# except:
#     import traceback
#     traceback.print_exc()
#     # 发生错误时会滚
#     conn.rollback()
# finally:
#     # 关闭游标连接
#     cursor.close()
#     # 关闭数据库连接
#     conn.close()


# 打开数据库连接
db = pymysql.connect("localhost", "root", "123", "TESTDB")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# # 使用 execute() 方法执行 SQL，如果表存在则删除
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
#
# # 使用预处理语句创建表
# sql = """CREATE TABLE EMPLOYEE (
#          id int primary key,
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT,
#          SEX CHAR(1),
#          INCOME FLOAT )"""
#
# cursor.execute(sql)

try:
    print('-----')
    # 增
    # sql1 = "INSERT INTO EMPLOYEE( id, \
    #        FIRST_NAME, \
    #        LAST_NAME, AGE, SEX, INCOME) \
    #        VALUES ('%s', '%s', '%s', '%d', '%c', '%d' )" % \
    #      (2 ,'xingl', 'wang', 20, 'M', 3000)
    ## 执行sql语句
    # cursor.execute(sql1)
    # db.commit()  #对数据库有修改的时候要提交，查询的时候就不需要了


    # SQL 查询语句
    # sql1 = "SELECT * FROM EMPLOYEE \
    #        WHERE INCOME > '%d'" % (2000)
    #
    # # 执行sql语句
    # cursor.execute(sql1)
    # # 获取所有记录列表
    # results = cursor.fetchall()
    # print(results)
    # for row in results:
    #     fname = row[1]
    #     lname = row[2]
    #     age = row[3]
    #     sex = row[4]
    #     income = row[5]
    #     # 打印结果
    #     print("fname = %s,\nlname = %s,\nage = %d,\nsex = %s,\nincome = %d" % \
    #           (fname, lname, age, sex, income))

    # SQL 更新语句
    # sql1 = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
    # try:
    #     # 执行SQL语句
    #     cursor.execute(sql1)
    #     # 提交到数据库执行
    #     db.commit()
    # except:
    #     # 发生错误时回滚
    #     db.rollback()
    # SQL 删除语句
    sql1 = "DELETE FROM EMPLOYEE WHERE AGE < '%d'" % (25)
    try:
        # 执行SQL语句
        cursor.execute(sql1)
        # 提交修改
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()

finally:
    pass
# 关闭数据库连接
db.close()