document.addEventListener('DOMContentLoaded', function() {
    const gridContainer = document.querySelector('.month-grid');
    if (!gridContainer) {
        console.error('Grid container not found.');
        return;
    }

    const year = 2024; // 年を指定
    const month = 4; // 月を指定（JavaScriptでは0が1月を表すので、4は5月）

    const holidays = {
        3: '憲法記念日',
        4: 'みどりの日',
        5: 'こどもの日',
        6: '祝日',
    };

    const monthStartDay = new Date(year, month, 1).getDay(); // その月の1日の曜日
    const daysInMonth = new Date(year, month + 1, 0).getDate(); // その月の日数
    const daysInPreviousMonth = new Date(year, month, 0).getDate(); // 前月の日数

    // 前月の最終日付を配置
    for (let i = monthStartDay - 1; i >= 0; i--) {
        const dayBox = document.createElement('div');
        dayBox.className = 'day-box previous-month';
        const day = daysInPreviousMonth - i;
        dayBox.textContent = `${day} (前月)`;
        gridContainer.appendChild(dayBox);
    }

    // 当月の日付とプルダウンメニューを配置
    for (let i = 1; i <= daysInMonth; i++) {
        const dayOfWeek = new Date(year, month, i).getDay();
        let dayBoxClass = 'day-box';
        let displayText = '未記入';

        if (dayOfWeek === 0) { // 日曜日
            displayText = '法定休日';
            dayBoxClass += ' sunday';
            setCookie(`day${i}_record`, JSON.stringify({status: 'vacation', vacationType: 'kyuka'}));
        } else if (dayOfWeek === 6) { // 土曜日
            displayText = '所定休日';
            dayBoxClass += ' saturday';
            setCookie(`day${i}_record`, JSON.stringify({status: 'vacation', vacationType: 'kyuka'}));
        } else if (holidays[i]) { // 祝日
            displayText = holidays[i] || '祝日';
            dayBoxClass += ' holiday';
            setCookie(`day${i}_record`, JSON.stringify({status: 'vacation', vacationType: 'holiday'}));
        } else {
            const cookieKey = `day${i}_record`;
            const cookieValue = getCookie(cookieKey);
            if (cookieValue) {
                const data = JSON.parse(cookieValue);
                if (data.status === 'work') {
                    displayText = '出勤';
                } else if (data.status === 'vacation') {
                    if (data.vacationType === 'yukyu') {
                        displayText = '有給休暇';
                    } else if (data.vacationType === 'summerkyu') {
                        displayText = '夏季休暇';
                    } else if (data.vacationType === 'winterkyu') {
                        displayText = '冬季休暇';
                    } else if (data.vacationType === 'anniversary') {
                        displayText = '設立休暇';
                    } else if (data.vacationType === 'kyuka') {
                        displayText = '所定休日';
                    }
                }
            }
        }

        const dayBox = document.createElement('div');
        dayBox.className = dayBoxClass;
        dayBox.innerHTML = `
            <div>${i}</div>
            <div style="text-align: right; color: gray;">${displayText}</div>
        `;
        dayBox.onclick = function() { openDetailForm(i); };
        gridContainer.appendChild(dayBox);
    }

    // 翌月の日付を配置（月末の曜日を計算し、残りのスペースを埋める）
    const lastDayOfWeek = new Date(year, month, daysInMonth).getDay();
    const daysToAdd = 6 - lastDayOfWeek; // 土曜日までの日数を計算

    for (let i = 1; i <= daysToAdd; i++) {
        const dayBox = document.createElement('div');
        dayBox.className = 'day-box next-month';
        dayBox.textContent = `${i} (翌月)`;
        gridContainer.appendChild(dayBox);
    }
});

// 休日の定義を追加
const holidays = {
    '2024-05-03': '憲法記念日',
    '2024-05-04': 'みどりの日',
    '2024-05-05': 'こどもの日',
    '2024-05-06': '祝日',
};

// Cookieを設定する関数
function setCookie(name, value, days) {
    let expires = '';
    if (days) {
        const date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = `; expires=${date.toUTCString()}`;
    }
    document.cookie = `${name}=${value || ''}${expires}; path=/html/schedule.html`;
}



function openDetailForm(day) {
    document.getElementById('modalDay').textContent = day;
    document.getElementById('detailModal').style.display = 'block';
}

function closeModal() {
    document.getElementById('detailModal').style.display = 'none';
}

function saveDetails() {
    const status = document.getElementById('status').value;
    const day = document.getElementById('modalDay').textContent;
    const key = `day${day}_record`;

    // Cookieをリセット（削除）する
    document.cookie = `${key}=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/html/schedule.html`;

    const value = JSON.stringify({
        status: status,
        startTime: status === 'work' ? document.getElementById('startTime').value : '',
        endTime: status === 'work' ? document.getElementById('endTime').value : '',
        breakTime: status === 'work' ? document.getElementById('breakTime').value : '',
        notes: document.getElementById('notes').value,
        vacationType: status === 'vacation' ? document.getElementById('vacationType').value : ''
    });

    document.cookie = `${key}=${value}; path=/html/schedule.html`;
    closeModal();
    // ブックマークチェックボックスがオンの場合にブックマークを保存
    if (document.getElementById('bookmarkCheckBox').checked) {
        saveBookmark(value);
    }

    setTimeout(function() {
        window.location.reload(true); // ページをキャッシュを無視してリロード
    }, 100); // 0.1秒の遅延を追加
}

function saveBookmark(value) {
    if (!getCookie('record1')) {
        document.cookie = `record1=${value}; path=/html/schedule.html`;
    } else if (!getCookie('record2')) {
        document.cookie = `record2=${value}; path=/html/schedule.html`;
    } else {
        document.cookie = `record3=${value}; path=/html/schedule.html`;
    }
}


function toggleTimes(status) {
    const timeInputs = document.querySelector('.modal-grid-right-top');
    const vacationTypeContainer = document.getElementById('vacationTypeContainer');
    const addOvertimeBtn = document.getElementById('addOvertimeBtn');
    if (status === 'work') {
        timeInputs.style.display = 'flex';
        vacationTypeContainer.style.display = 'none';
        addOvertimeBtn.style.display = 'block';
    } else if (status === 'vacation') {
        timeInputs.style.display = 'none';
        vacationTypeContainer.style.display = 'block';
        addOvertimeBtn.style.display = 'none';
    } else {
        timeInputs.style.display = 'none';
        vacationTypeContainer.style.display = 'none';
        addOvertimeBtn.style.display = 'none';
    }

    updateBookmarkButtons();
}

function updateBookmarkButtons() {
    const status = document.getElementById('status').value;
    const bookmarkButtons = document.getElementById('bookmarkButtons');
        const record1 = getCookie('record1');
    const record2 = getCookie('record2');
    const record3 = getCookie('record3');

    // 初期状態でクッキーを作成
    if (!record1) setCookie('record1', '', 1);
    if (!record2) setCookie('record2', '', 1);
    if (!record3) setCookie('record3', '', 1);


    if (status === 'work' && (getCookie('record1') || getCookie('record2') || getCookie('record3'))) {
        bookmarkButtons.style.display = 'block';
    } else {
        bookmarkButtons.style.display = 'none';
    }
}

function applyBookmark(record) {
    const bookmark = getCookie(record);
    if (bookmark) {
        const data = JSON.parse(bookmark);
        document.getElementById('startTime').value = data.startTime;
        document.getElementById('endTime').value = data.endTime;
        document.getElementById('breakTime').value = data.breakTime;
    }
}

// Cookieを取得する関数
function getCookie(name) {
    const nameEQ = `${name}=`;
    const ca = document.cookie.split(';');
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) === ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
}




document.addEventListener('DOMContentLoaded', function() {
    const statusSelector = document.getElementById('status');
    toggleTimes(statusSelector.value); // 初期状態で状況に基づいた入力フィールドの表示を設定

    // 残業時間入力フィールドを追加する関数
    window.addOvertimeField = function() {
        const container = document.getElementById('overtimeContainer');
        const newInputGroup = document.createElement('div');
        newInputGroup.className = 'input-group';

        const newInput = document.createElement('input');
        newInput.type = 'number';
        newInput.placeholder = '残業時間を分で入力';
        newInput.className = 'overtimeInput'; // CSSでスタイリング可能

        const deleteBtn = document.createElement('button');
        deleteBtn.className = 'delete-btn';
        deleteBtn.textContent = '削除';
        deleteBtn.onclick = function() {
            container.removeChild(newInputGroup);
        };

        newInputGroup.appendChild(newInput);
        newInputGroup.appendChild(deleteBtn);
        container.appendChild(newInputGroup);
    };

    statusSelector.addEventListener('change', function() {
        toggleTimes(this.value);
    });
});
