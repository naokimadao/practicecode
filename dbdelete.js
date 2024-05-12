function deleteRecordById() {
    var recordId = document.getElementById('recordIdToDelete').value;
    if (!recordId) {
        alert('IDを入力してください。');
        return;
    }
    fetch(`/delete-record`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({id: recordId})
        
    })
    .then(response => response.json())
    .then(result => {
        alert('指定したレコードの削除に成功しました。');
        document.getElementById('recordIdToDelete').value = ''; // 入力フィールドをクリア
    })
    .catch(error => {
        console.error('エラー:', error);
        alert("エラー: " + error.message);
    });
}
