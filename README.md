# Listary-plugins

自己写的一些listary插件

## 编译`docker`镜像

```bash
docker build -t listray-plugins:1.0 .
```

## 使用`docker-compose`启动

```bash
[root@r3 listray-plugins]# cat docker-compose.yml
version: '3.3'
services:
    listray-plugins:
        image: listray-plugins:1.0
        ports:
            - '8000:8000'
        restart: always
        logging:
            options:
                max-size: 1g
```