
# memcache_lock  
Simple locking mechanism for Python 2.7 GAE, using memcache  
  
## Usage  
  
Import the UUIDLock class in any app engine module  
  
```  
from memcache_lock import UUIDLock  
```  
  
Acquire the lock  
  
```  
lock_helper = UUIDLock(key='lock_key')  
lock_helper.lock()  
```  
  
Release the lock  
  
```  
lock_helper.release()  
```  
  
## Options  
  
### You use other kwargs to control the lock mechanism  
  
  
Send default_timeout in secs to change the time after with the lock will be released automatically  
```  
lock_helper = UUIDLock(key='lock_key', default_timeout=3600)  
```  
**NOTE**: default value for timeout is 24 hours  
  
  
Send force_lock as True to acquire lock even if some other application already has lock on the key  
```  
lock_helper = UUIDLock(key='lock_key', force_lock=True)  
```  
**NOTE**: default value for force_lock is False  
  
  
Send max_wait_time in secs to raise Exception if lock is not acquired after waiting for max_wait_time  
```  
lock_helper = UUIDLock(key='lock_key', max_wait_time=120)  
```  
**NOTE**: default value for max_wait_time is 60 secs