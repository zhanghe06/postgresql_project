-- 表结构
CREATE TABLE public.users (
  id SERIAL PRIMARY KEY NOT NULL, -- 主键ID
  name CHARACTER VARYING(100) DEFAULT '', -- 姓名
  address CHARACTER VARYING(100) DEFAULT '' -- 地址
);
CREATE UNIQUE INDEX idx_u_name ON public.users USING BTREE (name);
COMMENT ON TABLE public.users IS '用户表';
COMMENT ON COLUMN public.users.id IS '主键ID';
COMMENT ON COLUMN public.users.name IS '姓名';
COMMENT ON COLUMN public.users.address IS '地址';
