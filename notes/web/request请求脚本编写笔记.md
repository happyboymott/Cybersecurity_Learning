编写python的requests库测试脚本，尝试了headers设置，get请求，post的form与json格式请求，期间所有请求统一通过本地的8080端口转发到bp进行查看(下图所示)，其中post请求中json提交时为json结构化数据，支持嵌套和数组，请求头中带Content-Type: application/json，用form则作为传统数据提交，型如xxx&xxx,数据值会进行url编码，同时不支持嵌套和数组，数据头带Content-Type: application/x-www-form-urlencoded

![bp抓包图片](../images/屏幕截图%202026-11-10%20231825.png)