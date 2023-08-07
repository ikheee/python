# 필요한 라이브러리를 불러옵니다.
import easyocr

# OCR reader를 초기화합니다. 여기서는 영어(en) 텍스트를 읽을 것이므로 ['en']을 인자로 전달합니다.
# gpu=False로 설정하여 GPU를 사용하지 않도록 합니다. 만약 GPU를 사용할 수 있는 환경이라면 gpu=True로 설정하면 속도가 향상됩니다.
reader = easyocr.Reader(['en'], gpu=False)

# readtext 메서드를 사용하여 이미지에서 텍스트를 읽습니다. 이 메서드는 이미지 파일의 경로를 인자로 받습니다.
# 이 메서드는 이미지 내의 모든 텍스트 영역을 찾아내고, 각 영역의 경계 상자와 그 안의 텍스트를 반환합니다.
result = reader.readtext('ocr_org.png')

# 결과를 출력합니다.
print(result)

