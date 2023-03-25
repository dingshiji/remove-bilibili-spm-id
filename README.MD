## 复制B站链接时自动删除其中的 spm_id_from 参数


### 有一个 greasyfork 脚本也可以做到, 并且比这里的解决方式更好
[Bilibili 干净链接](https://greasyfork.org/zh-CN/scripts/393995-bilibili-%E5%B9%B2%E5%87%80%E9%93%BE%E6%8E%A5)


### spm_id_from 参数

`https://www.bilibili.com/video/BV1GJ411x7h7/?spm_id_from=123.456.789` 
当你分享的链接被人点击时, Biliili就知道了你们在B站外产生了互动. 

前段时间, 如果你关注一个已注销账号然后取关, B站会推荐你在现实中认识的人/群友的B站账号(已经修复). 应该就是通过这个 spm (super position model) 实现的. 

这个脚本可以在你复制B站链接时自动删除其中的 `spm_id_from` 参数.

### 安装

-   安装 `python3`
-   `pip install pyperclip`

#### 开机自启
**Windows**

为这个 `autorun_clipboard_cleaner.bat` 创建一个快捷方式, 放到 `C:\Users\YOUR_USERNAME\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup` 

也可以在文件管理器的地址栏输入 `shell:startup` 来打开这个目录

#### 手动运行

```bash
python clipboard_cleaner.py
```