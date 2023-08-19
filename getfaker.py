# Faker 라이브러리를 불러옵니다.
from faker import Faker

# # Faker 객체를 생성합니다.
# fake = Faker()

# 한글 데이터를 생성하기 위해 Faker 객체를 'ko_KR' 로케일로 생성합니다.
fake = Faker('ko_KR')

# 10명의 가짜 데이터를 생성하는 함수를 정의합니다.
def generate_fake_data(num=10):
    data = []  # 데이터를 저장할 빈 리스트를 생성합니다.
    
    for _ in range(num):  # num 횟수만큼 반복합니다.
        name = fake.name()  # 임의의 이름을 생성합니다.
        age = fake.random_int(min=20, max=80)  # 20에서 80 사이의 임의의 나이를 생성합니다.
        address = fake.address()  # 임의의 주소를 생성합니다.
        
        data.append({
            'name': name,
            'age': age,
            'address': address
        })  # 생성된 데이터를 리스트에 추가합니다.
    
    return data  # 생성된 데이터 리스트를 반환합니다.

# 함수를 호출하여 결과를 출력합니다.
for person in generate_fake_data():
    print(person)
