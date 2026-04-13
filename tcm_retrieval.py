import os
import fitz  # PyMuPDF
import dashscope
from dashscope import Generation
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_pdf_files(pdf_dir):
    pdf_files = []
    for file in os.listdir(pdf_dir):
        if file.endswith(".pdf"):
            pdf_files.append(file)
    return pdf_files


def retrieve_top_k(symptoms, pdf_files, k=5):
    corpus = pdf_files + [symptoms]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)

    sim = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])[0]

    top_k_idx = sim.argsort()[-k:][::-1]

    return [pdf_files[i] for i in top_k_idx]


def extract_pdf_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""

    for page in doc:
        text += page.get_text()

    doc.close()
    return text


def analyze_single_paper(api_key, text, symptoms, title, max_token):
    text = text[:max_token]

    prompt = f"""
        你是一位严谨的中医临床文献研究员。

        【论文标题】：
        {title}

        【患者症状】：
        {symptoms}

        【文献内容】：
        {text}

        请严格提取：
        1. 这篇文章的核心结论；
        2. 适用于这些病症的方剂；
        3. 方剂适用的原因。
        """

    response = Generation.call(
        model="qwen-turbo",
        api_key=api_key,
        prompt=prompt,
        temperature=0.1
    )

    if "output" not in response:
        return f"{title} 分析失败"

    return response["output"]["text"]


def summarize_all(api_key, results, symptoms):
    combined = "\n\n".join(results)

    prompt = f"""
        你是一位中医专家，请基于多篇文献分析结果进行总结。

        【患者症状】：
        {symptoms}

        【文献研究结果】：
        {combined}

        请输出：
        1. 这些文章的核心结论；
        2. 能够适用这些病症的方剂；
        3. 方剂适用的原因。
        """

    response = Generation.call(
        model="qwen-turbo",
        api_key=api_key,
        prompt=prompt,
        temperature=0.2
    )

    return response["output"]["text"]


# ========== 主流程 ==========
def literature_retrieval(symptoms, api_key, pdf_dir="./pdfs", topk=5, max_token=10000):
    print("读取PDF列表...")
    pdf_files = load_pdf_files(pdf_dir)

    print(f"共 {len(pdf_files)} 篇论文")

    print("正在匹配最相关论文...")
    top_papers = retrieve_top_k(symptoms, pdf_files, topk)

    print("Top论文：")
    for p in top_papers:
        print(" -", p)

    results = []

    for pdf_name in top_papers:
        print(f"正在分析：{pdf_name}")

        pdf_path = os.path.join(pdf_dir, pdf_name)
        text = extract_pdf_text(pdf_path)

        result = analyze_single_paper(api_key, text, symptoms, pdf_name, max_token)
        results.append(result)

    print("正在汇总所有文献结论...")
    final_result = summarize_all(api_key, results, symptoms)

    return final_result


# ========== 运行 ==========
if __name__ == "__main__":
    #symptoms = "下肢水肿 气促 心悸 夜间不能平卧"
    symptoms = "近期工作压力大，头晕胀痛，急躁易怒，口苦咽干，失眠多梦，舌红苔黄，脉弦数。"
    #symptoms = "患者，男性，68岁。近2个月来逐渐出现双下肢水肿，初起为踝部轻度浮肿，晨轻暮重，按之凹陷。近2周症状加重，水肿上延至小腿，伴乏力明显。活动后气促明显，上楼需中途休息，夜间需垫高2个枕头方可入睡，偶有夜间憋醒。伴心悸、胸闷，食欲减退，小便量减少。查体可见双下肢凹陷性水肿，面色晦暗，四肢欠温。"
    api_key = "QWEN_KEY"

    result = literature_retrieval(symptoms, api_key)

    print("\n===== 最终结果 =====\n")
    print(result)