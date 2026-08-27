# 日常 / Daily Practice

一个用于个人习惯打卡的静态单页网站。

## 运行

直接打开 `index.html` 即可使用；也可以运行：

```bash
npm run dev
```

习惯、打卡、目标和笔记数据统一保存在 GitHub 仓库文件中（默认路径：`data/checkins.json`），不再保存到浏览器 `localStorage`。首次使用需要在“设置与同步”中填写 GitHub 用户名、仓库名和 Fine-grained Personal Access Token；页面打开时会自动从 GitHub 读取，之后每次修改会自动同步。

## GitHub Token 权限

建议创建 Fine-grained token，只选择目标私有仓库，并授予 `Contents: Read and write` 权限。Token 只保存在当前浏览器，不会写进同步文件；GitHub 设置本身仍保存在浏览器中，用于下次自动连接。
