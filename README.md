# Zotero-import-items
用于构造向Zotero批量导入条目的RDF文件
## 标准文件（五字段）
1. 准备标准信息表格，该版本支持五个字段
   |标准号|标准名|url|发布时间|归口单位|
   |---|---|---|---|---|
   
   以**WS 445 -2014 电子病历基本数据集** 为例，在Excel准备好信息表格（字段顺序不要改变）
   ![image](https://github.com/user-attachments/assets/cbe58e36-bccb-45d5-a2d2-f727c80fcf61)
2. 直接连字段名一起粘贴进standard.py 'info'处
   ![image](https://github.com/user-attachments/assets/3519b3f3-6569-4777-b440-b5940c18f41d)
3. 运行，在变量查看器中复制'rdf_content'
   ![image](https://github.com/user-attachments/assets/f63709d7-55e4-4aeb-bd0a-e5366ea954d2)
4. 创建'导入的条目.rdf'，使用Zotero导入RDF文件
  ![ce6d24dd6bb596f4ce988bd836fd087](https://github.com/user-attachments/assets/14886fd7-26c3-4380-870b-c775cb17bbb4)

   
   
