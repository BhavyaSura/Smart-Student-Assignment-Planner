document.addEventListener("DOMContentLoaded", function () {
    const modal = document.getElementById("calendarModal");
    const modalDate = document.getElementById("modalDate");
    const modalAssignments = document.getElementById("modalAssignments");
    const closeButton = document.getElementById("closeCalendarModal");

    const dateButtons = document.querySelectorAll(".calendar-date-button");

    function closeModal() {
        modal.classList.remove("show");
        modal.setAttribute("aria-hidden", "true");
    }

    dateButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            const day = button.dataset.day;
            const month = Number(button.dataset.month);
            const year = Number(button.dataset.year);

            const assignments = JSON.parse(button.dataset.assignments);

            const selectedDate = new Date(year, month - 1, day);

            modalDate.textContent = selectedDate.toLocaleDateString(
                "en-US",
                {
                    weekday: "long",
                    month: "long",
                    day: "numeric",
                    year: "numeric"
                }
            );

            modalAssignments.innerHTML = "";

            if (assignments.length === 0) {
                const message = document.createElement("p");
                message.textContent = "No assignments due on this date.";
                modalAssignments.appendChild(message);
            } else {
                const list = document.createElement("ul");

                assignments.forEach(function (assignment) {
                    const item = document.createElement("li");
                    item.textContent = assignment;
                    list.appendChild(item);
                });

                modalAssignments.appendChild(list);
            }

            modal.classList.add("show");
            modal.setAttribute("aria-hidden", "false");
        });
    });

    closeButton.addEventListener("click", closeModal);

    modal.addEventListener("click", function (event) {
        if (event.target === modal) {
            closeModal();
        }
    });

    document.addEventListener("keydown", function (event) {
        if (event.key === "Escape") {
            closeModal();
        }
    });
});
