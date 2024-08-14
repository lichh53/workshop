## 新手入门NetDEM常用命令行

本文档仅为了尽快上手NetDEM使用，总结常用的相关Linux命令，完整Linux命令请自行系统学习. 学习的最好方法就是一边使用一边查文档， 用的多了就记住了。

##### 1 **Print current working directory**

输出当前的目录。

```sh
# 打印当前目录
pwd
```

##### 2 **List directory contents**

显示当前路径下有哪些文件。

```sh
# ls 相对路径
ls ./ #【表示当前目录下】 
ls ../ #【上一级目录下】
# ls 绝对路径
ls /home
# ls 选项 路径 ls -lah /home # 选项解释:
-l:表示list，表示以详细列表的形式进行展示 
-a:表示显示所有的文件/文件夹(包含了隐藏文件/文件夹) 
-h:表示以可读性较高的形式显示
# ls -l 中 “-”表示改行对应的文档类型为文件，“d”表示文档类型为文件夹。 
# 在Linux中隐藏文档一般都是以“.”开头
```

##### 3 **change directory**

 更换当前终端的工作路径。

```sh
# 以下两条命令等价，直接进入当前用户的目录下【很常用】 
cd
cd ~
# 进入到上级目录下
cd ..
# 进入到上级目录中的local目录下 cd ../local
# 进入到/usr/local目录下 
cd /usr/local
```

##### 4 **make directories**

```sh
# 在当前路径下创建出目录“myfolder”
mkdir myfolder
# 创建 ~/a/b/c 目录 
mkdir -p ~/a/b/c
# 在当前目录分别创建a、b、c三个文件夹 
mkdir a b c
```

##### 5 **remove files or directories**

```sh
# 删除当前路径下的myfile文件 
rm myfile
# 删除/usr路径下的myfile文件 
rm /usr/myfile
# 删除当前路径下的abc文件夹 
rm -rf myfolder
# 删除/usr路径下的abc文件夹
rm -rf /usr/myfolder
```

##### 6 **copy files and directories**

```sh
# cp命令来复制一个文件
cp /home/bing/myfile ./
# 复制/home/bing/myfolder文件夹到根目录/下 
cp -r /home/bing/myfolder /
```

##### 7 **reboot the machine**

```sh
# 立即重启 
reboot
```

##### 8 **power-off the machine**

```sh
# 立即关机 shut -h [时间]
shutdown -h now
```

##### 9 **an interface to the system reference manuals**

```sh
# 查看ls命令的手册 
man ls
# 查看cd命令的手册 
man cd
# 查看man命令的手册 
man man
```

## vim 编辑

在linux系统中编辑~/.bashrc或者在Mac系统中编辑～/.zshrc文件都需要使用vim编辑器进行文本编辑。（docker中的ubuntu可能没有自带vim，需要安装。）

```sh
sudo apt-get install vim
```

通过在命令行中输入，以通过vim打开文本。

```sh
vim ～/.bashrc
```

可以简单的将Vim编辑器理解为两个模式，1阅读模式。2编辑模式。

在阅读模式时，单击"i"进入编辑模式。

在编辑模式时，单击"esc"进入阅读模式。

"w"保存文件，“q”退出程序。

![img](vim-vi-workmodel.png)

