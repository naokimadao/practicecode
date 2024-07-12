// deleteCookies.js
function deleteAllCookies() {
    var cookies = ['username'];  // 削除したいクッキー名をここで指定

    for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i];
        document.cookie = cookie + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/index.html";　//即削除「過去日付を設定することでhtml内で過去cookieと判断して即削除」
    }

    // クッキー削除後にページをリロード
    window.location.reload();
}