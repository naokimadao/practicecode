
function fetchRecord() {
    var recordId = document.getElementById('recordId').value;//入力ないの値を取得してデータに代入、まだこの時点ではjsファイル内でのデータ作成JSONファイルとはなっていない。
    if (!recordId) {//もし入力がない場合のアラート分岐
        alert("IDが入力されておらず、検索できません。");
        return;
    }

    fetch(`/get-record?id=${recordId}`)// GETメソッドでserver.pyにリクエストを送信「record=??の値の参照お願いしますと言っている。」
    .then(response => {
        if (response.ok) {
            return response.json();//ここが正常にレスポンスを返す場所
        } else {
            throw new Error('対象のレコードがありません。');
        }
    })
    .then(data => {
        document.getElementById('recordIdDisplay').textContent = data.id;
        document.getElementById('timestampDisplay').textContent = data.timestamp;
        document.getElementById('dataDisplay').textContent = data.data;
        document.getElementById('nameDisplay').textContent = data.name;
        document.getElementById('passDisplay').textContent = data.pass;
        document.getElementById('recordId').value = ''; // 入力フィールドをクリア
    })
    .catch(error => {
        console.error('エラー:', error);
        alert("エラー: " + error.message);
        document.getElementById('recordIdDisplay').textContent = '';
        document.getElementById('timestampDisplay').textContent = '';
        document.getElementById('dataDisplay').textContent = '';
        document.getElementById('nameDisplay').textContent = '';
        document.getElementById('passDisplay').textContent = '';
    });
}
