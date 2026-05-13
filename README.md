# 医疗 HL7 协议解析器 (Medical Data Analyzer) 🩺📊

本项目专注于医疗行业标准协议 **HL7** 的解析与数据转化，是医疗安全态势感知系统的核心组件。

## 🌟 核心功能
- **协议自动化提取**：自动解析原始 HL7 报文，提取患者 ID、就诊科室、诊断结论等关键业务字段。
- **数据结构化导出**：支持将解析结果实时转化为 **Excel (.xlsx)** 报表，便于合规性审计。
- **业务安全支撑**：为项目三的态势感知看板提供科室维度的业务数据支撑。

## 🛠️ 技术栈
- **语言**：Python 3.x
- **核心库**：`pandas`, `openpyxl`

## 📖 运行流程
1. 激活环境：`conda activate med_sec`
2. 运行解析：`python xiangmu2.py`
3. 查看产出：在当前目录查看 `Clinical_Data_Export.xlsx`
<img width="1600" height="778" alt="屏幕截图 2026-05-13 111025" src="https://github.com/user-attachments/assets/e0eda011-b929-4006-9bb0-da30adcf5e8e" />
<img width="1059" height="431" alt="屏幕截图 2026-05-13 111057" src="https://github.com/user-attachments/assets/81665643-c463-4284-86a0-9d47c4ae2531" />
