function deleteAllRecords() {
    if (!confirm("本当に全てのレコードを削除しますか？")) {
        return;
    }

    fetch('/delete-all-records', {
        method: 'DELETE',
        headers: {'Content-Type': 'application/json'}
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        }
        throw new Error('Network response was not ok.');
    })
    .then(result => {
        alert('全てのレコードを削除しました。');
        document.getElementById('recordsContent').innerHTML = ''; // 表示をクリア
        document.getElementById('allRecordsBox').style.display = 'none';
    })
    .catch(error => {
        console.error('エラー:', error);
        alert("エラー: " + error.message);
    });
}