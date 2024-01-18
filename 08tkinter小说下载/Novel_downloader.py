""""""
from tkinter import messagebox

"""
使用 tkinter 打造一个小说下载器，想看什么小说，就下载什么小说

课题：使用 tkinter 打造一个属于自己的小说下载器

课程时间：14:00-15:00

知识点：
    1. tkinter

开发环境：
    1. 版  本：Python 3.6.5 |Anaconda, Inc.|
    2. 编辑器：pycharm
"""
import tkinter
# 把导入的方法当做普通的方法使用
from download import get_one_book, get_book_links, save_text, download_one_chapter


class Query:
    # 类 是一整个页面
    def __init__(self, master):
        # 类里面固定的一个方法
        self.root = master
        # 设置窗口对象的大小
        self.root.geometry('600x500+100+100')
        # 设置窗口的标题
        self.root.title('笔趣阁小说下载')
        # 设置窗口的图标
        self.root.iconbitmap('favicon.ico')

        # tkinter 的特殊变量，可以与组件里面的文字进行绑定
        self.index_url = tkinter.StringVar()

        self.create_page()
        self.handle_event()

    def create_page(self):
        """创建页面"""
        # label 文本框
        tkinter.Label(self.root, text='请输入你想要的下载的小说的目录页链接').place(x=30, y=30)
        # 输入框 entry 只是布局了一个控件
        tkinter.Entry(self.root, width=70, textvariable=self.index_url).place(x=30, y=60)
        # 保存路径
        tkinter.Label(self.root, text='保存路径').place(x=30, y=90)
        # # 路径标签
        tkinter.Entry(self.root).place(x=30, y=120)
        self.button1 = tkinter.Button(self.root, text='浏览', width=6, height=1)
        self.button1.place(x=200, y=120)

        self.button2 = tkinter.Button(self.root, text='下载', width=6, height=1)
        self.button2.place(x=350, y=120)

        self.button3 = tkinter.Button(self.root, text='清空', width=6, height=1)
        self.button3.place(x=450, y=120)

        # 文本框
        self.text = tkinter.Text(self.root, width=70, height=22)
        self.text.place(x=30, y=160)

    def handle_event(self):
        # 点击下载，就开始下载小说
        # 拿到需要的链接，
        # 当下载按钮被点击的时候，获取下载地址，然后再进行下载
        self.button2['command'] = self.download_book

    def download_book(self):
        book_url = self.index_url.get()
        if book_url:
            print('打印的是book_url',book_url)
            # 下载小说逻辑之前公开课已经实现过了，直接导入使用
            # 调用方法，获取每一章的下载地址
            links = get_book_links(book_url)
            for link in links:
                print('打印的是link',link)
                print('打印的是book_url + link',book_url + link)
                # 调用现有的逻辑，实现一章小说的下载
                title, text = download_one_chapter(link)
                save_text(title, text)
                # 把下载的信息插入的 text 文本框里面去
                # 第0行，第0个
                self.text.insert(0.0, f'{title} 下载成功\n')
                self.text.update()
        else:
            messagebox.showinfo(title='提示', message='下载链接不能为空')


if __name__ == '__main__':
    # 窗口对象
    root = tkinter.Tk()
    # 调用页面类，传入窗口对象
    Query(root)
    # 事件循环
    root.mainloop()

"""
思路跟的上吗 ？

"""
