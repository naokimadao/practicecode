
// 全てのレコードを表示する関数
function showAllRecords() {
    fetch('/get-all-records', {
        method: 'GET',
        headers: {'Content-Type': 'application/json'}
    })
    .then(response => response.json())
    .then(records => {
        const recordsContent = document.getElementById('recordsContent');
        recordsContent.innerHTML = ''; // 既存の内容をクリア

        records.forEach(record => {
            const recordElement = document.createElement('div');
            recordElement.classList.add('record-box');
            recordElement.innerHTML = `<strong>ID:</strong> ${record.id} <br>
                                       <strong>Timestamp:</strong> ${record.timestamp} <br>
                                       <strong>Data:</strong> ${record.data} <br>
                                       <strong>Name:</strong> ${record.name} <br>
                                       <strong>Pass:</strong> ${record.pass}`;
            recordsContent.appendChild(recordElement);
        });

        document.getElementById('allRecordsBox').style.display = 'block';
    })
    .catch(error => {
        console.error('エラー:', error);
        alert("エラー: " + error.message);
    });
}