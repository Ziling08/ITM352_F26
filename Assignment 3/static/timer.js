// I used ChatGPT to help with the timer and checking the selected answers.
// Python checks the time too.
const form = document.getElementById("answer-form");
const message = document.getElementById("message");
const timer = document.getElementById("timer");
let submitted = false;

form.addEventListener("submit", function (event) {
    const answers = document.getElementsByName("answer");
    let selectedCount = 0;
    for (let i = 0; i < answers.length; i++) {
        if (answers[i].checked) {
            selectedCount += 1;
        }
    }
    const required = Number(form.dataset.answerCount);

    if (selectedCount !== required) {
        event.preventDefault();
        message.textContent = "Please choose exactly " + required + " answer(s).";
    } else {
        submitted = true;
        form.querySelector('button[type="submit"]').disabled = true;
    }
});

if (timer) {
    // Start counting from the time left on this question.
    const startTime = performance.now();
    const timeLeft = Number(timer.dataset.remaining);

    function updateTimer() {
        if (submitted) {
            return;
        }

        const timePassed = (performance.now() - startTime) / 1000;
        let seconds = Math.ceil(timeLeft - timePassed);
        if (seconds < 0) {
            seconds = 0;
        }
        document.getElementById("seconds").textContent = seconds;

        if (seconds <= 5) {
            timer.classList.add("error");
        }
        if (seconds === 0) {
            submitted = true;
            form.submit(); // Send the form even if no answer was picked.
        }
    }

    updateTimer();
    setInterval(updateTimer, 100);
    document.addEventListener("visibilitychange", updateTimer);
}

window.addEventListener("pageshow", function (event) {
    // Reload if the Back button opens an old page.
    if (event.persisted) {
        window.location.reload();
    }
});
