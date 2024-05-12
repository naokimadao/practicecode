
function updatefetchRecord() {
    var recordId = document.getElementById('recordIdToUpdate').value;
    if (!recordId) {
        alert("IDが入力されておらず、検索できません。");
        return;
    }

    fetch(`/get-record?id=${recordId}`)
    .then(response => {
        if (!response.ok) {
            throw new Error('対象のレコードがありません。');
        }
        return response.json();
    })
    .then(data => {
        document.getElementById('recordIdDisplay').textContent = data.id;
        document.getElementById('timestampDisplay').textContent = data.timestamp;
        document.getElementById('dataDisplay').textContent = data.data;
    })
    .catch(error => {
        console.error('エラー:', error);
        alert("エラー: " + error.message);
        document.getElementById('recordIdDisplay').textContent = '';
        document.getElementById('dataDisplay').textContent = '';
        document.getElementById('newData').value = ''; // 入力フィールドをクリア
    });
    }
   