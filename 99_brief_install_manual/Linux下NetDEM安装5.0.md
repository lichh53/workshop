### NetDEM 安装方法 5.0 

Update date：2024 July 19

#### 通过ClashForUbuntu实现翻墙，通过GitHubDesktopForUbuntu实现下载NetDEM

##### 所需材料下载地址：[https://www.jianguoyun.com/p/DSN5ODQQo6K6CBjozaEFIAA] (访问密码：APAAM)

1. 下载`clash-linux.zip`，在下载文件夹的终端输入以下命令，解压压缩包，并移动重命名至本地路径下。

```
    unzip clash-linux.zip
    sudo mv clash-linux /usr/local/bin/clash
```

2. 关闭终端，在桌面打开终端，添加执行权限，并初始化clash后，关闭终端。
```
    sudo chmod +x /usr/local/bin/clash
    clash
```

3. 在下载文件夹的终端输入以下命令，将mmdb、yaml等配置文件移动至`/home/.config/clash/`；

```
    cd clash-linux
    sudo mv config.yaml /home/.config/clash/
    sudo mv Country.mmdb /home/.config/clash/
```

4. 运行Clash，于浏览器进入[https://clash.razord.top] 网址，测速并选择合适代理。（默认自动代理即可运行，若无法运行请于系统设置出开启手动代理，http和https均设置为```127.0.0.1:7890```。）

5. 下载GitHubDesktopForUbuntu；（安装包地址可能发生变化，建议跟踪地址[https://github.com/kontr0x/github-desktop-install]）。在桌面终端输入
```
    sudo wget https://github.com/shiftkey/desktop/releases/download/release-3.3.1-linux1/GitHubDesktop-linux-amd64-3.3.1-linux1.deb
```

6. 安装GitHubDesktopForUbuntu，在桌面终端输入
```
    sudo dpkg -i GitHubDesktop-linux-3.1.1-linux1.deb
```

7. 登录已授权的Github账号后即可通过图形界面下载所需库，所需环境以及需要更改的地方详见NetDEM_docs编译前请记得将所有库切换到develop分支。

8. 纯净的Ubuntu系统不带有gmp的库，需要安装gmp，gmp的下载网址为：[https://gmplib.org/]。需要使用命令进行解压：
```
    tar -xf gmp-6.3.0.tar.xz
    cd gmp-6.3.0
    ./configure --enable-cxx
    make
    make check
    sudo make install
```



9.需要调用netdem的python模块时，需安装pip3的支持。然后安装netdem的库。ubuntu系统中若已安装过编译过netdem，在netdem的路径下运行
```
    sudo apt install python3-pip
    make pip_install (已编译netdem)
    pip3 install netdem（未编译netdem）
```

10. OpenFOAM在新的ubuntu系统中编译可能会遇到没有flex库的问题，需要先安装flex的库。在终端输入：
```
    sudo apt install flex 
```

11. 系统中安装paraview，20.04链接的paraview为5.7.0，22.04链接的paraview为5.10.0。在终端输入：
```
    sudo apt install paraview
```
12. 若需要安装最新的paraview，需要在官网下载最新的包。下载后将解压缩后，将安装包复制到/usr/local/ 路径下，在~/.bashrc中修改默认的paraview路径，而后在终端中启用paraview即为最新版本的paraview。
```
    sudo tar -xvzf ParaView-5.13.0-MPI-Linux-Python3.10-x86_64.tar.gz 
    mv -rf ParaView-5.13.0-MPI-Linux-Python3.10-x86_64 /usr/local/paraview
    vim ~/.bashrc
    alias paraview=/usr/local/paraview/bin/paraview
    source ~/.bashrc
```

13. 无源代码安装python-netdem的库：

获取whl文件后的安装方式：
```
pip3 install [netdem-xxx.whl]
```

如何获取whl文件

检查确认制作whl的环境。
```
pip install setuptools wheel
```
在netdem的路径下运行：
```
python setup.py sdist bdist_wheel
```
即可在dist文件夹中获取生成的文件：以下为1.3版本的netdem在linux系统中，芯片架构为64位的X86处理器，python的版本为3.10。（ubuntu22.04的默认版本。）
netdem-1.3-cp310-cp310-linux_x86_64.whl

##### 编辑：李诚豪