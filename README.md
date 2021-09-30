English Version [README](./README.en.md)
# 在 openEuler 树莓派上打游戏！
## 说明
这个仓库里面的脚本，能让搭载 openEuler 21.03 的树莓派4上跑 Retropie。

Retropie 是一个复古游戏机，能跑很多以前游戏机的游戏，比如吃豆人啥的。

## 安装
首先，我移植了 140 多个 openEuler 没有的安装包，你需要等我把这些软件包提交到 openEuler 社区之后才能安装，或者我得想办法上传到哪里你能下载的地方。

其次，你需要安装必要的安装包：

```shell
sudo dnf update 
sudo dnf install git
```

由于国内访问 github 常常会报错，因此如果后续使用 https 协议报 git clone 错误，你需要做以下配置，使用 ssh 协议，来解决报错

```shell
sudo su 
git config --global url."git@github.com:".insteadOf https://github.com/
```

然后你就可以运行安装脚本了

```shell
cd
git clone --depth=1 git@github.com:apple-ouyang/RetroPie-Setup.git
cd RetroPie-Setup
git checkout openEuler
sudo ./retropie_setup.sh
```

然后蓝色的界面便会启动，一路确认后，点击 Basic Install，再一路确认，等待漫长的编译之后（大概需要一晚上），你就安装好了。

如果安装报错，请多装几次，或者在这里提 issue，我会尽量解决。

## 运行游戏
你可以参考我的运行游戏的视频，就在仓库里面的mp4视频，这里是链接：[如何运行游戏](./如何在搭载openEuler21.03的树莓派上跑游戏.mp4)
你得自己找到游戏，然后放到 ~/RetroPie/roms 的对应文件夹下，之后重启树莓派。

重启你便能进入 Retropie，初始时需要你进行一些键盘配置，来模拟手柄。
配置好后，你便能选择你刚刚放好的游戏，然后启动！

。。。

然后你就会发现黑屏，笑，暂时这里有一些bug，我没能解决，不过你还是可以玩儿游戏。

每次运行你选择的游戏，在黑屏之后，你需要按下F4，退出 Retropie，然后执行以下命令吗，来打印报错信息：

```shell
cat /dev/shm/runcommand.log
```


比如，我运行吃豆人游戏之后，按下 F4 退出，之后运行以上命令就有以下输出：

```shell
Parameters: 
Executing: /opt/retropie/emulators/retroarch/bin/retroarch -L /opt/retropie/libretrocores/lr-genesis-plus-gx/genesis_plus_gx_libretro.so --config /opt/retropie/configs/gamegear/retroarch.cfg "/home/ouyang/RetroPie/roms/gamegear/Pacman_(J).gg" --appendconfig /dev/shm/retroarch.cfg
/opt/retropie/supplementary/runcommand/runcommand.sh: line 1263: 21929 Segmentation fault      (core dumped) /opt/retropie/emulators/retroarch/bin/retroarch -L /opt/retropie/libretrocores/lr-genesis-plus-gx/genesis_plus_gx_libretro.so --config /opt/retropie/configs/gamegear/retroarch.cfg "/home/ouyang/RetroPie/roms/gamegear/Pacman_(J).gg" --appendconfig /dev/shm/retroarch.cfg
```

最后一步，你只需要运行 Executing 后面的命令，就能开始游戏了！
比如：

```shell
/opt/retropie/emulators/retroarch/bin/retroarch -L /opt/retropie/libretrocores/lr-genesis-plus-gx/genesis_plus_gx_libretro.so --config /opt/retropie/configs/gamegear/retroarch.cfg "/home/ouyang/RetroPie/roms/gamegear/Pacman_(J).gg" --appendconfig /dev/shm/retroarch.cfg
```

以下是原版 README。

RetroPie-Setup
==============

General Usage
-------------

Shell script to setup the Raspberry Pi, Vero4K, ODroid-C1 or a PC running Ubuntu with many emulators and games, using EmulationStation as the graphical front end. Bootable pre-made images for the Raspberry Pi are available for those that want a ready-to-go system, downloadable from the releases section of GitHub or via our website at https://retropie.org.uk.

This script is designed for use on Raspberry Pi OS (previously called Raspbian) on the Raspberry Pi, OSMC on the Vero4K or Ubuntu on the ODroid-C1 or a PC.

To run the RetroPie Setup Script make sure that your APT repositories are up-to-date and that Git is installed:

```shell
sudo apt-get update
sudo apt-get dist-upgrade
sudo apt-get install git
```

Then you can download the latest RetroPie setup script with:

```shell
cd
git clone --depth=1 https://github.com/RetroPie/RetroPie-Setup.git
```

The script is executed with:

```shell
cd RetroPie-Setup
sudo ./retropie_setup.sh
```

When you first run the script it may install some additional packages that are needed.

Binaries and Sources
--------------------

On the Raspberry Pi, RetroPie Setup offers the possibility to install from binaries or source. For other supported platforms only a source install is available. Installing from binary is recommended on a Raspberry Pi as building everything from source can take a long time.

For more information, visit the site at https://retropie.org.uk or the repository at https://github.com/RetroPie/RetroPie-Setup.

Docs
----

You can find useful information about several components and answers to frequently asked questions in the [RetroPie Docs](https://retropie.org.uk/docs/). If you think that there is something missing, you are invited to submit a pull request to the [RetroPie-Docs repository](https://github.com/RetroPie/RetroPie-Docs).


Thanks
------

This script just simplifies the usage of the great works of many other people that enjoy the spirit of retrogaming. Many thanks go to them!
