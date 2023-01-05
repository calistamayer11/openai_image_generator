function showSpinner() {
  document.querySelector(".loading").classList.add("show");
}

function removeSpinner() {
  document.querySelector(".loading").classList.remove("show");
}

async function fetchImage() {
  showSpinner();
  const prompt = document.querySelector("input").value;
  const size = document.querySelector("#size").value;
  const data = {
    prompt: prompt,
    size: size,
    n: 1,
  };
  const headers = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  };
  const response = await fetch("/generate", headers);
  const data2 = await response.json();
  const error = data2.error;
  const url = data2.url;
  if (response.ok) {
    removeSpinner();
  }
  if (error) {
    document.querySelector(".error").innerText = error;
  }
  const image = document.querySelector("#image");
  image.src = url;
  document.querySelector(".card").classList.add("show-p");
  document.querySelector("input").value = "";
  document.querySelector("p").innerText = prompt;
}
let button = document.querySelector(".btn");
button.addEventListener("click", fetchImage);
