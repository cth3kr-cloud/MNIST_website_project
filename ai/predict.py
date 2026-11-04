import numpy as np
"""
X_train
y_train
X_test
y_test
"""

# ==========================================
# 1. 신경망의 기본 설정
# ==========================================

input_size = 784
hidden_size = 128
output_size = 10

learning_rate = 0.01
batch_size = 100
epochs = 10


# ==========================================
# 2. 가중치와 편향 초기화
# ==========================================

# He Initialization
# ReLU를 사용하는 신경망에서 가중치를 적절한 크기로 초기화한다.

W1 = np.random.randn(input_size, hidden_size) * np.sqrt(2 / input_size)
b1 = np.zeros((1, hidden_size))

W2 = np.random.randn(hidden_size, output_size) * np.sqrt(2 / hidden_size)
b2 = np.zeros((1, output_size))


# ==========================================
# 3. 활성화 함수
# ==========================================

def relu(x):
    return np.maximum(0, x)


def softmax(x):
    # 각 행의 최댓값을 빼서 지수 계산의 수치적 안정성을 높인다.
    exp_x = np.exp(x - np.max(x, axis=1, keepdims=True))

    return exp_x / np.sum(exp_x, axis=1, keepdims=True)


# ==========================================
# 4. 순전파 (Forward Propagation)
# ==========================================

def forward(X):

    # 입력층 -> 은닉층
    z1 = X @ W1 + b1
    a1 = relu(z1)

    # 은닉층 -> 출력층
    z2 = a1 @ W2 + b2
    y_pred = softmax(z2)

    return z1, a1, z2, y_pred


# ==========================================
# 5. 손실 함수 (Cross Entropy)
# ==========================================

def cross_entropy(y_pred, Y):

    batch_size = Y.shape[0]

    # 정답에 해당하는 예측 확률만 선택한다.
    correct_probs = y_pred[np.arange(batch_size), Y]

    # log(0)을 방지하기 위해 아주 작은 값을 더한다.
    loss = -np.mean(np.log(correct_probs + 1e-8))

    return loss


# ==========================================
# 6. 역전파 (Backpropagation)
# ==========================================

def backward(X, Y, z1, a1, y_pred):

    batch_size = X.shape[0]

    # 정답값을 One-hot Encoding으로 변환
    Y_onehot = np.eye(output_size)[Y]

    # ------------------------------
    # 출력층의 gradient
    # ------------------------------

    dz2 = (y_pred - Y_onehot) / batch_size

    dW2 = a1.T @ dz2
    db2 = np.sum(dz2, axis=0, keepdims=True)

    # ------------------------------
    # 은닉층의 gradient
    # ------------------------------

    da1 = dz2 @ W2.T

    dz1 = da1 * (z1 > 0)

    dW1 = X.T @ dz1
    db1 = np.sum(dz1, axis=0, keepdims=True)

    return dW1, db1, dW2, db2


# ==========================================
# 7. 가중치와 편향 업데이트
# ==========================================

def update_parameters(dW1, db1, dW2, db2):

    global W1, b1, W2, b2

    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1

    W2 -= learning_rate * dW2
    b2 -= learning_rate * db2


# ==========================================
# 8. 예측 함수
# ==========================================

def predict(X):

    _, _, _, y_pred = forward(X)

    # 각 이미지에서 가장 높은 확률을 가진 숫자를 선택한다.
    return np.argmax(y_pred, axis=1)


# ==========================================
# 9. 정확도 측정
# ==========================================

def accuracy(X, Y):

    predictions = predict(X)

    return np.mean(predictions == Y)


# ==========================================
# 10. 신경망 학습
# ==========================================

for epoch in range(epochs):

    # 학습 데이터의 순서를 무작위로 섞는다.
    indices = np.random.permutation(X_train.shape[0])

    X_shuffled = X_train[indices]
    Y_shuffled = y_train[indices]

    total_loss = 0

    # 데이터를 batch_size개씩 나누어 학습한다.
    for start in range(0, X_train.shape[0], batch_size):

        end = start + batch_size

        X_batch = X_shuffled[start:end]
        Y_batch = Y_shuffled[start:end]

        # 순전파
        z1, a1, z2, y_pred = forward(X_batch)

        # 손실 계산
        loss = cross_entropy(y_pred, Y_batch)
        total_loss += loss * X_batch.shape[0]

        # 역전파
        dW1, db1, dW2, db2 = backward(
            X_batch, Y_batch, z1, a1, y_pred
        )

        # 파라미터 업데이트
        update_parameters(dW1, db1, dW2, db2)

    # 한 epoch의 평균 손실
    average_loss = total_loss / X_train.shape[0]

    # 학습 및 테스트 정확도
    train_acc = accuracy(X_train, y_train)
    test_acc = accuracy(X_test, y_test)

    print(
        f"Epoch {epoch + 1}/{epochs} | "
        f"Loss: {average_loss:.4f} | "
        f"Train Accuracy: {train_acc:.4f} | "
        f"Test Accuracy: {test_acc:.4f}"
    )


# ==========================================
# 11. 학습된 모델 저장
# ==========================================

np.savez(
    "mnist_model.npz",
    W1=W1,
    b1=b1,
    W2=W2,
    b2=b2
)

print("모델 저장 완료!")

