import os
import stat
import tempfile
import time
import traceback
import pyftpdlib.filesystems


class MyFileSystem(pyftpdlib.filesystems.AbstractedFS):

    def __init__(self, root, cmd_channel):
        super().__init__(root, cmd_channel=cmd_channel)

    def is_special_file(self, path):
        p, ext = os.path.splitext(path)
        return ext == '.query'

    # 指定されたパスがディレクトリであるか
    def isdir(self, path):
        if self.is_special_file(path):
            return True
        return os.path.isdir(path)

    # ディレクトリの内容をリストアップ
    def listdir(self, path):
        if self.is_special_file(path):
            return ['a']
        return os.listdir(path)

    # フォーマット済の内容を返す
    def format_mlsx(self, basedir, listing, perms, facts, ignore_err=True):
        line = u'type=dir;size=0;perm=el;modify=20071127230206;unique=801e33; 1\r\n'
        yield line.encode('utf8', self.cmd_channel.unicode_errors)

        line = u'type=file;size=156;perm=r;modify=20071029155301;unique=8012; 2\r\n'
        yield line.encode('utf8', self.cmd_channel.unicode_errors)

    #        -rw-rw-rw-   1 owner   group    7045120 Sep 02  3:47 music.mp3
    #        drwxrwxrwx   1 owner   group          0 Aug 31 18:50 e-books
    #        -rw-rw-rw-   1 owner   group        380 Sep 02  3:40 module.py
    def format_list(self, basedir, listing, ignore_err=True):
        for basename in listing:
            p = os.path.join(basedir, basename)
            is_dir = self.isdir(p)
            d = 'd' if is_dir else '-'
            line = (f'{d}rwxrwxrwx 1 owner group 0 Sep 02 3:47 {basename}\r\n')
            yield line.encode('utf8', self.cmd_channel.unicode_errors)
