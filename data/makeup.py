import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist

# 1. MNIST 데이터셋 수집
(X_train, y_train), (X_test, y_test) = mnist.load_data()

print("MNIST 데이터 수집 완료!")

# 2. 데이터 크기 확인
print("\n[데이터 크기 확인]")
print("X_train:", X_train.shape)
print("y_train:", y_train.shape)
print("X_test:", X_test.shape)
print("y_test:", y_test.shape)

# 3. 이미지 데이터를 784개 픽셀로 변환
X_train_flat = X_train.reshape(60000, 784)
X_test_flat = X_test.reshape(10000, 784)

# 4. Pandas DataFrame으로 변환
train_df = pd.DataFrame(X_train_flat)
test_df = pd.DataFrame(X_test_flat)

# 정답 데이터 추가
train_df["label"] = y_train
test_df["label"] = y_test

print("\n[데이터 확인]")
print(train_df.head())

# 5. 데이터 전처리 (픽셀값 정규화)
pixel_columns = train_df.columns[:-1]

train_df[pixel_columns] = (
    train_df[pixel_columns].astype("float32") / 255.0
)

test_df[pixel_columns] = (
    test_df[pixel_columns].astype("float32") / 255.0
)

print("\n데이터 전처리 완료!")

# 6. 숫자별 데이터 개수 분석
print("\n[숫자별 데이터 개수]")
number_counts = train_df["label"].value_counts().sort_index()
print(number_counts)

# 7. 숫자별 데이터 분포 시각화
number_counts.plot(kind="bar")

plt.title("MNIST Number Distribution")
plt.xlabel("Number")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 8. 전처리 결과 확인
print("\n[최종 데이터 형태]")
print("학습 데이터:", train_df.shape)
print("테스트 데이터:", test_df.shape)

print("\n모든 데이터 처리 완료!")
