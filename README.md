# BNDLG-public
Baidu Netdisk Download Link Get 

事先声明，本软件：
1. 不获取任何用户信息
2. 仅使用百度官方api接口

安装教程：
1. [fork](https://github.com/lemonorangeapple/BNDLG-public/fork)本仓库。
2. 部署后端：
   1. 将`backend/worker.js`中文件的代码复制。
   2. 在[Cloudflare Worker](https://workers.cloudflare.com/)创建一个worker。
   3. 将代码编辑为第2.i步复制的代码。
3. 部署前端：
   1. 将`config.py`中的`api_link`改为部署的api地址。
   2. 去[百度网盘开放平台](https://pan.baidu.com/union/)接入，创建应用并获取AppKey。
   3. 将`config.py`中的`client_id`改为AppKey。
   4. 在[百度网盘开放平台控制台](https://pan.baidu.com/union/console/applist)中打开第3.ii步中创建的应用。
   5. 在安全设置中，将"OAuth授权回调页"配置为`http://访问域名/login_success`。
   6. 在[vercel](https://vercel.com)中部署。
