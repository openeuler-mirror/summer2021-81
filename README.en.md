[中文版本 README](./README.md)
# Play games on openEuler Raspberry Pie!
## What is it
The scripts inside this repository can run Retropie on a Raspberry PI 4 running on openEuler 21.03.

Retropie can runs a lot of old games like Pac-Man.

## Install
First, I ported over 140 packages that openEuler doesn't have, and you'll have to wait for me to submit them to the openEuler community before you can install them, or I'll will find a place so you can download them.

Second, you need to install the necessary installation packages:

```shell
sudo dnf update 
sudo dnf install git
```

Then you can run the installation script.

```shell
cd
git clone --depth=1 git@github.com:apple-ouyang/RetroPie-Setup.git
cd RetroPie-Setup
git checkout openEuler
sudo ./retropie_setup.sh
```

Then the blue screen will launch, click yes on fews steps, click Basic Install, click yes along the way, and wait a long compilation (which will take about an evening), and you'll be ready.

If there is any error in installation, please install it several times, or put the issue here, I will try my best to solve it.

## Run game!
You can refer to my video running the game, mp4 video in this repo, here is the link[How to play](./How_to_play.mp4)

You need to find the game yourself, put it in the corresponding folder of ~/RetroPie/roms, and restart raspberry PI.

Rebooting takes you to Retropie, which initially requires you to do some keyboard configuration to simulate the gamepad.

Once configured, you can select the game you just downloaded and launch it!

......

And then you get a black screen, LOL, there are still some bugs that I can't fix, but you can still play the game like this.

Every time you run the game of your choice, after you see a black screen, you need to press F4 to exit Retropie, and then execute the following command to print an error message:

```shell
cat /dev/shm/runcommand.log
```

For example, after I run Pac-Man, see the black screen and press F4 to exit, and then run the above command to get the following output:

```shell
Parameters: 
Executing: /opt/retropie/emulators/retroarch/bin/retroarch -L /opt/retropie/libretrocores/lr-genesis-plus-gx/genesis_plus_gx_libretro.so --config /opt/retropie/configs/gamegear/retroarch.cfg "/home/ouyang/RetroPie/roms/gamegear/Pacman_(J).gg" --appendconfig /dev/shm/retroarch.cfg
/opt/retropie/supplementary/runcommand/runcommand.sh: line 1263: 21929 Segmentation fault      (core dumped) /opt/retropie/emulators/retroarch/bin/retroarch -L /opt/retropie/libretrocores/lr-genesis-plus-gx/genesis_plus_gx_libretro.so --config /opt/retropie/configs/gamegear/retroarch.cfg "/home/ouyang/RetroPie/roms/gamegear/Pacman_(J).gg" --appendconfig /dev/shm/retroarch.cfg
```

You only need to run the command after "Executing" or "(core dumped)" to start the game!
Such as:

```shell
/opt/retropie/emulators/retroarch/bin/retroarch -L /opt/retropie/libretrocores/lr-genesis-plus-gx/genesis_plus_gx_libretro.so --config /opt/retropie/configs/gamegear/retroarch.cfg "/home/ouyang/RetroPie/roms/gamegear/Pacman_(J).gg" --appendconfig /dev/shm/retroarch.cfg
```
when you want to exit, press ctrl + C to exit.

Here's the original README.

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
