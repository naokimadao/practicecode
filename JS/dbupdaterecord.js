
function updateRecordById() {
    var recordId = document.getElementById('recordIdToUpdate').value;
    var newData = document.getElementById('newDataInput').value;

    if (!recordId || !newData) {
        alert("IDと新しいデータの両方を入力してください。");

        return;
    }

    fetch('/update-record', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({id: recordId, data: newData})
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(data => { throw new Error(data.message) });
        }
        return response.json();
    })
    .then(result => {
        alert(result.message || 'レコードの変更に成功しました。');
        document.getElementById('newDataInput').value = ''; // 入力フィールドをクリア
        document.getElementById('recordIdToUpdate').value = ''; // 入力フィールドをクリア
    })
    .catch(error => {
        console.error('エラー:', error);
        alert("エラー: " + error.message);
    });
}
