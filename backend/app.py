from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import numpy as np

app = Flask(__name__)
CORS(app)


def preprocess_image(file):
    image = Image.open(file).convert("L")
    image = image.resize((28, 28))

    image = np.array(image)
    image = image.astype("float32") / 255.0

    image = image.reshape(1, 28, 28, 1)

    return image


@app.route("/predict", methods=["POST"])
def predict():

    if "image" not in request.files:
        return jsonify({
            "error": "이미지 파일이 없습니다."
        }), 400

    file = request.files["image"]

    if file.filename == "":
        return jsonify({
            "error": "이미지가 선택되지 않았습니다."
        }), 400

    try:
        image = preprocess_image(file)

        # AI 모델 예측 부분
        # prediction = model.predict(image)
        # predicted_digit = int(np.argmax(prediction))

        # 모델 연결 전 테스트용
        predicted_digit = 0

        return jsonify({
            "prediction": predicted_digit
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)