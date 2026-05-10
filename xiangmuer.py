import hl7
import pandas as pd
import os

def process_hospital_data(file_path):
    print(f"[*] 医疗数据自动化流水线启动...")
    
    if not os.path.exists(file_path):
        print(f"[X] 错误：在文件夹下找不到 {file_path}")
        return

    try:
        # --- 1. 自动化数据清洗 ---
        with open(file_path, 'r', encoding='utf-8') as f:
            # 无论手改时有多少空格或换行，全部清洗并重组成标准 HL7 格式 (\r)
            lines = [l.strip() for l in f.readlines() if l.strip()]
            standard_data = '\r'.join(lines)
        
        # --- 2. 解析标准化数据 ---
        h = hl7.parse(standard_data)
        
        # 稳健取值工具函数
        def get_val(seg_name, index):
            try:
                target_seg = h.segment(seg_name)
                if index < len(target_seg):
                    # 处理组件分隔符 ^ 并剔除两端空格
                    return str(target_seg[index]).split('^')[0].strip()
                return ""
            except:
                return ""

        # --- 3. 构造业务逻辑记录 ---
        # 重新校对后的字段位置：PID-3 ID, PID-5 Name, PID-7 DOB, PID-8 Gender
        raw_gender = get_val('PID', 8).upper()
        
        record = {
            "消息控制ID": get_val('MSH', 9) or "未定义",
            "病人病历号": get_val('PID', 3) or "缺失",
            "患者姓名": get_val('PID', 5) or "未知",
            "生物学性别": "男" if raw_gender == "M" else ("女" if raw_gender == "F" else "未记录"),
            "出生日期": get_val('PID', 7) or "未填",
            "就诊科室": get_val('PV1', 3) or "待分诊",
            "系统记录时间": get_val('MSH', 6) or "无时间戳"
        }
        
        # --- 4. 导出高质量报表 ---
        df = pd.DataFrame([record])
        output_file = "Clinical_Data_Export.xlsx"
        
        # 如果文件已存在，先尝试删除（防止文件被打开导致无法写入）
        df.to_excel(output_file, index=False)
        
        print("-" * 40)
        print(f"[+] 处理成功！Excel 报表已生成。")
        print(f"[+] 当前解析对象: {record['患者姓名']} ({record['病人病历号']})")
        print(f"[+] 最终文件存放在: {os.path.abspath(output_file)}")
        print("-" * 40)

    except Exception as e:
        print(f"[X] 发生逻辑错误: {e}")
        print("💡 建议检查：确保 sample.hl7 里的竖线 | 数量符合 PID 段的标准格式。")

if __name__ == "__main__":
    process_hospital_data("sample.hl7")