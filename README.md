# 一触即发 · TouchAndTrigger

UE 5.8.4 纯蓝图毕业游戏。方向是雨后庭园里的滚球探索，以局部沾染、湿润、清洗和 Niagara 交互效果形成特效向 TA 作品。完整通关玩法仍需原型验证，不能把技术展示等同于完成的游戏。

## 从这里开始

1. 双击根目录的 `OpenProject.cmd`，使用本机 UE 5.8 打开工程。
2. 以 [当前进度](Docs/Progress.md) 中记录的关卡和蓝图为准，不依赖聊天中的旧路径。
3. 每次只做进度页中的一个任务。完成后记录现象、原因和下一步，再提交阶段成果。

工程文件是 `TouchAndTrigger.uproject`。旧 `BallPuzzle` 只作为参考，不继续开发，也不作为运行依赖。

## 文件在哪里

| 目录 | 放什么 | 什么时候打开 |
| --- | --- | --- |
| `Content/Game/Core` | 游戏模式与公共基础 | 调整启动与玩家生成 |
| `Content/Game/Player` | 球体、输入、相机 | 调整操作和视角 |
| `Content/Game/World` | 地面、区域和环境交互 | 搭关卡与交互规则 |
| `Content/Game/Effects` | 共用材质和 Niagara 效果 | 完善已验证的效果 |
| `Content/Game/Maps` | 项目关卡 | 试玩、搭场景 |
| `Content/Game/UI` | 必要界面 | 做操作提示、暂停和结束反馈 |
| `Content/Student/Contamination` | 你亲手制作的沾染实验 | 当前学习主线 |
| `Content/ThirdParty` | 确认许可后的外部资源 | 导入素材时 |
| `Docs` | 制作规则与进度 | 不确定下一步时 |
| `Tools` | AI 使用的编辑器辅助工具 | 日常制作不需要打开 |

未使用的分类先不创建资产。`Saved`、`Intermediate`、`DerivedDataCache`、`Binaries` 是生成内容，不是你的制作目录，不上传 Git。

## 制作与提交

- 玩法在蓝图里修改，外观在材质和 Niagara 中修改。不新增自写 C++ 游戏模块。
- 基础整理、命名、接线辅助、排错和验证可以由 AI 完成；关键效果、审美判断和核心玩法取舍由你掌握。
- 一个较大的功能完成并验证后，更新进度、提交 Git、推送 GitHub。小改动可以先本地提交，不逐次打扰你。
- 仓库：[GoalActionYes/GraduationProject](https://github.com/GoalActionYes/GraduationProject)。UE 资产使用 Git LFS。

需要了解项目分工、旧版教训和完整制作路线时，读 [制作约定](Docs/ProjectGuide.md)。
