# PostgresQL 项目实例

MacOS（ld: library not found for -lssl）
```
brew reinstall openssl
export LIBRARY_PATH=$LIBRARY_PATH:/usr/local/opt/openssl/lib/
```

项目依赖
```
pip install Flask
pip install SQLAlchemy
pip install sqlacodegen==1.1.6
pip install psycopg2
```

项目演示
```
➜  postgresql_project git:(master) ✗ source .venv/bin/activate
(.venv) ➜  postgresql_project git:(master) ✗ python run_app.py
[√] 当前环境变量: default
 * Serving Flask app "app_demo" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
[√] 当前环境变量: default
 * Debugger is active!
 * Debugger PIN: 180-067-960
```

访问 [http://0.0.0.0:5000/](http://0.0.0.0:5000/)


## Flask SQLAlchemy

http://flask.pocoo.org/docs/1.0/patterns/sqlalchemy/

https://docs.sqlalchemy.org/en/13/errors.html#error-e3q8

https://docs.sqlalchemy.org/en/13/core/pooling.html#pool-switching


## SQLAlchemy 连接池最佳实践

```
# 方式一：默认开启连接池，不设连接回收时间，连接永不回收（需要自己维护连接，两种方式：悲观处理、乐观处理，都需要动代码）
# engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_size=SQLALCHEMY_POOL_SIZE, max_overflow=0)

# 方式二：开启连接池，设置连接回收时间（web应用，短连接推荐这种方式）
engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_recycle=200, pool_size=SQLALCHEMY_POOL_SIZE, max_overflow=0)

# 方式三：禁用连接池，适合长连接、多任务场景
# engine = create_engine(SQLALCHEMY_DATABASE_URI, poolclass=NullPool)
```

如果采用 pgpool, 使用连接池的情况下, 需要注意`pool_recycle`不能大于`child_life_time`的值

http://www.pgpool.net/docs/latest/en/html/runtime-config-connection-pooling.html


## 延迟加载

http://flask.pocoo.org/docs/1.0/patterns/lazyloading/


SQLALCHEMY_ENGINE_OPTS

