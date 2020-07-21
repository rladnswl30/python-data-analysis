print('\n---------------')
print('# 2.8 파일 처리 및 외부 라이브러리 활용')
print('## 2.8.1, 2.8.2 request로 이미지 파일 가져와서 보여준 후 다운로드 받기')
import requests

url = 'http://image.dongascience.com/Photo/2017/03/14900752352661.jpg'
r = requests.get(url, stream=True).raw # 이미지 다운로드

from PIL import Image
img = Image.open(r)
img.show()
img.save('/Users/user/Downloads/src.png')

print(img.get_format_mimetype)


print('\n---------------')
print('## 2.8.3 이미지 파일 복사')

BUF_SIZE = 1024
# 원본을 읽기모드로 열어서 sf 파일 객체 생성하고, 대상 이미지 파일을 쓰기 모드로 열어서 df 파일 객체 생성
with open('/Users/user/Downloads/src.png', 'rb') as sf, open('/Users/user/Downloads/dst.png', 'wb') as df:
    while True:
        data = sf.read(BUF_SIZE) # sf 파일 객체로부터 1024바이트씩 읽기
        if not data:
            break # 읽을 데이터가 없으면 빠져나온다
        df.write(data) # 읽어온 data를 df 파일 객체에 쓴다



print('\n---------------')
print('## 2.8.4 SHA-256으로 파일 복사 검증')

import hashlib

# 원본, 사본의 이미지 파일에 대한 해시 객체 생성
sha_src = hashlib.sha256()
sha_dst = hashlib.sha256()

# 원본, 사본 이미지를 바이너리 읽기 모드로 열어 파일 객체 생성
with open('/Users/user/Downloads/src.png', 'rb') as sf, open('/Users/user/Downloads/dst.png', 'rb') as df:
    # 파일 객체로부터 전체 내용을 읽어서 해시 객체를 업데이트한다
    sha_src.update(sf.read())
    sha_dst.update(df.read())

# 해시 객체를 16진수로 출력
print("src.png's hash : {}".format(sha_src.hexdigest()))
print("dsc.png's hash : {}".format(sha_dst.hexdigest()))



print('\n---------------')
print('## 2.8.5 맷플롯립으로 이미지 가공하기')

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# 3차원 부동소수점 데이터
dst_img = mpimg.imread('/Users/user/Downloads/dst.png')
print('3차원 : ', dst_img)

# RGB 채널 중 첫 번째 채널만 슬라이싱해서 저장... 부동 소수점 데이터가 2차원으로 변경
pseudo_img = dst_img [:, :, 0]
print('2차원 : ', pseudo_img)

plt.suptitle('Image Processing', fontsize=17)
plt.subplot(1,2,1) # 1행 2열 중 1행 생성
plt.title('Original Image')
plt.imshow(mpimg.imread('/Users/user/Downloads/src.png'))

plt.subplot(1,2,2)
plt.title('Pseudocolor Image')
dst_img = mpimg.imread('/Users/user/Downloads/dst.png')
pseudo_img = dst_img [:, :, 0]
plt.imshow(pseudo_img)
plt.show()