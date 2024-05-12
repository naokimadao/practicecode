function createDayBoxes() {
    const container = document.querySelector('.days-container');
    for (let day = 1; day <= 31; day++) {
        const dayBox = document.createElement('div');
        dayBox.classList.add('day-box');
        
        const label = document.createElement('label');
        label.textContent = `${day}日`;
        label.classList.add('day-label');
        
        const select = document.createElement('select');
        select.classList.add('day-select');
        
        const option1 = document.createElement('option');
        option1.value = 'option1';
        option1.text = 'Option 1';
        select.appendChild(option1);
        
        const option2 = document.createElement('option');
        option2.value = 'option2';
        option2.text = 'Option 2';
        select.appendChild(option2);
        
        const option3 = document.createElement('option');
        option3.value = 'option3';
        option3.text = 'Option 3';
        select.appendChild(option3);
        
        dayBox.appendChild(label);
        dayBox.appendChild(select);
        container.appendChild(dayBox);
    }
}

// ページ読み込み時に日付ボックスを作成
window.onload = createDayBoxes;
