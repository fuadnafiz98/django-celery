## Commands 🥧

```bash

$ poetry new $PROJECT_NAME
$ poetry add django djangorestframework
$ django-admin startproject core .
$ django-admin startapp app
$ poetry add flower
$ poetry add django-celery-beat
```

### Error Descriptior 🎯

1. celery hard time limit error:

```
Traceback (most recent call last):
  File "/usr/local/lib/python3.10/site-packages/billiard/pool.py", line 684, in on_hard_timeout
    raise TimeLimitExceeded(job._timeout)
billiard.exceptions.TimeLimitExceeded: TimeLimitExceeded(10,)
```

2. celery soft time limit error:

```
Traceback (most recent call last):
  File "/usr/local/lib/python3.10/site-packages/celery/app/trace.py", line 451, in trace_task
    R = retval = fun(*args, **kwargs)
  File "/usr/local/lib/python3.10/site-packages/celery/app/trace.py", line 734, in __protected_call__
    return self.run(*args, **kwargs)
  File "/usr/src/app/app/tasks.py", line 13, in multiply
    sleep(2)
  File "/usr/local/lib/python3.10/site-packages/billiard/pool.py", line 229, in soft_timeout_sighandler
    raise SoftTimeLimitExceeded()
billiard.exceptions.SoftTimeLimitExceeded: SoftTimeLimitExceeded()
```
