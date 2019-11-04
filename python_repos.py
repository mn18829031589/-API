import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

#执行API调用并存储响应
url='https://api.github.com/search/repositories?q=language:python&sort=stars'
r=requests.get(url)  #响应对象
print("Status code:",r.status_code) #状态码

#将API响应存储在一个变量中
response_dict=r.json() #这个API返回JSON格式信息
print('Total repositories:',response_dict['total_count'])
#探索有关仓库信息
repos_dict=response_dict['items']
print('Repositories returned:',len(repos_dict))
names,plot_dicts=[],[]
for repo_dict in repos_dict:
    names.append(repo_dict['name'])
    #创建自定义工具提示,添加可单击的链接(键‘value’相关联的数字确定条形的高度,键‘label’相关联的
    # 字符串创建工具提示,键‘xlink’相关联的URL将每个条形转换为活跃的链接
    plot_dict={'value':repo_dict['stargazers_count'],
               'label':str(repo_dict['description']),
               'xlink':repo_dict['html_url']
               }
    plot_dicts.append(plot_dict)

#可视化
my_style=LS('#333366',base_style=LCS)
my_config=pygal.Config() #配置对象
my_config.x_label_rotation=45 #绕x轴旋转45°
my_config.show_legend=False #不显示左上角图例
my_config.truncate_label=15 #将较长的项目名缩短为15字符
my_config.show_y_guides=False  #表中水平线
my_config.width=1000 #自定义宽度

chart=pygal.Bar(my_config,style=my_style) #style类有默认的字体大小设置,当在上面设置字体时传不进去
  #config类中包含名为style的style类属性,style类中含有title/label_font_size属性
chart.config.style.title_font_size=24  #设置图表标题字体
chart.config.style.label_font_size=14 #副标签(包括x轴项目名和y轴大部分数字)字体
chart.config.style.major_label_font_size=18 #主标签(y轴5000整数倍刻度)字体,特殊刻度区分开
chart.title='Most-Starred Python Projects on Github'
chart.x_labels=names

chart.add('',plot_dicts)
chart.render_to_file('python_repos.svg')
"""
#概述最受欢迎的仓库
print("\nSelected information about each repository: ")
for repo_dict in repos_dict:
    print('\nName:',repo_dict['name'])
    print('Owner:',repo_dict['owner']['login'])
    print('Stars:',repo_dict['stargazers_count'])
    print('Repository:',repo_dict['html_url'])
    print('Description:',repo_dict['description'])
repo_dict=repos_dict[0]
#print('Keys:',len(repo_dict))
#for key in sorted(repo_dict.keys()):
#    print(key)
"""
