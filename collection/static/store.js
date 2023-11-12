document.addEventListener("DOMContentLoaded", () => {
  const packages = document.querySelectorAll(".package");
  const confirmPaymentButton = document.getElementById("confirm-payment");

  packages.forEach((package) => {
    const buyButton = package.querySelector(".buy-button");
    const price = package.dataset.price;
    const name = package.dataset.name;
    const packageId = package.dataset.id;

    buyButton.addEventListener("click", () => {
      const modal = document.getElementById("modal");

      modal.classList.remove("hidden");

      document.getElementById(
        "package-selected-name"
      ).innerText = `Buy ${name}`;

      confirmPaymentButton.innerText = `Buy for $${price}`;
      confirmPaymentButton.setAttribute("data-id", packageId);
    });
  });

  confirmPaymentButton.addEventListener("click", async () => {
    let csrfToken = getCookie("csrftoken");

    const previousText = confirmPaymentButton.innerText;

    try {
      confirmPaymentButton.innerText = "Processing...";
      confirmPaymentButton.disabled = true;
      const packageSelectedInfo = document.getElementById(
        "package-selected-info"
      );
      const loader = document.getElementById("loader");
      const purchaseDetails = document.getElementById("purchase-details");

      loader.classList.remove("hidden");
      packageSelectedInfo.classList.add("hidden");

      const response = await fetch("/api/store/package", {
        method: "POST",
        body: JSON.stringify({
          package_id: confirmPaymentButton.dataset.id,
        }),
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
          "X-CSRFToken": csrfToken,
        },
      });

      const data = await response.json();

      loader.classList.add("hidden");

      if (data.status === "success") {
        confirmPaymentButton.innerText = previousText;
        confirmPaymentButton.disabled = false;

        const artworks = JSON.parse(data.artworks);

        artworks.forEach((artwork) => {
          const artworkElement = document.createElement("div");
          artworkElement.classList.add("artwork");

          const artworkImage = document.createElement("img");
          artworkImage.src = artwork.image;
          artworkImage.alt = artwork.title;
          artworkImage.height = 200;
          artworkImage.width = 200;

          const artworkTitle = document.createElement("p");
          artworkTitle.innerText = artwork.title;

          artworkElement.appendChild(artworkImage);
          artworkElement.appendChild(artworkTitle);

          purchaseDetails
            .querySelector("#artworks")
            .appendChild(artworkElement);
        });

        purchaseDetails.classList.remove("hidden");
      } else if (data.status === "error") {
        packageSelectedInfo.classList.remove("hidden");

        confirmPaymentButton.innerText = previousText;
        confirmPaymentButton.disabled = false;

        const purchaseError = document.getElementById("purchase-error");
        purchaseError.classList.remove("hidden");

        purchaseError.innerText = data.message;
      }
    } catch (error) {
      confirmPaymentButton.innerText = previousText;
      confirmPaymentButton.disabled = false;
      console.log(error);
    }
  });
});

const toggleModal = () => {
  const modal = document.getElementById("modal");
  const confirmPaymentButton = document.getElementById("confirm-payment");
  const purchaseDetails = document.getElementById("purchase-details");
  const purchaseError = document.getElementById("purchase-error");
  const artworks = document.getElementById("artworks");

  // Reset buttons
  confirmPaymentButton.innerText = "Buy for";
  confirmPaymentButton.disabled = false;

  // Remove loader
  document.getElementById("loader").classList.add("hidden");

  // Reset selected info
  document.getElementById("package-selected-info").classList.remove("hidden");

  // Remove error if exists

  if (!purchaseError.classList.contains("hidden")) {
    purchaseError.classList.add("hidden");
  }

  // Remove purchase details if exists
  if (!purchaseDetails.classList.contains("hidden")) {
    purchaseDetails.classList.add("hidden");
  }

  // Remove artworks if exists
  if (artworks.children.length > 0) {
    artworks.innerHTML = "";
  }

  // Hide modal
  modal.classList.add("hidden");
};

const getCookie = (name) => {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    let cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      let cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
};
