要使用pyinstaller打包你的Tkinter应用以及相关资源如music.mp3，请按照以下步骤操作：

安装PyInstaller：如果你还没有安装pyinstaller，你可以通过pip安装：

- pip install pyinstaller
资源文件路径：你已经有了resource_path函数，它在打包后能够正确访问资源文件。

- 生成.spec文件：在你的Python脚本目录，运行以下命令来生成一个.spec文件：

- pyinstaller --onefile --windowed --add-data "music;music" your_script_name.py
这里your_script_name.py是你的Tkinter应用脚本的名字。--add-data选项将music文件夹（里面有你的music.mp3）与你的Python脚本一起打包。

注意：在Windows上使用;作为分隔符，而在Linux和Mac上使用:。

修改.spec文件：打开生成的.spec文件，确保datas字段包含你的音乐文件路径，如下：

- datas=[('music/music.mp3', 'music')]
构建应用：再次在终端或命令提示符中运行以下命令来构建应用：

- pyinstaller your_script_name.spec
完成：完成后，你的应用和所有需要的文件将被打包到dist目录中。你可以从那里运行你的应用。由于你使用了--onefile标志，应用会被打包成一个单独的可执行文件。

