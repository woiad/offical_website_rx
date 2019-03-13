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





#以下是关于本次项目的一些总结

项目刚开始是先做好前端页面的，想着先把前端页面做出来，才能根据页面去生成页面需要的数据。前端页面本来是用html5 + js + css,写的，本来打算前端页面独立写，数据的话就用python写接口，然后前端直接调用接口，获取数据，即可。但，发现问题，由于之前用vue做了好几个项目，想着这个项目也用模板渲染引擎来写,去搜索找的模板渲染引擎art-template，写起来破费力，模板需要在js中生成，然后再用jq将模板插入到指定的元素中，发现这样子写起来不好重用，有些重复的地方，想着可以重用，即写一个模板，其他的直接调用这个模板即可，找到art-template,研究了几天，发现，重用方面有点复杂，直接放弃。想着之前有学过python的flask框架，直接用这个框架来实现前后台的页面即可，方面许多。且，flask里面包含jinjia2这个模板渲染引擎，可以直接使用模板语法，方便许多，故整个项目直接改用python的flask框架来实现，（若一开始直接用falsk框架来实现，就不用费怎么多劲了。。。）。

首先要做的，就是把页面的一些写法给改了，首先生成一个公用的模板，命名为:layout.html,该模板包含页面公用的头部，即导航栏，底部，footer.和一些其他公用的部分。

  {% block content %}
  {% endblock %}
  
其他页面的内容，则放在这里面，加入其他页面有独立的css和js，可以在页面的header里和</body>之后分别加上

  {% block css %}
  {% endblock %}
  
  {% block js %}
  {% endblock %}
  
这里面的内容则是其他页面的独立的css和js。

其他的页面直接用jinjia的继承来使用该模板。

  {% extends 'home/layout.html' %}

提示:jinjia的所有模板和页面必须位于tempaltes目录下，渲染页面时，会直接在templates目录下寻找相关的页面。

然后，页面的内容则包含在block content 里面
  {% block content %}
  页面的内容。。。
  {% endblock %}

接着就是修改页面的链接，页面的所有跳转直接在views.py中生成，html页面的a标签的跳转改用python的url_for()

  <a href={{ url_for('index') }}></a>
  
index就是views.py中定义渲染相关页面的函数名。

页面改写完成。。。。

接下来就要写项目的后台，需要写一个后台管理，来管理页面的内容，该后台管理可以实现数据的增、删、查、改。由于前端页面和后台管理界面位于同一应用下，必须想办法把这两块内容分割开来，让这两个项目独立开。这下子，python的蓝图就登场了，利用它可以进行模块化，把同一个应用下的不同内容分隔开，变成连个独立的项目，互不干扰。首先在app目录下定义连个目录home,admin,home是前端页面，admin，是后台管理页面。然后再分别在这两个目录下创init.py,form.py,view.py
其中init.py,创建蓝图，form.py,定义相关的表单，views.py 定义视图的渲染和业务逻辑。（home 页面可以不用创建form.py）。

app > admin > init.py

  from flask import Blueprint
  
  admin = Blueprint('admin', __name__)
  
  import app.admin.views
  
app > home > init.py

  from flask import Blueprint
  
  home = Blueprint('home', __name__)

  import app.home.views
  
首先从flask中导入Blueprint（蓝图），接着蓝图实例化，第一个参数是蓝图的名字，第二个参数是一个python的特殊变量，表示当前的模块。之后导入需要使用蓝图
的视图。

相关目录结构

website/
  app/
    admin/
      views.py
      init.py
      form.py
    home/
      views.py
      init.py
    static/
    template/
      home/
      admin/
    init.py
  config.py

接下来要在全局变量app当中注册蓝图，才可以使用
app/init.py

  from .admin import admin as admin_blueprint
  from .home import home as home_blue_print
  
  app.register_blueprint(admin_blueprint)
  app.register_blueprint(home_blueprint)
  
先导入蓝图，然后在全局变量中注册蓝图，接着分别在admin/views.py和home/views.py中导入蓝图

  app/admin/views.py
  form . import admin
  
  app/home/views.py
  from .import home

然后修改home中的路由，把@app.route(path)修改成@home.route(path),admin里面的路由也变成了@admin.route(path)。之后每当调用路由之后的函数名，需要加上蓝图名前缀，例如：

app/home/views
  @home.route('/')
  def index():
  return render_template('home/index.html')

首页的logo如要跳转至页面的首页
  <a href="{{ url_for('home.index') }}"></a>
即凡是需要调用路由后面的函数名进行跳转的都需要加上相关的蓝图前缀。


蓝图定义好，现在一个应用包含了两个子项目，可以编写后台管理页面了。后台管理页面主要是用于处理数据的，因此，form表单少不了的，刚好flask也集成了form表单，wtf_form,可以使用这个form表单提前前端的form表单，该表单有许多的便利，可以很轻易的获取里面的数据，因此，使用falsk自带的form表单带来极大的便利。如需知道wtf_form的相关用法，请自行谷歌。

表单处理好了之后，碰到的第一个难题是，文章如何实现，官网一般都会包含一些公司的介绍，新闻文章，公司新闻等等文章，而这些文章要如何实现呢？谷歌了之后，才知道可以使用富文本编辑器来保存文章格式。富文本编辑器，可是一个大神器，使用它编辑好文章之后，把该文章的内容发送给后台，它会包含文章的格式，即把文章转为html格式，我只要保存该html格式的文章在数据库，前端直接获取，然后渲染文章，那么这个文章的格式，就跟之前编辑的时候是一摸一样的。。。好强大！然后又找到了一个flask集成的富文本编辑器，CKEditor。

先安装：
pip install flask-ckeditor

初始化扩展：
app/init.py

from flask_ckeditor import CKEditor

app = Flask(__name__)
ckeditor = CKEditor(app)

在form.py中创建 CKEditor 文本区域

from flask_ckeditor import CKEditorField

class articleForm(FlaskForm):
    ....
    article_content = CKEditorField(label='文章内容', validators=[DataRequired('文章内容不能为空')],
                                    render_kw={'class': 'form-control', 'placeholder': '请输入文章内容'})
                                    
接着在需要使用 ckeditor 的地方,form是articleForm的实例，有渲染函数传递过来的。
{{ form.article_content }}

加载 ckeditor

{{ ckeditor.load() }}

ckeditor的配置 #相关的配置在config.py中，想知道配置的详细信息，点击下面的链接

{{ ckeditor.config(name='article_content') }} #这个name至关重要，填写的是在表单类中定义的属性名，否则会报错，导致图片上传功能无法实现！！

之前就是在这里研究了好久，各种谷歌百度都不管用，好几次都想一个编辑器，好在，最后找到了问题，就是name的问题，必须是表单类中定义的CKEditorField（）的实例，否则图片上传功能，无法实现！！！！！这是我自己踩的第一个大坑。。。
这是
之前就是在这里研究了好久，各种谷歌百度都不管用，好几次都想一个编辑器，好在，最后找到了问题，就是name的问题，必须是表单类中定义的CKEditorField（）的实例，否则图片上传功能，无法实现！！！！！这是我自己踩的第一个大坑。。。
这是关于flask-ckeditor 的链接： https://juejin.im/post/5b35c0e4f265da5974057044

数据获取的页面写好了，文章的问题也解决了，接下来就该考虑的是，数据的存储问题了。数据肯定是要存到数据库里面的，这里使用到的数据库是mysql,关系型数据库。之前有学过mysql的命令，所以对它也有一些了解,但是在python中如何使用python，则不知道了，没关系，有谷歌，又是各种资料查找后，才找到解决的办法。用flask_sqlalchemy,这是一个orm框架，所谓的orm（object-relationship-mapping）即是，对象关系映射。对mysql的一些操作，可以使用python的对象的操作来代其，之后，orm框架会把这些操作映射成mysql的操作，即我们只需要使用python的对象的操作，就可以操作数据库了，而不需要直接写数据库的命令，是不是很强大，而且很方便，特别是对我们这些，不懂后端的前端工程师来说，简直就是神器啊，又一神器。。。
flask_sqlalchemy 官方文档：http://www.pythondoc.com/flask-sqlalchemy/quickstart.html
使用方法：

  app/init.py
  
    form flask_sqlalchemy import SQLALchemy
    
    app = Flask(app)
    db = SQLALchemy(app)
    
  condig.py
  
  #用于连接数据的数据库
  #SQLALCHEMY_DATABASE_URL = 'mysql+pyslql://user:password@ddress:port/database_name'
  SQLALCHEMY_dATABASE_URL = 'mysql+pysql://root:123456@localhost:3306/website_data'
  #如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。
  SQLALCHEMY_TRACK_MODIFICATIONS = True
  
  #提示：如果使用mysql，则数据库必须存在，也就是要先创配置中的建数据库，其次，mysql.server 必须开启。
  全局定义好了，接下来该写模型了，所谓的模型也就数数据库的字段，只不过，这些字段，我们使用python的类的属性来先定义创建。
  
  app/models.py
  
    from app import db
    
    class Article(db.Model):
    
    __tablename__ = 'article'
    
    id = db.Column(db.Integer, primary_key=True) #对应数据库的id字段
    title = db.Column(db.String(64), index=True, unique=True)  #对应数据库的title字段
    info = db.Column(db.String(256))  #对应数据库的info字段
    release_time = db.Column(db.String(128), index=True)  #对应数据库的release_time字段
    click_count = db.Column(db.String(64), index=True)  #对应数据库的click_count字段
    article_content = db.Column(db.Text)  #对应数据库的article_content字段
    article_type = db.Column(db.Integer, index=True)  #对应数据库的article_type字段
    cover_img = db.Column(db.String(64), index=True)  #对应数据库的cover_imgd字段
    
  模型定义好了之后，需要使用的话，直接导入即可。
  
  接下来就是实现数据存进数据的实现了！
  
  app/admin/views.py
  
  form app.models import Article
  from app import db
  from .from import articleForm  #编辑文章的form表单
  from flask import render_template , url_for
  
  @admin.route('/article_add')
  def article_add():
  form = articleForm()
  if validate_on_submit  #点击提交时执行，且校验都通过
      article = Article(title = form.data['title'], info = form.data['info'], release_time = form.data['release_time']
                         click_count = form.data['click_count'], article_content = form.data['article_content']
                         article_type = form.data['article_type'], cover_img  =form.data['cover_img']
      )
      db.session.add(article) #Article实例化后，添加到session,
      db.session.commit() #提交session,只有提交了session,数据库才有内容，如果只是把实例添加到session,而没有提交，数据库没内容
      return redirect(url_for('admin.article_add', form=form))
  return render_template('admin/article_add.html', form=from)
  
#说明一下,form.data[name],获取form表单的内容,nama就是表单字段的实例，这只是简单的实例，提交时还有一些逻辑处理，例如title不能重复，上传的图片的存储，图片的名字的修改等。

模型一旦创建之后，就无法修改，即一旦你定义好了类，后期想要在增加字段时，这时候，直接在类哪里增加，是没用的，数据库里面是无法增加的，这时候，就需要用到数据库迁移了，flask_migrate,可以更新数据库，保证数据库的表跟相对应的类的同步。

安装 flask_migrate

pip install flask_migrate

初始化：

app/init.py 

  from flask import Flask
  from flask_migrate import Migrate
  
  app = Flask(app)
  migrate = Migrate(app)
  
创建项目的迁移存储库:

  falsk db init

完成之后，会发现根目录多一个目录 migrations,会面保存着每次迁移的数据库的表即标的结构。
第一次迁移：
  falsk db migrate -m'迁移说明'

迁移完成之后：升级数据库。即同步类和数据库，修改数据库
flask db upgrade

数据库降级：把数据降回修改之前的状态
falsk db downgrade

#只有删除，增加，修改字段时，数据库迁移才能使用
#如果想要修改字段的数据类型的大小时，数据迁移也能使用，需要修改migrations里面的env.py文件
 context.configure(
          …………
          compare_type=True,  # 检查字段类型
          )
修改之后即可。

这样一来，数据的获取和储存都完成了，顿时松了一口气！！！
接下的是这次项目的第二大的坑，全文搜素。文章有个搜素的按钮，那么后台就要实现全文搜素的这个功能，由于之前没做过，只好去谷歌找资料，找了之后，发现有个全文搜素的库，elasricsearch，功能挺强大的，而且，也挺出名的，就用了这个库，安装配置好了之后，可以使用，但搜索的时候就有问题了，关键字搜索的时候有些关键字的结果会重复，有些不会，这。。。，费了好大力气，才做好的，结果出这个问题，吐血。。。。只能找办法看能不能解决了，结果，找了一天，依然没办法，好吧，只能放弃了，好郁闷，废了好大的力气，才做好，却要启用！！！！后用了 flask集成的flask_whooshee,这个比较好用了，配置也简单，但，又出问题了，搜索是只有全部的内容输入才能搜到，关键字搜不到。。。，找了谷歌，说要用分词,jieba,安装好，配置好，结果，依然用不了，我的天啊啊啊啊啊啊啊，奔溃中。。。。。。
好吧
