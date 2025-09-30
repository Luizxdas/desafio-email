const fileInput = document.getElementById("file-upload");
const fileNameSpan = document.getElementById("file-name");
const switchEl = document.getElementById("switch");
const leftTab = switchEl.querySelector(".tab-left");
const rightTab = switchEl.querySelector(".tab-right");
const textDiv = document.querySelector(".div-text");
const uploadDiv = document.querySelector(".div-upload");
const textInstructions = document.querySelector(".text-instructions");
const fileInstructions = document.querySelector(".file-instructions");

leftTab.addEventListener("click", () => {
  switchEl.classList.remove("active-right");
  switchEl.classList.add("active-left");

  textDiv.style.display = "flex";
  uploadDiv.style.display = "none";
  textInstructions.style.display = "flex";
  fileInstructions.style.display = "none";
});

rightTab.addEventListener("click", () => {
  switchEl.classList.remove("active-left");
  switchEl.classList.add("active-right");

  textDiv.style.display = "none";
  uploadDiv.style.display = "flex";
  textInstructions.style.display = "none";
  fileInstructions.style.display = "flex";
});

fileInput.addEventListener("change", (event) => {
  const file = event.target.files[0];

  if (file) {
    fileNameSpan.textContent = file.name;
  } else {
    fileNameSpan.textContent = "Nenhum arquivo selecionado";
  }
});
