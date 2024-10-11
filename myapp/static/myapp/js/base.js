document.addEventListener('DOMContentLoaded', function() {
    var sidebar = document.getElementById('sidebar');
    var sidebartoggle = document.getElementById('open-sidebar-btn');
    var sidebarClose = document.getElementById('close-sidebar-btn');

    sidebartoggle.addEventListener('click', function() {
        sidebar.classList.toggle('sidebar-open');
    });

    sidebarClose.addEventListener('click', function() {
        sidebar.classList.remove('sidebar-open');
    });
    
    document.addEventListener('click', function(event) {
        // Check if the click target is outside the sidebar and not the toggle button
        if (!sidebar.contains(event.target) && !sidebartoggle.contains(event.target)) {
            sidebar.classList.remove('sidebar-open');
        }
    });
});


