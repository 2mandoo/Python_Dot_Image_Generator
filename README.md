# 이미지 색상 추출 및 픽셀화 도구 🎨
![Python](https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=fff)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=flat&logo=Matplotlib&logoColor=black)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=flat&logo=numpy&logoColor=white)

 이미지를 불러와 특정 색상을 선택하고, 선택한 색상들을 이용해 이미지를 픽셀화하는 Python 기반 도구입니다. 
 
 이미지를 간소화하면서도 중요한 시각적 요소를 유지할 수 있습니다.
 
#### 주요 기능
- 색상 추출: 이미지에서 원하는 색상을 클릭하여 선택하여 원하는 색상(RGB)을 추출.
- 맞춤형 픽셀화: 각 블록의 평균 색상을 계산하고, 선택한 색상 중 가장 가까운 색상으로 매핑하여 이미지를 픽셀화.
- 동적 블록 크기: 픽셀 블록 크기를 조정하여 다양한 세부 수준 제공.
- 이미지 처리: Python의 Matplotlib, NumPy, PIL 라이브러리를 활용한 효율적인 이미지 처리.
- 결과 저장: 처리된 이미지를 지정된 경로에 새 파일로 저장.


#### 사용 방법
- m_size 변수 값을 조정하여 픽셀화 블록 크기를 변경할 수 있습니다.
- 이미지를 클릭하여 원하는 색상을 선택하세요.
- 처리된 이미지는 화면에 표시되고 지정된 경로에 저장됩니다.
