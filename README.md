# BNDLG
Baidu-Netdisk-Download-Link-Get

事先声明，本软件：
1. 仅使用百度网盘api
2. 不收集任何用户信息

部署教程：
1. [import](https://github.com/new/import)本仓库
2. 部署后端：
   1. 在[Cloudflare Workers](https://workers.cloudflare.com)创建一个workers。
   2. 将workers的代码更改为`backend/worker.js`的代码。
3. 部署前端：
   1. 在[百度网盘开放平台](https://pan.baidu.com/union/console/applist)创建一个应用并获取AppKey。
   2. 修改`config.py`，将`client_id`改为AppKey，将`api_link`改为后端访问地址
   3. 在[vercel](https://vercel.com)部署
