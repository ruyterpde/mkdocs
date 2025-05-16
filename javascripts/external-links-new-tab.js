document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll("a[href^='http']:not([href*='ruyter.org'])").forEach(function (el) {
    el.setAttribute("target", "_blank");
    el.setAttribute("rel", "noopener noreferrer");
  });
});
