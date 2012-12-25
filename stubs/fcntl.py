# constants
int DN_ACCESS
int DN_ATTRIB
int DN_CREATE
int DN_DELETE
int DN_MODIFY
int DN_MULTISHOT
int DN_RENAME
int FASYNC
int FD_CLOEXEC
int F_DUPFD
int F_EXLCK
int F_GETFD
int F_GETFL
int F_GETLEASE
int F_GETLK
int F_GETLK64
int F_GETOWN
int F_GETSIG
int F_NOTIFY
int F_RDLCK
int F_SETFD
int F_SETFL
int F_SETLEASE
int F_SETLK
int F_SETLK64
int F_SETLKW
int F_SETLKW64
int F_SETOWN
int F_SETSIG
int F_SHLCK
int F_UNLCK
int F_WRLCK
int LOCK_EX
int LOCK_MAND
int LOCK_NB
int LOCK_READ
int LOCK_RW
int LOCK_SH
int LOCK_UN
int LOCK_WRITE

str __doc__
bytes __file__

int fcntl(int fd, int opt, int arg=0): pass
bytes fcntl(int fd, int opt, bytes arg): pass

def ioctl(int fd, int opt, any arg = 0, bool mutate_flag=False): pass

void flock(int fd, int operation): pass

void lockf(int fd, int operation, length=0, start=0, whence=0): pass

