# -*- coding:utf-8 -*-

from asyncore import dispatcher
from asynchat import async_chat
import asyncore
import socket

PORT = 5005
NAME = '127.0.0.1'

class EndSession(Exception): pass

class CommandHandler:
    # 类似于一个cmd.CMD的简单命令处理程序


    def unknown(self, session, cmd):
        # 响应未知命令

        session.push('Unknown command %s\r\n' % cmd)

    def handle(self, session, line):
        # 处理给的回话中接受到的行

        if not line.strip(): return

        # 分离命令：
        parts = line.split(' ', 1)
        cmd = parts[0]
        try: line = parts[1].strip()
        except IndexError: line = ''

        # 查找处理程序：
        meth = getattr(self, 'do_' + cmd, None)
        try:
            # 假定它是可以调用的：
            meth(session, line)
        except TypeError:
            # 如果不可以调用，这段代码用来响应未知的命令
            self.unknown(session, cmd)


class Room(CommandHandler):

    # 负责基本的命令处理和广播

    def __init__(self, server):
        self.server = server
        self.sessions = []

    def add(self, session):
        # 一个用户进入会话
        self.sessions.append(session)

    def remove(self, session):
        # 一个用户离开会话
        self.sessions.remove(session)

    def broadcast(self, line):
        # 向房间中所有用户发送一行数据
        for session in self.sessions:
            session.push(line)

    def do_logout(self, session, line):
        # 响应logout命令
        raise EndSession

class LoginRoom(Room):
    # 为刚刚连接的用户准备的房间

    def add(self, session):
        Room.add(self, session)
        # 当用户进入是 欢迎
        self.broadcast('Welcome to %s\r\n' % self.server.name)

    def unknown(self, session, cmd):

        # 所有未知命令都会返回一个错误提示
        session.push('Please log in\nUse "login <nick>"\r\n')

    def do_login(self, session, line):
        name = line.strip()
        # 确认用户输入了名字
        if not name:
            session.push('Please enter a name\r\n')
        elif name in self.server.users:
            session.push('The name %s is Taken. \r\n' % name)
            session.push('Please try again. \r\n')
        else:
            session.name = name
            session.enter(self.server.main_room)

class ChatRoom(Room):
    def add(self, session):
        self.broadcast(session.name + 'has entered the room.\r\n')
        self.server.users[session.name] = session
        Room.add(self, session)

    def remove(self, session):
        Room.remove(self, session)
        self.broadcast(session.name + 'has left the room.\r\n')

    def do_say(self, session, line):
        self.broadcast(session.name + ':' + line + '\r\n')

    def do_look(self, session, line):
        # look 命令查看谁在房间里
        session.push('The following are in the room:\r\n')
        for other in self.sessions:
            session.push(other.name + '\r\n')

    def do_who(self, session, line):
        # who命令查看谁登陆了
        session.push('The following are logged in:\r\n')
        for name in self.server.users:
            session.push(name + '\r\n')

class LogoutRoom(Room):

    def add(self, session):
        try: del self.server.users[session.name]
        except KeyError: pass





class ChatSession(async_chat):

    def __init__(self, server, sock):
        async_chat.__init__(self, sock)
        self.server = server
        self.set_terminator('\r\n')
        self.data = []
        self.name = None
        self.enter(LogoutRoom(server))

    def enter(self, room):

        try: cur = self.room
        except AttributeError: pass
        else: cur.remove(self)
        self.room = room
        room.add(self)


    def collect_incoming_data(self, data):
        self.data.append(data)

    def found_terminator(self):
        line = ''.join(self.data)
        self.data = []
        # self.server.broadcast(line)
        try: self.room.handle(self, line)
        except EndSession:
            self.handle_close()

    def handle_close(self):
        async_chat.handle_close(self)
        # self.server.disconnect(self)
        self.enter(LogoutRoom(self.server))


class ChatServer(dispatcher):

    def __init__(self, port, name):
        dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('', port))
        self.listen(5)
        self.name = name
        self.users = {}
        # self.sessions = []
        self.main_room = ChatRoom(self)

    #
    # def disconnect(self, session):
    #     self.sessions.remove(session)
    #
    # def broadcast(self, line):
    #     for session in self.sessions:
    #         session.push(line + '\r\n')

    def handle_accept(self):
        conn, addr = self.accept()
        ChatSession(self, conn)
        # self.sessions.append(ChatSession(self, conn))
        # print 'Connection attempt from', addr[0]


if __name__ == '__main__':
    s = ChatServer(PORT, NAME)
    try: asyncore.loop()
    except KeyboardInterrupt: pass