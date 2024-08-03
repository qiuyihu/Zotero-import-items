# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 11:56:26 2024

@author: Ivo Chiu
"""

info ="""
standard_number	standard_name	url	release_time	surname
WS 445.1-2014	电子病历基本数据集 第1部分：病历概要	http://www.nhc.gov.cn/wjw/s9497/201406/e75425e4f720443fba37907f5bd7c326.shtml	2014/5/30	中华人民共和国国家卫生和计划生育委员会
WS 445.2-2014	电子病历基本数据集 第2部分：门（急）诊病历	http://www.nhc.gov.cn/wjw/s9497/201406/ca86202bf9ae46c0ad4b25d26d2f2375.shtml	2014/5/30	中华人民共和国国家卫生和计划生育委员会
WS 445.3-2014	电子病历基本数据集 第3部分：门（急）诊处方	http://www.nhc.gov.cn/wjw/s9497/201406/ef71425ac89d489180541ba6e751498b.shtml	2014/5/30	中华人民共和国国家卫生和计划生育委员会
WS 445.4-2014	电子病历基本数据集 第4部分：检查检验记录	http://www.nhc.gov.cn/wjw/s9497/201406/e467bd81e1014516861a11e7bae49929.shtml	2014/5/30	中华人民共和国国家卫生和计划生育委员会
WS 445.5-2014	电子病历基本数据集 第5部分：一般治疗处置记录	http://www.nhc.gov.cn/wjw/s9497/201406/15349b9e45ff4aabac990fdd86332029.shtml	2014/5/30	中华人民共和国国家卫生和计划生育委员会
WS 445.6-2014	电子病历基本数据集 第6部分：助产记录	http://www.nhc.gov.cn/wjw/s9497/201406/d81cab62423e4e57bac6e064bacf289a.shtml	2014/5/30	中华人民共和国国家卫生和计划生育委员会
WS 445.7-2014	电子病历基本数据集 第7部分：护理操作记录	http://www.nhc.gov.cn/wjw/s9497/201406/5ee7bb656f5f47da8f619daf2c8a4fb8.shtml	2014/5/30	中华人民共和国国家卫生和计划生育委员会
WS 445.8-2014	电子病历基本数据集 第8部分：护理评估与计划	http://www.nhc.gov.cn/wjw/s9497/201406/ad82b6e9f2be443dacc67ae3318ab076.shtml	2014/5/30	中华人民共和国国家卫生和计划生育委员会
WS 445.9-2014	电子病历基本数据集 第9部分：知情告知信息	http://www.nhc.gov.cn/wjw/s9497/201406/3ca2537980c2467f8b4dc0c69c2b48e7.shtml	2014/5/30	中华人民共和国国家卫生和计划生育委员会
WS 445.10-2014	电子病历基本数据集 第10部分：住院病案首页	http://www.nhc.gov.cn/wjw/s9497/201406/d71e897955b24cefb9ef903ab6d7f680.shtml	2014/5/30	中华人民共和国国家卫生和计划生育委员会
WS 445.11-2014	电子病历基本数据集 第11部分：中医住院病案首页	http://www.nhc.gov.cn/wjw/s9497/201406/7ab31d6da6cb4833848c3586904d4a70.shtml	2014/5/30	中华人民共和国国家卫生和计划生育委员会
WS 445.12-2014	电子病历基本数据集 第12部分：入院记录	http://www.nhc.gov.cn/wjw/s9497/201406/64940eb79803460aa147d0c14c5074af.shtml	2014/5/30	中华人民共和国国家卫生和计划生育委员会
WS 445.13-2014	电子病历基本数据集 第13部分：住院病程记录	http://www.nhc.gov.cn/wjw/s9497/201406/99c6652dd1c34f6cb3543b6f1b734a97.shtml	2014/5/30	中华人民共和国国家卫生和计划生育委员会
WS 445.14-2014	电子病历基本数据集 第14部分：住院医嘱	http://www.nhc.gov.cn/wjw/s9497/201406/5b40ad9037f64410ad10974f50d6e2bb.shtml	2014/5/30	中华人民共和国国家卫生和计划生育委员会
WS 445.15-2014	电子病历基本数据集 第15部分：出院小结	http://www.nhc.gov.cn/wjw/s9497/201406/4a5b133c07a54e2889d84bb7cf4808cc.shtml	2014/5/30	中华人民共和国国家卫生和计划生育委员会
WS 445.16-2014	电子病历基本数据集 第16部分：转诊（院）记录	http://www.nhc.gov.cn/wjw/s9497/201406/7c52ce7319bb4bea9d4b4aaf5680bf7b.shtml	2014/5/30	中华人民共和国国家卫生和计划生育委员会
WS 445.17-2014	电子病历基本数据集 第17部分：医疗机构信息	http://www.nhc.gov.cn/wjw/s9497/201406/155687fce1034dd78789e55dc9bbd11b.shtml	2014/5/30	中华人民共和国国家卫生和计划生育委员会
"""
info = info.split("\n")

items = []
for  lines in info[2:-1]:
    line = lines.split("\t")
    items.append({"url": line[2], "standard_name": line[1], "release_time": line[3], "standard_number": line[0], "surname": line[4]})

rdf_description_template = """
    <rdf:Description rdf:about="{url}">
        <z:itemType>standard</z:itemType>
        <bib:authors>
            <rdf:Seq>
                <rdf:li>
                    <foaf:Person>
                       <foaf:surname>{surname}</foaf:surname>
                    </foaf:Person>
                </rdf:li>
            </rdf:Seq>
        </bib:authors>
        <dc:subject>
           <z:AutomaticTag><rdf:value>/unread</rdf:value></z:AutomaticTag>
        </dc:subject>
        <dc:title>{standard_name}</dc:title>
        <dc:date>{release_time}</dc:date>
        <z:language>zh-CN</z:language>
        <dc:identifier>
            <dcterms:URI>
                <rdf:value>{url}</rdf:value>
            </dcterms:URI>
        </dc:identifier>
        <prism:number>{standard_number}</prism:number>
    </rdf:Description>"""

rdf_content = """<rdf:RDF
 xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
 xmlns:z="http://www.zotero.org/namespaces/export#"
 xmlns:bib="http://purl.org/net/biblio#"
 xmlns:foaf="http://xmlns.com/foaf/0.1/"
 xmlns:dc="http://purl.org/dc/elements/1.1/"
 xmlns:prism="http://prismstandard.org/namespaces/1.2/basic/">"""

for item in items:
    rdf_content += rdf_description_template.format(**item)

rdf_content +="""
</rdf:RDF>"""
print(rdf_content)