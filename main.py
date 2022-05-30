# -*- coding: utf8 -*-
import pyftpdlib.authorizers
import pyftpdlib.handlers
import pyftpdlib.servers
import fs

# 認証ユーザーを作る
authorizer = pyftpdlib.authorizers.DummyAuthorizer()
authorizer.add_user('user', 'password', r"./ftp", perm='elradfmw')
authorizer.add_anonymous(r"./ftp", perm='elradfmw')

# 個々の接続を管理するハンドラーを作る
handler = pyftpdlib.handlers.FTPHandler
handler.authorizer = authorizer
handler.abstracted_fs = fs.MyFileSystem

# FTPサーバーを立ち上げる
server = pyftpdlib.servers.FTPServer(("0.0.0.0", 10021), handler)
server.serve_forever()