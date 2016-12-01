

class CommandHandler:

    def unknow(self, session, cmd):
        session.push('Unknown command %s\r\n' %cmd)

    def handler(self, session, line):
        if not line.strip(): return
        parts = line.split('', 1)
        cmd = parts[0]
        try: line = parts[1].strip()
        except IndexError: line = ''
        meth = getattr(self, 'do_' + cmd, None)
        try:
            meth(session, line)
        except TypeError:
            self.unknow(session, cmd)

class EndSession(Exception): pass

class Room(CommandHandler):
    def __init__(self, server):
        self.server = server
        self.session = []

    def add(self, session):
        self.session.append(session)

    def remove(self, session):
        self.session.remove(session)

    def broadcast(self, line):
        for session in self.session:
            session.push(line)

    def do_logout(self, session, line):
        raise EndSession



















