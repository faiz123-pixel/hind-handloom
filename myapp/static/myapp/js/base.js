const sidebar = document.getElementById('sidebar');
const openBtn = document.getElementById('open-sidebar-btn');
const closeBtn = document.getElementById('close-sidebar-btn');

openBtn.addEventListener('click', () => {
    sidebar.classList.add('active');
});

closeBtn.addEventListener('click', () => {
    sidebar.classList.remove('active');
});
