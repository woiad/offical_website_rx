# offical_website_rx
公司企业网 flask 实现 前端+后台

#克隆后先运行requirements.txt 文件安装项目的环境和依赖
pip install -r requirements.txt

#安装好依赖后，要确保mysql服务启动，如果为启动，会报错
mysql.server start   #启动mysql服务

#后直接运行 flask run 项目启动

# 注意

配置文件 config.py里面的SQLALCHEMY_DATABASE_URI配置的是数据库连接的

mysql+pymysql://root(连接数据库的用户名):password(密码)@localhost:3306(地址:端口)/数据库名字
