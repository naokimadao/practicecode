document.addEventListener('DOMContentLoaded', function() {
    // サーバーから勤怠情報を取得する関数
    function fetchAttendanceData() {
        fetch('/api/getAttendanceData')
            .then(response => response.json())
            .then(data => displayData(data))
            .catch(error => console.error('Error:', error));
    }

    // JSONデータを表示する関数
    function displayData(data) {
        const container = document.getElementById('data-container');
        container.innerHTML = '';

        data.forEach(item => {
            const div = document.createElement('div');
            div.className = 'data-item';
            div.innerHTML = `
                <p>日付: ${item.date}</p>
                <p>状態: ${item.status}</p>
                <p>開始時間: ${item.startTime}</p>
                <p>終了時間: ${item.endTime}</p>
                <p>休憩時間: ${item.breakTime}</p>
            `;
            container.appendChild(div);
        });
    }

    // データ取得を初期化
    fetchAttendanceData();
});
