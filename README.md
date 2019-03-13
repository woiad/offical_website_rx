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

rom flask_ckeditor import CKEditor

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

文章的问题解决了，接下来该解决的是图片的问题。大多数的文章都带有图片的
