# 打包Perun二进制文件

## 直接打包：

Perun可以直接使用pyinstaller打包，操作非常简单

- pip安装[pyinstaller](https://www.pyinstaller.org/)

    `pip install pyinstaller`

- 进入Perun/doc/package2exe目录

    `cd Perun/doc/package2exe`

- 根据.spec文件直接打包

    `pyinstaller Perun.spec`

- 成功打包二进制控制台单文件`Perun/doc/package2exe/dist/Perun.exe`，大小应该在4.5M左右

## 打包到更小

通过[UPX](https://upx.github.io/)压缩，Perun打成后生成文件应该不会超过3.5M

- 下载UPX(存放到Perun/doc/package2exe目录下，该目录下已经准备好了upx-3.95-win64版本)

    `https://github.com/upx/upx/releases`
    
- pip安装[pyinstaller](https://www.pyinstaller.org/)

    `pip install pyinstaller`

- 进入Perun/doc/package2exe目录

    `cd Perun/doc/package2exe`

- 根据.spec文件直接打包，并通过upx压缩

    `pyinstaller Perun.spec --upx-dir=upx-3.95-win64`

- 成功打包二进制控制台单文件`Perun/doc/package2exe/dist/Perun.exe`，大小应该在3.5M左右

## 测试打包环境：

- Python 2.7.15

- PyInstaller 3.4

- Windows 10
