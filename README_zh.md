<p align="center">
  <img src="icon.png" alt="SlashFixer 图标" width="100" height="100">
</p>

# SlashFixer
[English](README.md) | [简体中文](README_zh.md)

SlashFixer 是一款实用工具，可以自动将 Windows 剪贴板中的反斜杠（\）转换为正斜杠（/）。

这个工具特别适合在 Windows 系统上进行 Python 编程的开发者使用，可以有效解决路径中反斜杠带来的困扰。

## 功能

- 实时监控剪贴板内容
- 自动将反斜杠转换为正斜杠
- 系统托盘图标，操作便捷
- 替换操作时提供视觉反馈
- 可随时开启或关闭替换功能

## 安装

### 方法一：使用源代码

1. 克隆或下载本仓库
2. 安装所需依赖：`pip install -r requirements.txt`
3. 运行程序：`python SlashFixer.py`

### 方法二：使用可执行文件

1. 在 [Release](https://github.com/Plasma-Blue/SlashFixer/releases) 页面下载最新版本
2. 解压下载的 zip 文件
3. 运行 SlashFixer.exe

注意：某些杀毒软件（如 Windows Defender）可能会将编译后的 .exe 文件误报为病毒。如果您对此有疑虑，可以查看源代码，或按照下面的说明自行编译。

## 使用

1. 启动程序：
   - 如果使用源代码：运行 `python SlashFixer.py`
   - 如果使用可执行文件：双击 SlashFixer.exe
2. 在系统托盘中找到 "\w/" 图标
3. 程序默认启用替换功能
4. 复制含有反斜杠的文本，程序会自动进行替换
5. 右键点击托盘图标可以：
   - 开启或关闭替换功能
   - 退出程序

## 编译

使用 Nuitka 可以将程序编译为独立的 EXE 文件：

1. 安装 Nuitka：`pip install nuitka`
2. 执行编译命令：`nuitka --windows-disable-console --standalone --onefile --windows-icon-from-ico=icon.png SlashFixer.py`
3. 编译完成后，在同一目录下找到生成的 EXE 文件

请注意：编译过程可能需要几分钟。生成的文件体积较大，但可以在未安装 Python 的环境中运行。

重要提示：某些杀毒软件可能会将编译后的 .exe 文件误报为病毒。如果遇到这种情况，可以将 SlashFixer.exe 添加到杀毒软件的白名单中。

## 限制

本程序仅支持 Windows 操作系统。

## 贡献

我们欢迎您提交错误报告或功能建议，帮助我们改进这个项目。

## 开源

本项目采用 [GNU General Public License v3.0](LICENSE) 许可证。
