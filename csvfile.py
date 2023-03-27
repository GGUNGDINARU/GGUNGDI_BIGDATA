import csv

# CSV 파일에 저장할 데이터
data = [
    ['Name', 'Age', 'Gender'],
    ['John', 25, 'Male'],
    ['Jane', 30, 'Female'],
    ['Bob', 20, 'Male']
]

# CSV 파일 열기
with open('data.csv', 'w', newline='') as file:

    # create a CSV writer object
    writer = csv.writer(file)

    # 데이터 쓰기
    for row in data:
        writer.writerow(row)

print("CSV 파일 쓰기 완료")