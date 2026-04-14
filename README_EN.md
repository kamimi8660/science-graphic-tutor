# Science Graphic Tutor —— Advanced Wan 2.7 AI Skill 🧬⚡🧪

[**🇨🇳 中文**](./README.md) | [**🇬🇧 English**](./README_EN.md)

[![Type](https://img.shields.io/badge/Type-Wan_Skill-orange)](#)
[![Apache 2.0 License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE.txt)
[![Model](https://img.shields.io/badge/Model-Wan_2.7-purple)](#)
[![Python Required](https://img.shields.io/badge/Python-3.9+-green.svg)](#)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#)

> **What is a Skill?** This project is not just a batch of image generation code. It is an independent "Skill Module" (Prompt Stack + Automated Workflow) that encapsulates the native image generation capabilities of the **Wan 2.7** large model into a product. We have black-boxed complex prompt engineering and layout design, making it an out-of-the-box toolkit.

**Core Scenario: Auto-generating textbook-quality "Review Cards" for Physics, Chemistry, and Biology.**
When your AI Agent or backend system is equipped with this Skill: It will not only interface with Wan 2.7 to generate highly spatial scientific illustrations, but also automatically extract core principles and common pitfalls, leaving a 45% white space on the right side for text overlay. The final output is an A4-sized **"Textbook-quality Graphic Lecture Card"** ready for printing or screen projection.

Supports **all natural science subjects, from elementary school science to high school examinations and university core majors.**

---

## 📂 Project Directory Structure

```text
📦 science-graphic-tutor
 ┣ 📂 assets                  # High-quality generated graphic examples
 ┣ 📂 skills                  
 ┃ ┗ 📂 wan2.7-image-skill
 ┃   ┣ 📜 SKILL_Science_Graphic_Cards.md      # [Core] AI Agent Persona & Rules (CN)
 ┃   ┣ 📜 SKILL_Science_Graphic_Cards_EN.md   # [Core] AI Agent Persona & Rules (EN)
 ┃   ┣ 📂 scripts                             # [Core] Native Python generation script
 ┃   ┃ ┗ 📜 image-generation-editing.py
 ┃   ┗ 📂 references                          # R&D archives
 ┣ 📜 README.md               # Chinese Documentation
 ┣ 📜 README_EN.md            # English Documentation
 ┗ 📜 LICENSE.txt             # Open Source License
```

---

## ✨ Core Highlights

- 🎨 **Extreme Illustration Quality**: Leveraging the powerful foundation of Wan 2.7, the generated scientific diagrams are logically accurate and structurally clear—far superior to standard AI "aesthetic hallucination" outputs.
- 🧠 **Highly Condensed Knowledge**: Refuses huge walls of text. All text outputs are strictly filtered to contain only [Core Principles], [Key Steps], and combat-tested [Common Pitfalls].
- 🖨️ **Golden Typography Rule**: Pre-configured instructions force a 16:9 or A4 landscape ratio output, dedicating exactly 55% of the left to the illustration, leaving a pure white 45% on the right for text compositing.

---

## 🖼️ Practical Showcases

*Check the [Chinese README](./README.md) for full image displays of various physics, chemistry, and biology diagrams generated exclusively by this skill workflow.*

---

## 🚀 How to Use (Deployment Guide)

This Skill is completely decoupled. We highly recommend using it with cutting-edge powerful Desktop Agents (e.g., OpenClaw / Claude Code).

### Scheme A: Use within a Desktop Agent (OpenClaw / Claude Code) 【⭐ Highly Recommended】
If you are using an AI coding assistant with MCP (Model Context Protocol) or local sandbox capabilities, you don't need to manually type any code.

Simply copy the following text and send it to OpenClaw / Claude Code:

> 🗣️ Send this to the AI:  
> "Hello! Please set up and run the Science Graphic Tutor skill for me. Please **execute the following in the terminal yourself**:
> 1. Run `git clone https://github.com/kamimi8660/science-graphic-tutor.git` and `cd` into it.
> 2. Ensure dependencies exist via `pip install dashscope pillow`.
> 3. Temporarily set the environment variable `export DASHSCOPE_API_KEY="YOUR_ALIBABA_CLOUD_API_KEY"` (replace with my real key but do not write it to any file).
> 4. Silently read the full content of `skills/wan2.7-image-skill/SKILL_Science_Graphic_Cards_EN.md`, and absorb it as your persona and standard operating procedure for our next steps (do not alter its rules).
> 5. Finally, based on the rules you just learned, generate a high school physics 'Cyclotron' review diagram. Call the native python script in the directory to generate the image and save the result locally."

### Scheme B: No-code Agent Platforms (Coze / Dify)
1. **Create Agent**: Open platforms like Coze or Dify.
2. **Implant Brain**: Copy all contents from `SKILL_Science_Graphic_Cards_EN.md` and paste it as the Agent's System Prompt.
3. **Configure Plugins**: Mount a `Web Search` plugin and the `Wan 2.7 Image Generation` plugin.
4. **API Key**: Safely fill in your API Key within the platform's plugin settings.

### Scheme C: Traditional CLI Hardcoding
```bash
pip install dashscope pillow
export DASHSCOPE_API_KEY="YOUR_API_KEY"
python3 skills/wan2.7-image-skill/scripts/image-generation-editing.py \
  --user_requirement "Scientific textbook illustration of Projectile Motion. Diagram showing an object thrown horizontally..." \
  --size "1774*1254"
```

---

## 🤝 Support & Contributions

If this automated workflow has helped you, please consider giving this repository a **⭐ Star**! 

- For any collaboration or questions, feel free to open an [Issue](https://github.com/kamimi8660/science-graphic-tutor/issues).
- PRs for adding more subjects are highly welcome.
