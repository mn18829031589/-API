import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Python Projects'
chart.x_labels = ['httpie', 'django', 'flask']

#添加自定义工具提示(将鼠标指向条形将显示它表示的信息)
plot_dicts = [ {'value': 16101,'label': 'Description of httpie.'},
               {'value': 15028,'label': 'Description of django.'},
               {'value': 14798,'label': 'Description of flask.'},]
#pygal根据键‘value’相关联的数字确定条形的高度,键‘label’相关联的字符串创建工具提示
chart.add('', plot_dicts) #默认工具提示是星数和项目名
chart.render_to_file('bar_descriptions.svg')
