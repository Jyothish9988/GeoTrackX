const toggleSwitch = document.querySelector('.theme-switch input[type="checkbox"]');

// Set dark theme by default
document.documentElement.setAttribute('data-theme', 'dark');
toggleSwitch.checked = true;

function switchTheme(e) {
    if (e.target.checked) {
        document.documentElement.setAttribute('data-theme', 'dark');
    } else {
        document.documentElement.setAttribute('data-theme', 'light');
    }
}

toggleSwitch.addEventListener('change', switchTheme, false);
