# Clash配置


### 下载与安装
可以自行到仓库中下载最新版本，也可以直接复制以下命令并执行。
```bash
wget https://github.com/Dreamacro/clash/releases/download/v0.19.0/clash-linux-amd64-v0.19.0.gz
```
依次执行下面命令。
```bash
gzip -d clash-linux-amd64-v0.19.0.gz
mv clash-linux-amd64-v0.19.0 /usr/bin/clash
chmod +x /usr/bin/clash
```

### 将其注册为服务并开机自启
在`/lib/systemd/system/`下创建文件`clash@.service`：
```bash
sudo vim /lib/systemd/system/clash@.service
```

将以下内容复制到`clash@.service`中：
```
[Unit]
Description=A rule based proxy in Go for %i.
After=network.target

[Service]
Type=simple
User=%i
Restart=on-abort
ExecStart=/usr/bin/clash

[Install]
WantedBy=multi-user.target
```

执行以下命令重新加载服务模块以及启动clash服务：
```bash
systemctl daemon-reload
systemctl start clash@user #user为自己当前的用户名
```

设置开机自启动：
```bash
systemctl enable clash@user
```

### 配置UI
第一次启动会在`~/.config/clash`下生成初始文件，现在开始配置dashboard，使得其可以在浏览器中配置节点。

```bash
cd ~/.config/clash
wget https://github.com/haishanh/yacd/archive/gh-pages.zip
unzip gh-pages.zip
mv yacd-gh-pages/ dashboard/
```

订阅文件可以从机场官网获得，或者复制Windows下的配置文件，在其中添加上如下配置：
```yaml
secret: xxxx
external-controller: 0.0.0.0:9090  #若是云服务器记得开放端口
external-ui: dashboard
```

重启服务：
```bash
systemctl restart clash@user
```

此时便可以通过`localhost:9090/ui/`或`ip:9090/ui/`进行访问了。
