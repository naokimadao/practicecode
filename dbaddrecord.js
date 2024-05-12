function addRecordToDB() {
    var now = new Date();
    var dataInput = document.getElementById('dataInput').value.trim();
    var nameInput = document.getElementById('nameInput').value.trim();
    var passInput = document.getElementById('passInput').value.trim();

    if (!dataInput || !nameInput || !passInput) {
        alert("全てのフィールドに入力してください。");
        return;
    }

    // 日付と時刻のフォーマット
    var formattedDate = now.getFullYear() + '-' +
                        ('0' + (now.getMonth() + 1)).slice(-2) + '-' +
                        ('0' + now.getDate()).slice(-2) + ' ' +
                        ('0' + now.getHours()).slice(-2) + ':' +
                        ('0' + now.getMinutes()).slice(-2) + ':' +
                        ('0' + now.getSeconds()).slice(-2);

    var data = { 
        timestamp: formattedDate, 
        data: dataInput,
        name: nameInput,
        pass: passInput
    };

    fetch('/add-record', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        }
        throw new Error('Network response was not ok.');
    })
    .then(result => {
        alert('新しいレコードの追加に成功しました。');
        document.getElementById('dataInput').value = ''; // 入力フィールドをクリア
        document.getElementById('nameInput').value = ''; // 入力フィールドをクリア
        document.getElementById('passInput').value = ''; // 入力フィールドをクリア
    })
    .catch(error => {
        console.error('エラー:', error);
        alert("エラー: " + error.message);
    });
}
