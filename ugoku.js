document.addEventListener('DOMContentLoaded', function() {
    updateTime();
    setInterval(updateTime, 1000); // 毎秒ごとに時刻を更新
});

function updateTime() {
    var now = new Date();
    var timeElement = document.getElementById("time");
    timeElement.textContent = now.toLocaleString(); // ローカルの日時フォーマットで表示
}

