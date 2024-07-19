## Git使用教学

完整学习git
网页可见：[常用Git命令清单-阮一峰的网络日志](http://www.ruanyifeng.com/blog/2015/12/git-cheat-sheet.html”)

### 常用指令

```sh
# 设置提交代码时的用户信息
git config [--global] user.name "[name]"
git config [--global] user.email "[email address]"

# 查看目前代码的状态 
git status
# 查看git的版本日志
git log 
# 更新到develop分支
git checkout develop 
# 拉取最新的版本
git pull 
# 回滚至之前的某个版本
git reset --hard xxxx(版本号) 
```


### 常用工作流程
```sh
# 下载代码
git clone https://github.com/apaam/netdem.git
# 检查更新最新版本
git pull
# 切换到develop分支
git checkout develop 
# （如果进行代码修改）在本地建立自己的新的分支
git checkout -b lichh53-test(分支名称)
# 提交该分支至github服务器
git push origin lichh53-test(分支名称)
# 在github网页端提交 compare & pull request （请注意选择提交源为 develop分支！）

# 待管理员审核代码后，该远程分支会merge入develop分支中

# 重复以下 继续进行开发(切换至develop分支，拉取最新)
git checkout develop
git pull
git checkout -b lichh53-test2(分支名称)
```
