# -*- coding: utf8 -*-
import pyftpdlib.authorizers
import pyftpdlib.handlers
import pyftpdlib.servers
import fs

# 認証ユーザーを作る
authorizer = pyftpdlib.authorizers.DummyAuthorizer()
authorizer.add_user('user', 'password', r"C:\Users\noritaka\ftp", perm='elradfmw')
authorizer.add_anonymous(r"C:\Users\noritaka\ftp", perm='elradfmw')

# 個々の接続を管理するハンドラーを作る
handler = pyftpdlib.handlers.FTPHandler
handler.authorizer = authorizer
handler.abstract_fs = fs.FFS

# FTPサーバーを立ち上げる
server = pyftpdlib.servers.FTPServer(("127.0.0.1", 10021), handler)
server.serve_forever()