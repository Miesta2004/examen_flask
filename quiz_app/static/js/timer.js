document.addEventListener('DOMContentLoaded', () => {
    const timerBar = document.getElementById('timer-bar');
    const timeLimit = parseInt(timerBar.dataset.timeLimit);
    let remaining = timeLimit;

    const timer = setInterval(() => {
        remaining -= 0.1;
        timerBar.style.width = `${(remaining / timeLimit) * 100}%`;

        if (remaining <= 0) {
            clearInterval(timer);
            document.getElementById('timeout-form').submit();
        }
    }, 100);
});