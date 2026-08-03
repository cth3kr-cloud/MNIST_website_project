// HTML 요소 가져오기
const imageInput = document.getElementById("imageInput");
const predictBtn = document.getElementById("predictBtn");
const previewImage = document.getElementById("previewImage");
const resultText = document.getElementById("resultText");

// 이미지 선택 시 미리보기
imageInput.addEventListener("change", function () {

    const file = imageInput.files[0];

    if (file) {
        previewImage.src = URL.createObjectURL(file);
        previewImage.style.display = "block";
    }

});

// 분석 버튼 클릭
predictBtn.addEventListener("click", function () {

    // 파일 선택 여부 확인
    if (!imageInput.files[0]) {
        resultText.textContent = "먼저 이미지를 선택하세요.";
        return;
    }

    // 분석 시작
    resultText.textContent = "분석을 시작합니다...";
    predictBtn.disabled = true;
    predictBtn.textContent = "분석 중...";

    // 2초 후 결과 표시
    setTimeout(function () {

        predictBtn.disabled = false;
        predictBtn.textContent = "분석하기";

        resultText.textContent = "예측 결과 : 7";

    }, 2000);

});