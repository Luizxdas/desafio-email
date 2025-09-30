const data = localStorage.getItem("responseData");
const responseText = document.getElementById("response-area");

if (data) {
  const parsed = JSON.parse(data);
  const classification = document.getElementById("classification");
  const originalText = document.getElementById("original-area");

  classification.innerHTML = parsed.classification;
  originalText.innerHTML = parsed.message;
  responseText.value = parsed.generatedResponse;
}

const botaoHome = document.getElementById("return-button");
botaoHome.addEventListener("click", () => {
  window.location.href = "/";
});

const copyButton = document.getElementById("copy-button");
copyButton.addEventListener("click", () => {
  responseText.select();
  navigator.clipboard
    .writeText(responseText.value)
    .then(() => {
      alert("Texto copiado!");
    })
    .catch((err) => {
      console.error("Erro ao copiar: ", err);
    });
});
