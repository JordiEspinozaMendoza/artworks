document.addEventListener("DOMContentLoaded", () => {});

const addToFavorites = async (id) => {
  const csrfToken = getCookie("csrftoken");

  const request = await fetch("/api/profile/favorite/add", {
    method: "POST",
    body: JSON.stringify({
      artwork_id: id,
    }),
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
      "X-CSRFToken": csrfToken,
    },
  });

  const data = await request.json();

  if (data.status === "success") {
    alert(data.message);

    const button = document.querySelector(`[data-artwork="${id}"]`);

    button.innerText = "In Favorites";
    button.disabled = true;
  }

  if (data.status === "error") {
    alert(data.message);
  }
};

const removeFromFavorites = async (id) => {
  const csrfToken = getCookie("csrftoken");

  const request = await fetch("/api/profile/favorite/remove", {
    method: "POST",
    body: JSON.stringify({
      artwork_id: id,
    }),
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
      "X-CSRFToken": csrfToken,
    },
  });

  const data = await request.json();

  if (data.status === "success") {
    alert(data.message);

    window.location.reload();
  }

  if (data.status === "error") {
    alert(data.message);
  }
};
