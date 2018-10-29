# git 命令教程

1、mkdir 文件夹名名称 -----> 创建一个文件夹

2、git init 	      -----> git初始化，使当前文件夹成为git本地仓库

3、git add 文件名     -----> 添加文件到仓库
	（git add -f：强制添加文件）

4、git commit -m "改动记录" -----> 添加改动记录、提交说明

5、git status -----> 查看仓库当前状态

6、git diff 文件名 -----> 查看修改内容

7、git log -----> 查看从最近到最远的提交日志

8、git log --pretty=oneline

9、git reset --hard HEAD^ -----> 回退到上一个版本
	HEAD^^回退到上两个版本，HEAD~N回退到上N个版本

10、cat 文件名 -----> 查看文件内容

11、git reset --hard 版本号前几位 -----> 跳到指定版本

12、git reflog -----> 显示记录的git命令

13、git checkout -- 文件名 -----> 撤销文件在工作区的修改

14、git rm 文件名 -----> 在版本库中删除指定文件


------------------ git 远程管理教程 ------------------------

1、搭建自己git服务器或注册GitHub账号

2、ssh-keygen -t rsa -C "邮箱地址" -----> 创建SSH Key

3、在GitHub网站"Account settings","SSH Keys"点击"Add SSH Key"，填入任意Title，在文本框里粘贴id_rsa.pub文件的内容

4、点击"Add Key" 完成添加KEY

-------------- 创建远程gitHub仓库 ----------------------

1、在GitHub中点击"Create a new repo", 在Repository name填入文件夹名称（与本地保持一致可方便管理）

2、git remote add origin git@github.com:账户名/文件夹.git -----> 将本地仓库与远程关联

3、git push -u 远程库名 本地分支 -----> 将本地库内容推送到远程库，-u 参数使本地分支与远程分支关联，简化以后命令

4、git clone git@github.com:账号/路径.git -----> 从远程库克隆内容到本地（可以直接用git clone+网址 克隆远程库）

5、git checkout -b 分支名 -----> 创建一个新的分支（相当于：git branch 分支名; git checkout 分支名）

6、git branch -----> 查看当前分支

7、git merge 分支名 -----> 将指定分支合并到当前分支

8、git branch -d 分支名 -----> 删除指定分支

9、git log --graph --pretty=oneline --abbrev-commit -----> 带参数查看分支合并情况

10、git merge --on---m "合并说明" 分支名 -----> --on--off表示禁用Fast forward 

=====》》 说明：master分支应该保持稳定，仅用来发布新版本，要做出修改时使用别的分支修改后再合并

11、git stash -----> 储藏当前工作现场，等以后恢复现场可继续工作，此时可以创建新的分支来修改代码

12、git stash list -----> 查看被藏起来的工作现场

13、git stash pop -----> 恢复stash内容，并把stash内容删除（相当于git stash apply; git stash drop）

14、git stash apply stash@{N} -----> 恢复指定的stash

15、git remote -----> 查看远程库信息

16、git remote -v -----> 查看可以抓取和推送的git地址

17、git pull -----> 将最新的提交抓取下载，在本地合并解决冲突等

18、git tag "标签内容" -----> 给当前分支打标签

19、git tag "标签内容" 版本号 -----> 给指定版本打标签

20、git show "标签内容" -----> 插卡标签信息

21、git tag -d "标签名" -----> 删除指定标签，不删除内容

22、git push 远程仓库 标签名 -----> 推送标签到远程
	（git push 远程仓库 --tags：推送所有标签到远程）

23、git push 远程仓库 :refs/tags/标签名 -----> 删除远程标签，须先删除本地标签

24、git remote rm 远程库名 -----> 删除已关联的远程库（链接到新库时用）



25、git config --global color.ui true -----> 配置git显示颜色


----------------- 忽略特殊文件 -----------------------

1、在工作区目录创建".gitignore"文件，所有配置文件可以直接浏览：https://github.com/github/gitignore

忽略文件的原则是：

    1. 忽略操作系统自动生成的文件，比如缩略图等；
    2. 忽略编译生成的中间文件、可执行文件等，也就是如果一个文件是通过另一个文件自动生成的，那自动生成的文件就没必要放进版本库，比如Java编译产生的.class文件；
    3. 忽略你自己的带有敏感信息的配置文件，比如存放口令的配置文件。

2、git check--ignore -v 文件名 -----> 检查规则错误位置

3、git config --global alias.新命令 旧命令 -----> 用新命令代替旧命令（git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"）


--------------------- 搭建Git服务器 ---------------------

前提要求：1、准备一台运行Linux的机器
	  2、使用Ubuntu或Debian可以简单用apd命令完成安装

1、sudo apt-get install git -----> 安装git

2、sudo adduser git -----> 创建git用户，运行git服务

3、创建证书登陆，将需登录的yoghurt公钥id_rsa.pub内容拷贝到"/home/git/.ssh/authorized_keys"文件里，一行一个

4、sudo git init --bare sample.git -----> 初始化git仓库
   sudo chown -R git:git samle.git -----> 防止用户在服务器修改工作区，把owner改为git

5、编辑"/etc/passwd"文件，找到"git:x:1001:1001:,,,:/home/git:/bin/bash"修改为"git:x:1001:1001:,,,:/home/git:/user/bin/git-shell"。这样，git用户可以正常通过ssh使用git，但无法登陆shell，

6、git clone git@server:/srv/sample.git -----> 克隆工作区到自己电脑





