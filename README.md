# SpaceCore
一个简单的集成化渗透测试工具,该工具在于帮助您更好的完成渗透测试,请不要用于非法用途
简单工具,仅供学习,渗透大佬轻喷 (｡･∀･)ﾉﾞ

## 工具使用步骤

因工具部分功能使用NMAP，这可能需要您在使用部分功能时，在您的客户端中安装NMAP，NMAP官方下载链接:请点击[NMAP官方链接](https://nmap.org/download.html)
在确保NMAP已在您的环境变量中后,可进行以下步骤

进入SpaceCore目录下安装该环境依赖
```python
pip install -r requirements.txt
```

运行该脚本

```python
python SpaceCore.py
```

## 支持功能

* 资产模块
  * whois 域名/IP 查询
  * 基于NMAP扫描的HTTP资产发现
* 漏洞利用模块
  * 一句话连接脚本
* 爆破模块
  * SSH弱口令爆破
  * MySQL弱口令爆破
* 漏洞扫描模块
  * Web Logic常见CVE漏洞扫描
  * Tomcat 常见CVE漏洞扫描

## 下版本预计新增

* 子域名查询
* 常见中间件CVE漏扫


## 下一步计划

* 考虑新增站点目录扫描
* 考虑新增简单SQL注入检测

## 如何贡献代码

若您对该项目感兴趣,可以帮助编写该项目,灰常感谢

(￣▽￣)～■干杯□～(￣▽￣)

* 新增已有模块下功能
    * 新增代码文件在某个module package下
    * 将代码入口在该module package的start方法下暴露，然后在help方法中添加功能说明
* 新增新的模块功能
    * 您应该新增一个package,然后创建__ init__.py文件并创建Start.py方法
    * 然后将您的接口暴露在Core的start方法下这将为main提供入口
* 为什么要这样?
    * 因为为了保证代码量的增加,整体代码不会变得混乱
    如果您有更好的建议,请发邮件告诉我:[erosionzhu@outlook.com]


## 捐献列表
* hunter 150￥