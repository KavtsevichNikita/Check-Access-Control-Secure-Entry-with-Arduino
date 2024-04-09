document.addEventListener("DOMContentLoaded", function () {
  const scrollLinks = document.querySelectorAll('a[href^="#"]');

  scrollLinks.forEach((scrollLink) => {
    scrollLink.addEventListener("click", function (event) {
      event.preventDefault();

      const targetId = this.getAttribute("href");
      const targetElement = document.querySelector(targetId);

      if (targetElement) {
        const offsetTop =
          targetElement.getBoundingClientRect().top + window.pageYOffset;

        window.scrollTo({
          top: offsetTop,
          behavior: "smooth",
        });
      }
    });
  });
});

function login() {
  let usernameInput = document.getElementById("start_vertice").value;
  let loginMessage = document.getElementById("loginMessage");

  if (usernameInput.trim().toLowerCase() === "admin") {
    loginMessage.textContent = "Success. You are logged in!";
    loginMessage.style.color = "green";
    document.getElementById("door").classList.add("open-door");
  } else {
    loginMessage.textContent =
      "Error. Your ID does not match, please try again!";
    loginMessage.style.color = "red";
  }

  document.getElementById("start_vertice").value = "";
}

function resetData() {
  let loginMessage = document.getElementById("loginMessage");
  loginMessage.textContent = "";
  loginMessage.style.color = ""; // Reset color
  document.getElementById("start_vertice").value = "";
  document.getElementById("door").classList.remove("open-door");
}
