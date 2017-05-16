"""
当前脚本的绝对路径：sys.argv[0]
当前脚本的文件名：os.path.basename(sys.argv[0])
当前脚本所在目录：os.path.dirname(sys.argv[0])
"""
import sys
#if len(sys.argv)<2:
#    sys.exit(-1)
if len(sys.argv)>1:
    import os
    filetoadd=os.path.basename(sys.argv[1])#返回文件名
    
    #改变工作目录
    os.chdir(os.path.dirname(sys.argv[0]))
    print('当前工作目录：'+os.getcwd())
    print('需要上传的文件：'+filetoadd)
    #git相关命令
    os.system('git add '+filetoadd)
    os.system('git commit -m "add {}"'.format(filetoadd))
    os.system('git push origin master')
    #%%
    import win32con
    import win32clipboard as w
    #设置剪贴板的内容
    def setText(aString):
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
        w.CloseClipboard()
    pathtocopy='https://raw.githubusercontent.com/cyyphy/markdown_figure/master/'+filetoadd
    codetopaste='![image]('+pathtocopy+')'
    setText(codetopaste)
    
    print('文件引用地址：\n\t'+pathtocopy)
    print('Markdown 引用代码：\n\t'+codetopaste)
    os.system('pause')



