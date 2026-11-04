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

    // 분석 시작
    resultText.textContent = "분석을 시작합니다...";
    predictBtn.disabled = true;
    predictBtn.textContent = "분석 중...";

    // 임시 테스트 코드
    setTimeout(function () {

        predictBtn.disabled = false;
        predictBtn.textContent = "분석하기";

        resultText.textContent = "예측 결과 : 7";

    }, 2000);

});