function login() {
    var name = document.getElementById('username').value;
    var pass = document.getElementById('password').value;

    if (!name || !pass) {
        alert("ユーザー名とパスワードを入力してください。");
        return;
    }

    fetch('/login', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({username: name, password: pass      
        })
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('認証に失敗しました。');
        }
    })
    .then(data => {
        if (data.status === 'success') {
            alert('ログイン成功');
            location.href = 'index.html'; // ログイン成功後のリダイレクト
        } else if (data.status === 'fail') {
            alert(data.message);
        }
    })
    .catch(error => {
        console.error('エラー:', error);
        alert("エラー: " + error.message);
    });
}
