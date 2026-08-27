# 日常 / Daily Practice

一个用于个人习惯打卡的静态单页网站。

## 运行

直接打开 `index.html` 即可使用；也可以运行：

```bash
npm run dev
```

数据默认保存在浏览器 `localStorage`。在“设置与同步”中填写 GitHub 用户名、仓库名和 Fine-grained Personal Access Token 后，可以把数据写入自己的仓库文件（默认路径：`data/checkins.json`）。

## GitHub Token 权限

建议创建 Fine-grained token，只选择目标私有仓库，并授予 `Contents: Read and write` 权限。Token 只保存在当前浏览器，不会写进同步文件。
