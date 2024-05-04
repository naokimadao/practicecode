document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('deleteRecord').addEventListener('click', function(event) {
    event.preventDefault(); // デフォルトのフォーム送信を防ぐ
    deleteRecordById();
});

    updateTime();
    document.getElementById('refreshTime').addEventListener('click', refreshTime);
    document.getElementById('recordForm').addEventListener('submit', function(event) {
        event.preventDefault();
        addRecordToDB();
    });
});

function updateTime() {
    var now = new Date();
    var timeElement = document.getElementById("time");
    timeElement.textContent = now.toLocaleString();
}

function refreshTime() {
    updateTime();
}

function addRecordToDB() {
    var now = new Date();
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/add-record", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onload = function() {
        if (xhr.status === 200) {
            var recordArea = document.getElementById("recordArea");
            var recordText = "記録: " + now.toLocaleString();
            var recordParagraph = document.createElement("p");
            recordParagraph.textContent = recordText;
            recordArea.appendChild(recordParagraph);
        } else {
            console.error("サーバーエラー:", xhr.statusText);
        }
    };
    xhr.onerror = function () {
        console.error("リクエストエラー");
    };
    xhr.send(JSON.stringify({timestamp: now.toJSON()}));
}
function deleteRecordById() {
    var recordId = document.getElementById('recordId').value;
    if (!recordId) {
        alert('IDを入力してください。');
        return;
    }
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/delete-record", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onload = function() {
        if (xhr.status === 200) {
            console.log("データが削除されました: ID " + recordId);
            alert("データが削除されました: ID " + recordId); // ユーザーにアラートを表示
            document.getElementById('recordId').value = ''; // 入力フィールドをクリア
        } else {
            console.error("サーバーエラー: ", xhr.statusText);
        }
    };
    xhr.onerror = function() {
        console.error("リクエストエラー");
    };
    xhr.send(JSON.stringify({id: recordId}));
}
