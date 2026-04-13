import os
from openai import OpenAI

QWEN_API_KEY = "sk-1170bf351c7a45e1bd348e9012d4268e"
DEEPSEEK_API_KEY = "sk-16e95fdf022a443ca23c64982a025e58"

qwen_client = OpenAI(
    api_key=QWEN_API_KEY,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

deepseek_client = OpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com"
)

# Qwen开方
def generate_prescription_qwen(symptoms):
    print("▶ Qwen 正在进行辨证与组方...")
    prompt = f"""
    你是一位资深中医。患者主诉症状如下：【{symptoms}】
    请执行以下任务：
    1. 给出明确的中医辨证结果，需要指出从何种症状得出何种证候（如：气虚血瘀、肝郁化火等）。
    2. 开具一个合适的药方（包含具体中药名和参考剂量）。
    3. 说明该方的“君臣佐使”逻辑。
    请直接输出结果，保持客观专业。
    """
    
    response = qwen_client.chat.completions.create(
        model="qwen3.6-plus",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6
    )
    return response.choices[0].message.content

# DeepSeek审核
def verify_and_provide_evidence_deepseek(symptoms, prescription):
    print("▶ DeepSeek 正在进行安全审核并汇聚证据...")
    prompt = f"""
    你是一位严谨的中药药理学专家。
    现有一位患者主诉如下症状：【{symptoms}】
    主治医师开具的方案如下：
    {prescription}
    
    请执行以下任务：
    1. 【安全校验】：检查方剂中是否存在“十八反”、“十九畏”或明显的毒性药物配伍冲突。如果有，请明确指出并建议替换；如果无，请声明“安全校验通过”。
    2. 【古典医籍支撑】：指出该药方的核心骨架来源于哪部中医经典（如《伤寒论》《金匮要略》中的原方或加减），并引用相关古籍条文。
    3. 【现代药理证据】：简述方中核心药物（君药/臣药）在现代医学中针对该症状的药理学作用（如：抗炎、改善微循环、调节免疫等）。
    
    请排版清晰，分为“安全校验”、“古典医籍支撑”、“现代药理证据”三个模块。
    """
    
    response = deepseek_client.chat.completions.create(
        model="deepseek-reasoner",
        messages=[{"role": "user", "content": prompt}],
        temperature=1.0
    )
    return response.choices[0].message.content

# main
def tcm_agent_run(symptoms):
    print(f"=== 收到患者症状：{symptoms} ===\n")
    
    # 开方
    qwen_output = generate_prescription_qwen(symptoms)
    print("\n【初诊方案 (Qwen)】\n", qwen_output)
    print("-" * 50)
    
    # 审核
    deepseek_output = verify_and_provide_evidence_deepseek(symptoms, qwen_output)
    print("\n【审查与证据报告 (DeepSeek)】\n", deepseek_output)
    
    return qwen_output, deepseek_output

if __name__ == "__main__":
    #test_symptoms = "近期工作压力大，头晕胀痛，急躁易怒，口苦咽干，失眠多梦，舌红苔黄，脉弦数。"
    test_symptoms = "突发眼部浮肿，皮肤紧绷，伴有发热、恶寒，小便不利。"
    tcm_agent_run(test_symptoms)