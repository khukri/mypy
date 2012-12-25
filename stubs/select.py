# TODO: BSD/Solaris-specific things
import builtins

# libepoll; Linux-specific:
int EPOLLERR
int EPOLLET
int EPOLLHUP
int EPOLLIN
int EPOLLMSG
int EPOLLONESHOT
int EPOLLOUT
int EPOLLPRI
int EPOLLRDBAND
int EPOLLRDNORM
int EPOLLWRBAND
int EPOLLWRNORM

# Unix-specific
int PIPE_BUF

# cross-platform
int POLLERR
int POLLHUP
int POLLIN
int POLLMSG
int POLLNVAL
int POLLOUT
int POLLPRI
int POLLRDBAND
int POLLRDNORM
int POLLWRBAND
int POLLWRNORM

str __doc__
bytes __file__

class error(OSError): pass

class epoll(builtins.object):
    bool closed
    any __getattribute__(self, str name): pass
    void __init__(self, int sizehint=-1, int flags=0): pass
    void close(self): pass
    int fileno(self): pass
    #<t> fromfd<t>(self, int fd): pass
    void modify(self, int fd, int eventmask): pass
    list<tuple<int,int>> poll(self, timeout=-1, maxevents=-1): pass
    list<tuple<int,int>> poll(self, timeout=-1.0, maxevents=-1): pass
    void register(self, int fd, int eventmask): pass
    void unregister(self, int fd): pass

class poll(builtins.object):
    void register(self, int fd, int eventmask=0): pass
    void modify(self, int fd, int eventmask): pass
    void unregister(self, int fd): pass
    list<tuple<int,int>> poll(self, float timeout=0.0): pass
    list<tuple<int,int>> poll(self, int timeout=0): pass

tuple<list<int>, list<int>, list<int>> select(list rlist, list wlist, list xlist, timeout=0.0): pass
tuple<list<int>, list<int>, list<int>> select(list rlist, list wlist, list xlist, timeout=0): pass
# TODO: implement support for the classes with a fileno() method
# The first three arguments are sequences of ‘waitable objects’: either
# integers representing file descriptors or objects with a parameterless
# method named fileno() returning such an integer

class kqueue(object): pass # TODO
class devpoll(object): pass # TODO
