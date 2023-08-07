# -*- coding: utf-8 -*-

# # 필요한 라이브러리를 불러옵니다.
import qrcode
from qrcode.image.pil import PilImage

# QR 코드 생성기를 초기화합니다.
# version=1은 QR 코드의 버전을 나타냅니다. 1은 가장 작은 크기의 QR 코드를 의미합니다.
# error_correction는 QR 코드의 오류 수정 수준을 설정합니다. ERROR_CORRECT_L은 가장 낮은 수준입니다.
# box_size는 QR 코드의 각 박스의 픽셀 크기를 설정합니다.
# border는 QR 코드 주변의 테두리 크기를 설정합니다.
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    image_factory=PilImage
)

# QR 코드에 데이터를 추가합니다. 여기서는 웹 사이트 링크를 추가합니다.
qr.add_data('https://cgweb.kr')

# QR 코드를 최종적으로 생성합니다.
qr.make(fit=True)

# QR 코드 이미지를 생성하고, 색상을 설정합니다.
# fill_color는 QR 코드의 색상을, back_color는 배경색을 설정합니다.
img = qr.make_image(fill_color="green", back_color="white")

# QR 코드 이미지를 파일로 저장합니다.
img.save('cgweb_qrcode.png')
