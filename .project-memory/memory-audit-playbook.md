# Memory Audit Playbook

## 什么时候启动
当 memory 文件数量变多、规则重复、输出摇摆、用户偏好变化或项目阶段变化时启动。

## 审计顺序
1. 先看 `.project-memory/README.md`。
2. 再看 `project-state.md`、`decision-log.md` 与 `user-preferences.md`。
3. 最后看低频模板、知识缓存与交付规范。

## 审计问题
- 这条信息是否仍然有效？
- 是否重复？
- 是否应该下沉、合并或移除？

## 默认修正顺序
先合并重复，再收缩低频细节，最后才新增缺口。
