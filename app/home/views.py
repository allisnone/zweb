# -*- coding:utf-8 -*-
#Author: allisnone

from . import home
from flask import render_template
from app.models import db

# -*- coding: utf-8 -*-
# Author: allisnone
#from flask import homeprint
from sqlalchemy import and_, not_, or_

from app.models import db, Student


@home.route('/')
def hello():
    return 'hello world'


@home.route('/create_db/')
def create_db():
    # 迁移模型
    # 第一次迁移模型时才有用
    db.create_all()
    # 删除表
    # db.drop_all()
    return '创建表成功'


@home.route('/add_stu/')
def add_stu():
    # 新增学生数据
    stu = Student()
    stu.s_name = '小蕊'
    stu.age = 20
    # 准备向数据库flask9中的student表中插入数据
    db.session.add(stu)
    # 提交操作
    db.session.commit()
    return '创建数据成功'


@home.route('/add_stus/')
def add_stus():
    # 批量插入内容
    stu_list = []
    for i in range(10):
        stu = Student()
        stu.s_name = '小李' + str(i)
        stu.age = int(i)
        stu_list.append(stu)
        # db.session.add(stu)
    db.session.add_all(stu_list)
    db.session.commit()
    return '批量插入数据成功'


@home.route('/sel_stu/')
def sel_stu():
    # select * from stu where s_name='小张0'
    # stu = Student.query.filter_by(s_name='小张0').all()[0]
    stu = Student.query.filter_by(s_name='小李0').first()
    print(stu.s_name)
    print(stu.age)
    return '查询数据成功'


@home.route('/del_stu/')
def del_stu():
    # 删除年龄等于0的信息
    stus = Student.query.filter_by(age=0).all()
    for stu in stus:
        db.session.delete(stu)
    db.session.commit()
    return '删除数据成功'


@home.route('/update_stu/')
def update_stu():
    # 修改，先获取需要修改的对象
    stu = Student.query.filter_by(s_name='小张1').first()
    stu.age = 10
    # db.session.add(对象)  可以不用写
    # db.session.add(stu)
    # db.session.commit()
    stu.save()
    return '修改数据成功'


@home.route('/sel_stus/')
def sel_stus():

    stu = Student.query.filter_by(s_name = '小张1').first()
    stu = Student.query.filter(Student.s_name == '小张1').first()
    print(stu)

    # 查询所有学生信息
    # all()结果为列表，列表中的元素为查询的学生对象
    stus = Student.query.all()
    print(stus)

    # 查询id=1的学生信息
    stu = Student.query.filter(Student.id == 1).first()
    print(stu)
    # get()： 查询主键所在行的信息，主键为id。查询不到数据，返回None
    stu = Student.query.get(1)
    print(stu)

    # 排序 order_by()
    # 升序: order_by(Student.id)
    # 降序: order_by(-Student.id)
    stus = Student.query.order_by(-Student.id).all()
    print(stus)

    # offset  limit   limit 1,4
    page = 2
    stus = Student.query.limit(3).all()
    stus = Student.query.all()
    # stus[0:3]  stus[3:6]
    stus[(page-1)*3 : page*3]

    stus = Student.query.offset((page-1)*3).limit(3).all()
    print(stus)

    # 模糊查询 like % _
    stus = Student.query.filter(Student.s_name.contains('小张')).all()
    print(stus)
    stus = Student.query.filter(Student.s_name.like('%小张%')).all()

    stus = Student.query.filter(Student.s_name.like('_张')).all()
    stus = Student.query.filter(Student.s_name.like('张_')).all()
    # startswith: 以什么开头
    # endswith: 以什么结束
    stus = Student.query.filter(Student.s_name.startswith('张')).all()
    stus = Student.query.filter(Student.s_name.endswith('张')).all()

    # 大于 gt  小于lt
    # 大于等于ge   小于等于le
    stus = Student.query.filter(Student.age.__ge__(10)).all()
    stus = Student.query.filter(Student.age >= 10).all()
    print(stus)

    # where id not in [1,2,3,4,5,6,7]
    stus = Student.query.filter(Student.id.in_([1,2,3,4,5,6,7])).all()
    stus = Student.query.filter(Student.id.notin_([1,2,3,4,5,6,7])).all()
    print(stus)

    # 多条件查询
    stus = Student.query.filter(Student.age == 2).\
        filter(Student.s_name.like('小%')).all()

    stus = Student.query.filter(Student.age == 2,
                                Student.s_name.like('小%')).all()

    # and 或者or
    stus = Student.query.filter(Student.age == 2 and Student.s_name.like('小%')).all()
    # and_, or_, not_
    stus = Student.query.filter(and_(Student.age == 2,
                                Student.s_name.like('小%'))).all()
    stus = Student.query.filter(or_(Student.age == 2,
                                     Student.s_name.like('小%'))).all()
    stus = Student.query.filter(not_(Student.age == 2)).all()

    print(stus)

    return '查询学生信息'


@home.route("/")
def index():
    print('__name__',__name__)
    return render_template('home/home.html')  #返回home.html模板