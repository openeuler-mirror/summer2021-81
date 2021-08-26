# 分支说明

当前分支保存了为vlc这个视频框架软件包移植所需要的文件。

具体列表说明如下：

| 名称                | 说明                                                         |
| ------------------- | ------------------------------------------------------------ |
| done_*              | 各个轮次rpmbuild成功的src.rpm源码包                          |
| deplist_*           | 各个轮次所缺失的软件包名称，这里只保存SPEC文件对应的名称，如多个子包对应一个SPEC，则只保存对应SPEC文件名称 |
| download_deplist.sh | 在Fedora上运行，输入轮次，下载对应轮次的SPEC文件，压缩后传输到Windows的共享文件夹 |
| find_dep.sh         | 使用dnf的builddep命令，查找某个轮次所有rpm包所缺失的包名称   |
| real_deplist.sh     | 处理deplist_*，将不是软件包名称，而只是某个pkgconfig/文件名，转换为对应的包名 |

