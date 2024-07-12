document.addEventListener('DOMContentLoaded', function() {
    var urlParams = new URLSearchParams(window.location.search);
    var authCode = urlParams.get('code');
    var authCodeElement = document.getElementById('auth-code');
    if (authCodeElement) {
        authCodeElement.textContent = authCode;
    }
});

function copyToClipboard() {
    var copyText = document.getElementById("auth-code");
    var textArea = document.createElement("textarea");
    textArea.value = copyText.textContent;
    document.body.appendChild(textArea);
    textArea.select();
    document.execCommand("Copy");
    textArea.remove();
    alert("認証コードがコピーされました！");
}
