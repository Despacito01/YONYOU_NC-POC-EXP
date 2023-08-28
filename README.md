# YONYOU_NC-POC-EXP
This vulnerability is a remote command execution vulnerability

UClient 提供全新客户端，消除浏览器依赖，完成用户与企业应用的链接优化，并支持企业应用在终端上的自动升级。
UClient 打造一个面向企业的端服务平台，提供改善体验相关的端服务，并对提供的服务进行应用优化。
UClient 通过嵌入社交协同能力，建立企业用户之间的连接，提供企业间数据共享和连接的服务，形成基于企业服务云平台的企业社交网络。

用友 NC bsh.servlet.BshServlet 存在远程命令执行漏洞，该漏洞为远程命令执行漏洞，在无需登陆系统的情况下，攻击者可通过BeanShell测试接口（BeanShell可以直接执行java代码，适用于测试java代码的接口）直接执行任意命令，恶意攻击者成功利用该漏洞可获得目标系统管理权限。
该脚本能够测试目标网站是否具有远程代码执行漏洞，测试单个网站时使用-u参数，能够循环输入命令并执行
批量测试网站时只需导入站点的url文档，即可批量测试站点是否具有该漏洞
![image](https://github.com/Despacito01/YONYOU_NC-POC-EXP/blob/main/START.png?raw=true)
![image](https://github.com/Despacito01/YONYOU_NC-POC-EXP/blob/main/EXP.png?raw=true)
![image](https://github.com/Despacito01/YONYOU_NC-POC-EXP/blob/main/multiple.png?raw=true)
![image](https://github.com/Despacito01/YONYOU_NC-POC-EXP/blob/main/result.png?raw=true)
