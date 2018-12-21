import time
import uuid

from google.appengine.api import memcache


class UUIDLock(object):

    def __init__(self, key, default_timeout=24*3600, max_wait_time=60, force_lock=True):
        self.uuid = uuid.uuid4()
        self.key = key
        self.default_timeout = default_timeout
        self.force_lock = force_lock
        self.max_wait_time = max_wait_time
        self.wait_interval = max_wait_time * 10
        self.count = 0

    def is_open(self):
        initial_value = memcache.get(self.key)
        return initial_value is None or initial_value is False

    def lock(self):
        if not self.is_open():
            self._wait()
        return self._lock()

    def _lock(self):
        result = memcache.set(self.key, self.uuid)
        if self.is_lock_acquired():
            return result
        else:
            self._wait()
            return self._lock()

    def is_lock_acquired(self):
        return memcache.get(self.key) == self.uuid

    def _wait(self):
        while(not self.is_open() or self.force_lock):
            time.sleep(.1)
            self.count += 1
            if self.count > self.wait_interval:
                raise Exception('Timeout')

    def release(self):
        self._release()

    def _release(self):
        if self.is_lock_acquired():
            memcache.delete(self.key)
            return True
        else:
            return False
