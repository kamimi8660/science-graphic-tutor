# 学霸理科图解卡片机 (Science Graphic Tutor) 🧬⚡🧪

这是一个基于 [Wan 2.7](https://github.com/Wan-Video/Wan2.1) 构建的自动化 AI 教学辅助工作流。

只需输入一个极其抽象难懂的理科知识点，AI 就能自动联网搜索验证，并生成一幅**「教科书级科学图解 + 左侧配图右侧留白排版文字」**的 A4 打印级教学卡片，实现理科知识点的空间与视觉降维打击。

支持 **涵盖小学自然科普、初高中中高考核心考点，直至大学专业的理化学科**。

---

## ✨ 核心亮点

- 🎨 **极致绘图质量**：得益于 Wan 2.7 卓越的模型底座，生成的科学图解逻辑精准、结构清晰，绝非普通的大模型“光影乱炖”。
- 🧠 **考点高度提炼**：拒绝大段枯燥文字，所有输出经过严格筛选，仅保留【核心原理】、【关键步骤】与经实战检验的【易错警示】，专治“看懂图但不会做题”。
- 🖨️ **图文黄金排版**：预装指令控制出图呈现 16:9 或 A4 横版比例，强制左侧 55% 画面留给插图，右侧 45% 留白用于知识点叠写，随时可用作课堂投屏或学生考前速记。

---

## 🖼️ 生成案例实测展示 (全学科矩阵)

为了验证本工作流的实战能力，我们在理化生各个维度的至难考点中进行了自动化生成测试：

### ⚡ 物理学科
涉及场论、力学机制、电磁学动量等需要极强空间建构能力的知识域：
- **[复合场运动] 速度选择器与质谱仪**：直观展示电磁平衡筛选极板与磁偏转半径实验。
   ![速度选择器与质谱仪](assets/mass_spec_final.png)
- **[天体力学] 开普勒三大定律**：用椭圆轨道再现近快远慢与焦点占位的宏大宇宙定律。
   ![开普勒定律](assets/kepler_final.png)
- **[电磁感应] 单杆模型**：安培力、感应电动势、速度衰增一目了然的动态过程宏观呈现。
   ![单杆模型](assets/emi_rod_final.png)
- **[运动学] 平抛运动**：将矢量分解附着于抛物线轨迹。
   ![平抛运动](assets/projectile_final.png)

### 🧪 化学学科
从微观粒子轨道到底层电化学机制、再到复杂空间有机合成：
- **[物质结构] 原子轨道与电子云**：极其科幻的三维 s/p/d 轨道包络面与电子概率云展示。
   ![原子轨道](assets/orbitals_final.png)
- **[有机机理] SN2 亲核取代反应**：完美的瓦尔登翻转(雨伞翻转)及背侧立体进攻轨迹。
   ![SN2 亲核取代](assets/sn2_final.png)
- **[电化学] 原电池与电解池**：通过双池串联，彻底根治电子绝不入水、唯见离子定向移动的痛点。
   ![原电池与电解池](assets/electrochem_final.png)

### 🧬 生物学科 / 地理科学
主攻微观结构与极其复杂的循环动态生理机制：
- **[经典启蒙] 动植物细胞三维对比**：细胞壁与大液泡带来的坚硬包络结构形态差异，直击眼球。
   ![动植物细胞](assets/cell_final.png)
- **[代谢图谱] 光合作用**：类囊体里的光反应与基质中的暗反应解耦呈现。
   ![光合作用](assets/photo_final.png)
- **[遗传分子] 基因表达(转录与翻译)**：从解旋的DNA、合成的mRNA穿出核孔、再到 tRNA 的流水线接力。
   ![转录与翻译](assets/gene_final.png)
- **[神经调节] 突触传递机理**：重现电信号通过钙离子通道引发胞吐释放并开启配体通道的魔法瞬间。
   ![突触传递](assets/synapse_final.png)
- **[地球科学] 岩石圈物质循环**：岩浆岩、沉积岩、变质岩与内源岩浆的三进三出循环机制图谱。
   ![岩石圈物质循环](assets/rock_cycle_final.png)
- **[大气科学] 三圈环流**：通过地球剖面三段环流深刻理解七压六带的热力动力学实质。
   ![大气三圈环流](assets/circulation_final.png)

---

## 🚀 如何使用 (部署指南)

本技能的部署形态极速、解耦。我们首推结合最前沿的底层桌面代理（如 OpenClaw / Claude Code）来进行极客式调用。

### 方案 A：在底层桌面端 Agent 中使用（OpenClaw / Claude Code 等）【⭐首推】
如果您正在使用具备 MCP (Model Context Protocol) 协议或本地沙盒控制权的强大 AI 编码助手，此方案将带给您全自动的魔法体验。

**Step 1：安装 Skill 到本地工作区**
将本仓库直接克隆到您需要进行教学研发的文件夹：
```bash
git clone https://github.com/kamimi8660/science-graphic-tutor.git
cd science-graphic-tutor
```

**Step 2：配置环境变量**
在终端临时暴露您的百炼调用密钥（请勿将其写入任何文件防泄露）：
```bash
export DASHSCOPE_API_KEY="您的阿里云百炼_API_KEY"
```

**Step 3：唤醒小龙虾 (OpenClaw/Claude) 并“植入大脑”**
在上面打开的同一个终端里启动您的 AI 助手命令行，并要求它强制加载规则：
> 🗣️ 您输入：“请深度读取 `skills/wan2.7-image-skill/SKILL_Science_Graphic_Cards.md` 这个 Markdown 文件，必须绝对遵循里面的规则作为你接下来的工作人设和操作 SOP。”

**Step 4：下达画图指令（享受魔法落地）**
> 🗣️ 您输入：“我是高三物理老师，帮我生成一张《回旋加速器》的高频考点教学图。请你自己调用这个目录下的相应脚本完成出图，把成品保存在当前文件夹给我。”

*(由于这些高级工具本身具有联网检索与脚本执行权限，它们会按照规则自主核对物理公式、调用万象 API 并生成合图。)*

---

### 方案 B：在 Agent 开发平台免代码部署（非程序员选项）
1. **创建智能体**：打开 [Coze / 扣子](https://www.coze.cn/) 或 Dify 创建一个新的 Agent。
2. **植入大脑**：打开仓库中的 `skills/wan2.7-image-skill/SKILL_Science_Graphic_Cards.md`，复制全部内容，直接粘贴为主体的「人设与回复逻辑（System Prompt）」。
3. **配置插件（Plugins）**：必选挂载「搜索引擎插件」与「Wan2.7 图像生成插件」。
4. **填入密钥**：在平台的插件授权设置中填写 API Key。

### 方案 C：本地传统命令行硬编码调用
直接调用原生图片生成脚本：
```bash
export DASHSCOPE_API_KEY="您的百炼_API_KEY"
python3 skills/wan2.7-image-skill/scripts/image-generation-editing.py \
  --user_requirement "Scientific textbook illustration of Projectile Motion. Diagram showing an object thrown horizontally..." \
  --size "1774*1254"
```
