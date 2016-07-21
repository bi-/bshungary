Title: Debconf example
Date: 2016-06-29
Category: bash, programming

confmodule is written in /bin/sh, do NOT use it with bash.
```sh
#!/bin/sh
. /usr/share/debconf/confmodule

if db_get suitcase_nginx/domain ;then
        echo ok
        echo $RET
else
        echo error key does not exists or other problems
fi
```
