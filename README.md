# 生日快乐贺卡

这是根据截图中的 Python Turtle 蛋糕重做的小项目，包含两个版本：

- `index.html`：推荐使用。手机和电脑浏览器都能打开，点击按钮会点亮蜡烛、播放生日旋律并撒出彩纸。
- `birthday_cake.py`：Python Turtle 桌面版，不需要安装第三方库。

## 发给微信好友

最省事的方式是把整个 `birthday-card` 文件夹压缩后发送。好友解压并打开 `index.html` 即可观看。

更适合手机的方式是把 `index.html` 部署到任意静态网页托管服务，再把链接发给好友。网页是单文件，不依赖网络资源。

## 写上好友名字

部署成链接后，可以在网址末尾加参数：

```text
?name=小明
```

也可以同时自定义祝福语：

```text
?name=小明&wish=愿你新的一岁平安顺遂，天天开心
```

中文链接发送前建议让浏览器自动转码。直接打开本地文件时也支持这些参数。

## 运行 Python 版

电脑已安装 Python 3 时，在项目目录执行：

```powershell
python birthday_cake.py
```

Python 版使用系统自带的 `turtle` 和 `tkinter`；部分精简版 Python 可能没有安装 Tk 组件。
