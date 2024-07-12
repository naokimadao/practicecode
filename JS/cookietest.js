
//ログインクッキー生成
function cookie(name)
{
    var value = document.getElementById("username").value;
    document.cookie = name + "=" + (value || Null) + "; path=/";
}

