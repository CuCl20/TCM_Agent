import fitz
import os

def split_pdf_by_ranges(input_pdf, ranges, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    
    doc = fitz.open(input_pdf)
    
    for r in ranges:
        new_doc = fitz.open()
        new_doc.insert_pdf(doc, from_page=r["start"]-1, to_page=r["end"]-1)
        
        filename = f"{r['title']}.pdf"
        path = os.path.join(output_dir, filename)
        
        new_doc.save(path)
        new_doc.close()
        
        print(f"已生成: {path}")
    
    doc.close()

ranges = [
    {
        "title":"Safety and efficacy of Qishen granules inpatients with chronic heart failure———studyprotocol for a randomized controlled trial",
        "start":7,
        "end":13
    },
    {
        "title":"The effects of qishen granules for patients with chronic heart failure————A multicenter randomized double-blind placebo-controlled trial",
        "start":14,
        "end":24
    },
    {
        "title":"基于“虚、毒、瘀”浅述芪参颗粒治疗慢性心力衰竭气虚血瘀证中医理论依据",
        "start":25,
        "end":27
    },
    {
        "title":"芪参活血颗粒治疗脓毒症心肌损伤的随机对照临床研究",
        "start":28,
        "end":31
    },
    {
        "title":"芪参颗粒治疗冠心病的临床研究",
        "start":32,
        "end":33
    },
    {
        "title":"益心解毒方联合硝酸异山梨酯治疗老年无症状性心肌缺血疗效观察",
        "start":34,
        "end":36
    },
    {
        "title":"A Network Pharmacology Approach to Explore the Mechanisms of Qishen Granules in Heart Failure",
        "start":37,
        "end":47
    },
    {
        "title":"Antiapoptosis and Antifibrosis Effects of Qishen Granules on Heart Failure Rats via Hippo Pathway",
        "start":48,
        "end":60
    },
    {
        "title":"Cardioprotective Effects of Qishen Granule (芪参颗粒) on Sarcoplasmic Reticulum Ca2+ Handling in Heart Failure Rats",
        "start":61,
        "end":68
    },
    {
        "title":"Cardioprotective Effects of QishenyiqiMediated by Angiotensin II Type 1 Receptor Blockade and Enhancing Angiotensin-Converting Enzyme 2",
        "start":69,
        "end":77
    },
    {
        "title":"Drug Target Prediction Based on the Herbs Components————The Study on the Multitargets Pharmacological Mechanism of Qishenkeli Acting on the Coronary Heart Disease",
        "start":78,
        "end":87
    },
    {
        "title":"Multipronged Therapeutic Effects of Chinese Herbal Medicine Qishenyiqi in the Treatment of Acute Myocardial Infarction",
        "start":88,
        "end":99
    },
    {
        "title":"P2X7R-NEK7-NLRP3 Inflammasome Activation————A Novel Therapeutic Pathway of Qishen Granule in the Treatment of Acute Myocardial Ischemia",
        "start":100,
        "end":117
    },
    {
        "title":"Pseudotargeted screening and determination of constituents in Qishen granule based on compound biosynthetic correlation using UHPLC coupled with high resolution MS",
        "start":118,
        "end":129
    },
    {
        "title":"Qishen Granule (QSG) Inhibits Monocytes Released From the Spleen and Protect Myocardial Function via the TLR4-MyD88-NF-κB p65 Pathway in Heart Failure Mice",
        "start":130,
        "end":142
    },
    {
        "title":"Qishen Granule alleviates endoplasmic reticulum stress-induced myocardial apoptosis through IRE-1-CRYAB pathway in myocardial ischemia",
        "start":143,
        "end":155
    },
    {
        "title":"Qishen granule attenuates cardiac fibrosis by regulating TGF-β Smad3 and GSK-3β pathway",
        "start":156,
        "end":167
    },
    {
        "title":"Qishen granule attenuates doxorubicin-induced cardiotoxicity by protecting mitochondrial function and reducing oxidative stress through regulation of Sirtuin3",
        "start":168,
        "end":179
    },
    {
        "title":"Qishen Granule Protects against Doxorubicin-Induced Cardiotoxicity by Coordinating MDM2-p53-Mediated Mitophagy and Mitochondrial Biogenesis",
        "start":180,
        "end":196
    },
    {
        "title":"Qishen granules exerts cardioprotective effects on rats with heart failure via regulating fatty acid and glucose metabolism",
        "start":197,
        "end":213
    },
    {
        "title":"Qishen granules inhibit myocardial inflammation injury through regulating arachidonic acid metabolism",
        "start":214,
        "end":226
    },
    {
        "title":"Qishen granules regulate intestinal microecology to improve cardiac function in rats with heart failure",
        "start":227,
        "end":239
    },
    {
        "title":"Qishenyiqi Dropping Pill attenuates myocardial fibrosis in rats by inhibiting RAAS-mediated arachidonic acid inflammation",
        "start":240,
        "end":249
    },
    {
        "title":"Qishenyiqi Protects Ligation-Induced Left Ventricular Remodeling by Attenuating Inflammation and Fibrosis via STAT3 and NF-kB Signaling Pathway",
        "start":250,
        "end":262
    },
    {
        "title":"RNA-Seq Profiling to Investigate the Mechanism of Qishen Granules on Regulating Mitochondrial Energy Metabolism of Heart Failure in Rats",
        "start":263,
        "end":275
    },
    {
        "title":"Simultaneous Determination of Twenty-Five Compounds in Rat Plasma Using Ultra-High Performance Liquid Chromatography-Polarity Switching Tandem Mass Spectrometry and Its Application to a Pharmacokinetic Study",
        "start":276,
        "end":296
    },
    {
        "title":"The Protective Effect of Qishen Granule on Heart Failure after Myocardial Infarction through Regulation of Calcium Homeostasis",
        "start":297,
        "end":307
    },
    {
        "title":"The roles of Qishen granules recipes, Qingre Jiedu, Wenyang Yiqi and Huo Xue, in the treatment of heart failure",
        "start":308,
        "end":319
    },
    {
        "title":"基于HSP27-TLR4、NF-κB 通路的芪参颗粒对大鼠心肌梗死后炎症反应的影响",
        "start":320,
        "end":325
    },
    {
        "title":"基于网络药理学预测的芪参颗粒干预过量异丙肾上腺素诱导小鼠心力衰竭的机制研究",
        "start":326,
        "end":329
    },
    {
        "title":"基于氧化应激调控的芪参颗粒干预心力衰竭大鼠的机制研究",
        "start":330,
        "end":333
    },
    {
        "title":"基于转录组学的芪参颗粒调控脾脏ALOX15 、STAT3 通路抑制单核细胞释放防治心力衰竭的机制研究",
        "start":334,
        "end":341
    },
    {
        "title":"芪参颗粒调控ACE2-Ang(1-7) -Mas 轴改善大鼠心力衰竭合并骨骼肌萎缩的作用及机制探讨",
        "start":342,
        "end":346
    },
    {
        "title":"芪参颗粒调控SIRT1、PGC-1α、FNDC5通路介导的线粒体稳态防治心力衰竭心室重构的作用机制",
        "start":347,
        "end":353
    },
    {
        "title":"芪参颗粒调控心衰大鼠单核－ 巨噬细胞系统抗纤维化机制研究",
        "start":354,
        "end":354
    },
    {
        "title":"芪参颗粒对后负荷加重小鼠心肌组织中Fas、Fasl凋亡信号转导通路的影响",
        "start":355,
        "end":358
    },
    {
        "title":"芪参颗粒对心肌梗死后心力衰竭大鼠心肌纤维化的影响",
        "start":359,
        "end":364
    },
    {
        "title":"芪参颗粒对心力衰竭大鼠心脏功能和心肌细胞内钙离子浓度的影响",
        "start":365,
        "end":367
    },
    {
        "title":"芪参颗粒对血管紧张素Ⅱ诱导的大鼠心肌成纤维细胞基质代谢的影响",
        "start":368,
        "end":372
    },
    {
        "title":"芪参颗粒防治阿霉素所致心肌损伤的作用机制研究及实验验证",
        "start":373,
        "end":380
    },
    {
        "title":"芪参颗粒及其拆方对压力负荷所致心肌肥厚作用的实验研究",
        "start":381,
        "end":386
    },
    {
        "title":"芪参颗粒联合运动疗法对慢性心力衰竭大鼠心肌细胞凋亡及相关蛋白表达的影响",
        "start":387,
        "end":389
    },
    {
        "title":"芪参颗粒联合运动疗法对心力衰竭大鼠心功能及心室重构的影响",
        "start":390,
        "end":395
    },
    {
        "title":"益心解毒方对Ameroid缩窄环致心功能不全小型猪血流动力学的影响",
        "start":396,
        "end":398
    },
    {
        "title":"益心解毒方对Ameroid 缩窄环致心功能不全小型猪血液流变学的影响",
        "start":399,
        "end":403
    },
    {
        "title":"益心解毒方对Ameroid 缩窄环致气虚血瘀小型猪证候表征的影响",
        "start":404,
        "end":407
    },
    {
        "title":"益心解毒方对AngⅡ诱导的H9c2细胞NADPH氧化酶表达作用机制的研究",
        "start":408,
        "end":411
    },
    {
        "title":"益心解毒方对Nox2 和Nox4 亚基过表达的心肌细胞NADPH 氧化酶活性的影响",
        "start":412,
        "end":417
    },
    {
        "title":"益心解毒方对NOX2 亚基和NOX4 亚基过表达及小干扰RNA 引起的心肌细胞还原型辅酶Ⅱ氧化酶活性变化的机制研究",
        "start":418,
        "end":422
    },
    {
        "title":"益心解毒方对大鼠心肌细胞内活性氧水平及信号转导通路的影响",
        "start":423,
        "end":426
    },
    {
        "title":"益心解毒方对气虚血瘀证心力衰竭大鼠心肌组织中NOX2和NOX4的影响",
        "start":427,
        "end":430
    },
    {
        "title":"益心解毒方对气虚血瘀证心衰大鼠心肌组织中血小板—内皮细胞黏附分子和血管内皮生长因子表达的影响研究",
        "start":431,
        "end":435
    },
    {
        "title":"益心解毒方对心梗后心衰大鼠心肌保护作用的实验研究",
        "start":436,
        "end":439
    },
    {
        "title":"益心解毒方对心力衰竭气虚血瘀证大鼠血流动力学影响的实验研究",
        "start":440,
        "end":446
    },
    {
        "title":"益心解毒方改善心梗后心衰大鼠心功能的作用研究",
        "start":447,
        "end":450
    },
    {
        "title":"益心解毒方抑制H9C2 心肌细胞凋亡的作用机制",
        "start":451,
        "end":456
    }
]

if __name__ == "__main__":
    split_pdf_by_ranges("./pdfs/芪参颗粒研究文章合集.pdf",ranges,"./pdfs")