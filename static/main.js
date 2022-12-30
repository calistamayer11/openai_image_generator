async function fetchImage(size = "512x512") {
  const prompt = document.querySelector("input").value;
  console.log(prompt);
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
  console.log(data2);
  const url = data2.url;
  const image = document.querySelector("#image");
  image.src = url;
  console.log("image", image);
  document.querySelector("input").value = "";
}
let button = document.querySelector(".btn");
button.addEventListener("click", fetchImage);
