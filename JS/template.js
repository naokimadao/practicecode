document.addEventListener('DOMContentLoaded', function() {
    const ctaButton = document.querySelector('.cta-button');
    window.addEventListener('scroll', function() {
        // ここでスクロール位置に基づいた動作を定義できます
        // 例: スクロールに応じて透明度を変更する
        const opacity = Math.max(0, 1 - window.scrollY / 350);
        ctaButton.style.opacity = opacity;
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const navLinks = document.querySelectorAll('nav ul li a'); // ナビゲーションバー内のリンクを選択
    window.addEventListener('scroll', function() {
        const scrollY = window.pageYOffset || document.documentElement.scrollTop;
        const maxOpacity = 1; // 最大透明度
        const fadeStart = 100; // フェードアウト開始のスクロール位置
        const fadeUntil = 500; // フェードアウト完了のスクロール位置

        let opacity = maxOpacity;
        if (scrollY > fadeStart) {
            opacity = Math.max(0, maxOpacity - ((scrollY - fadeStart) / (fadeUntil - fadeStart)) * maxOpacity);
        }

        navLinks.forEach(link => {
            link.style.opacity = opacity;
        });
    });
});



document.addEventListener('DOMContentLoaded', function() {
    const headerNav = document.querySelector('header nav');
    window.addEventListener('scroll', function() {
        const opacity = Math.max(0, 1 - window.pageYOffset / 400);
        headerNav.style.opacity = opacity;
    });
});