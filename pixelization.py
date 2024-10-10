import matplotlib.pyplot as plt # 이미지 출력 모듈
from matplotlib.patches import Rectangle 
from PIL import Image # 이미지 처리. 픽셀 불러와서 rgb 값을 뽑고 넣는 모듈
import numpy as np

# 픽셀 크기
m_size = 5

# 클릭한 색상을 저장할 리스트
selected_colors = []
output_path = './img/new_pixel.png'

# 이미지 열기
image_path = './img/pika2.png'  # 이미지 경로를 입력
img = Image.open(image_path).convert("RGB")
img_array = np.array(img)

# 추출할 색상 개수를 설정
num_colors_to_extract = int(input("추출할 색상 개수를 입력하세요: "))

# 색상 추출 함수
def color_extract(event):
    if len(selected_colors) < num_colors_to_extract:  # 선택한 색상이 아직 부족하면
        x, y = int(event.xdata), int(event.ydata)     # 클릭한 좌표 가져오기
        color = img_array[y, x]                   # 클릭한 좌표의 RGB 색상 추출
        # color = img_array[y, x][:3] # alpha 값 제외
        color = tuple(map(int, color))                # numpy 값을 일반 int로 변환
        selected_colors.append(color)                 # 리스트에 (R, G, B) 튜플로 추가
        print(f"클릭한 위치: ({x}, {y}), 색상: {color}")
        
        # 색상 사각형 표시
        rect = Rectangle((0, -len(selected_colors)*0.1), 0.2, 0.1, color=np.array(color)/255)  # RGB 색상을 [0, 1] 범위로 변환
        ax_color.add_patch(rect)
        fig.canvas.draw()

    if len(selected_colors) == num_colors_to_extract:
        print(f"추출된 색상: {selected_colors}")
        plt.close()  # 색상이 모두 추출되면 창 닫기

# 이미지를 띄우고 클릭 이벤트 등록
fig, (ax_img, ax_color) = plt.subplots(2, 1, figsize=(6, 8))
ax_img.imshow(img_array)
ax_img.set_title("Click on the image to extract colors")
ax_img.axis("off")

ax_color.set_xlim(0, 1)
ax_color.set_ylim(-num_colors_to_extract * 0.1, 0)
ax_color.axis("off")  # 색상 보여주는 영역의 축 숨김

fig.canvas.mpl_connect('button_press_event', color_extract) # 클릭 이벤트 등록

# 화면에 이미지 보여주기
plt.show()

print(selected_colors)

# 픽셀 크기에 나누어 떨어지도록 이미지 확장
x_m = img.size[0] % m_size
y_m = img.size[1] % m_size

x_p = m_size - x_m # x padding
y_p = m_size - y_m

img_new = Image.new(img.mode, (img.size[0]+x_p, img.size[1]+y_p), (0,0,0)) # rgb 모드, 이미지 사이즈, 어떤 색으로 채울 것인지

img_new.paste(img, (0,0)) # img 이미지를 (0,0) 위치 기준으로 맞춰서 img_new에 붙여넣음

img = img_new

#선택한 색상을 기준으로 이미지에 픽셀화 적용
for i in range(0, img.size[0], m_size):
  for j in range(0, img.size[1], m_size):
    r_sum = 0
    g_sum = 0
    b_sum = 0

    # 각 블록 내에서 RGB 평균 계산
    for ii in range(i,i+m_size):
      for jj in range(j, j+m_size):
        rgb = img.getpixel((ii, jj))
        r_sum += rgb[0]
        g_sum += rgb[1]
        b_sum += rgb[2]

    r_a = round(r_sum/m_size**2)
    g_a = round(g_sum/m_size**2)
    b_a = round(b_sum/m_size**2)

    # 선택된 색상 중 가장 가까운 색상 찾기
    rgb_point = []

    for c in selected_colors:
      rgb_point.append(abs(r_a-c[0]) + abs(g_a-c[1]) + abs(b_a-c[2]))
    
    min_rgb = min(rgb_point)
    min_rgb_idx = rgb_point.index(min_rgb)

    r_f, g_f, b_f = selected_colors[min_rgb_idx]

    # 픽셀 값 적용
    for ii in range(i,i+m_size):
      for jj in range(j, j+m_size):
        img.putpixel((ii,jj), (r_f,g_f,b_f))


# plt.imshow(img)
# plt.show()

# 결과 이미지 저장
img.save(output_path)