// displayCookies.js

// 特定の名前のクッキーを取得する関数
function getCookie(name) {
    var matches = document.cookie.match(new RegExp(
        "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
    ));
    return matches ? decodeURIComponent(matches[1]) : undefined;
}

// クッキーをサーバーに送信する関数
function sendCookiesToServer() {
    var username = getCookie('username');
    if (!username) {
        alert('ユーザー名のクッキーが見つかりません。');
        return;
    }

    var dayRecords = {};
    for (let i = 1; i <= 32; i++) {
        let cookieName = `day${i}_record`;
        let cookieValue = getCookie(cookieName);
        if (cookieValue) {
            dayRecords[cookieName] = cookieValue;
        }
    }

    fetch('/saveDayRecords', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            username: username,
            records: dayRecords
        })
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('データベースへの保存に失敗しました。');
        }
    })
    .then(data => {
        if (data.status === 'success') {
            alert('クッキーのデータが保存されました。');
        } else {
            alert('保存に失敗しました: ' + data.message);
        }
    })
    .catch(error => {
        console.error('エラー:', error);
        alert('エラー: ' + error.message);
    });
}

// フォーム送信時に特定のクッキーを表示し、サーバーに送信する
document.getElementById('scheduleForm').addEventListener('submit', function(event) {
    event.preventDefault();
    sendCookiesToServer();
});
