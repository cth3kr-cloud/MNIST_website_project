// HTML 요소 가져오기
const imageInput = document.getElementById("imageInput");
const predictBtn = document.getElementById("predictBtn");
const previewImage = document.getElementById("previewImage");
const resultText = document.getElementById("resultText");

// 현재 미리보기 이미지의 URL 저장
let previewURL = null;

// 이미지 선택 시 미리보기
imageInput.addEventListener("change", function () {

    const file = imageInput.files[0];

    // 이전 미리보기 URL 정리
    if (previewURL) {
        URL.revokeObjectURL(previewURL);
        previewURL = null;
    }

    // 이미지 선택을 취소한 경우
    if (!file) {
        previewImage.src = "";
        previewImage.style.display = "none";
        resultText.textContent = "이미지를 선택하세요.";
        return;
    }

    // 이미지 파일 형식 검사
    if (!file.type.startsWith("image/")) {
        imageInput.value = "";

        previewImage.src = "";
        previewImage.style.display = "none";

        resultText.textContent = "이미지 파일만 업로드할 수 있습니다.";
        return;
    }

    // 이전 예측 결과 초기화
    resultText.textContent = "이미지가 선택되었습니다.";

    // 새로운 이미지 미리보기
    previewURL = URL.createObjectURL(file);

    previewImage.src = previewURL;
    previewImage.style.display = "block";

});

// 분석 버튼 클릭
predictBtn.addEventListener("click", function () {

    // 파일 선택 여부 확인
    if (!imageInput.files[0]) {
        resultText.textContent = "먼저 이미지를 선택하세요.";
        return;
    }

    // 이미지 파일 가져오기
    const file = imageInput.files[0];

    // 서버에 전송할 데이터 만들기
    const formData = new FormData();
    formData.append("image", file);
    // 분석 시작
    resultText.textContent = "분석을 시작합니다...";
    predictBtn.disabled = true;
    predictBtn.textContent = "분석 중...";
    // Flask 서버에 이미지 전송
    fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        body: formData
    })
    .then(function (response) {
        if (!response.ok) {
            throw new Error("서버에서 오류가 발생했습니다.");
        }

        return response.json();
    })
    .then(function (data) {
        resultText.textContent = "예측 결과 : " + data.prediction;
    })
    .catch(function (error) {
        resultText.textContent = "오류가 발생했습니다: " + error.message;
        console.error(error);
    })
    .finally(function () {
        predictBtn.disabled = false;
        predictBtn.textContent = "분석하기";
    });


});