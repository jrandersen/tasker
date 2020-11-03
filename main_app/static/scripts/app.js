// NAVBAR BURGER =========================
document.addEventListener('DOMContentLoaded', () => {
    // Get all "navbar-burger" elements
    const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);
    // Check if there are any navbar burgers
    if ($navbarBurgers.length > 0) {
      // Add a click event on each of them
      $navbarBurgers.forEach( el => {
        el.addEventListener('click', () => {
          // Get the target from the "data-target" attribute
          const target = el.dataset.target;
          const $target = document.getElementById(target);
          // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
          el.classList.toggle('is-active');
          $target.classList.toggle('is-active');
        });
      });
    }
  });

// SHOW & CLOSE MODAL - DELETE PROFILE  =========================
$("#showProfileDeleteModal").click(function() {
  $("#deleteProfile").addClass("is-active");
});

$(".closeModal").click(function() {
  $("#deleteProfile").removeClass("is-active");
});

// SHOW & CLOSE MODAL - DELETE TIME  =========================
$("#showTimeDeleteModal").click(function() {
  $("#deleteTime").addClass("is-active");
});

$(".closeModal").click(function() {
  $("#deleteTime").removeClass("is-active");
});

// SHOW & CLOSE MODAL - DELETE PROJECT  =========================
$("#showProjectDeleteModal").click(function() {
  $("#deleteProject").addClass("is-active");
});

$(".closeModal").click(function() {
  $("#deleteProject").removeClass("is-active");
});

// SHOW & CLOSE MODAL - DELETE TASK  =========================
$("#showTaskDeleteModal").click(function() {
  $("#deleteTask").addClass("is-active");
});

$(".closeModal").click(function() {
  $("#deleteTask").removeClass("is-active");
});





// SHOW & CLOSE MODAL - ADD NEW TIME  =========================
$("#showAddTimeModal").click(function() {
  $("#addTime").addClass("is-active");
});

$(".closeModal").click(function() {
  $("#addTime").removeClass("is-active");
});