const uploadForm = document.getElementById("upload-form");
const fileUploaded = document.getElementById("file-upload");
const textInput = document.getElementById("text-input");
const classification = document.getElementById("classification");
const loading = document.getElementById("loading");
const submitButton = document.getElementById("submit-button");

uploadForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  submitButton.disabled = true;
  loading.style.display = "flex";

  const formData = new FormData();

  if (textInput.value.trim()) {
    formData.append("text", textInput.value.trim());
  } else if (fileInput.files.length) {
    formData.append("file", fileUploaded.files[0]);
  } else {
    classification.innerHTML = `<p style="color:red;">Nenhum texto ou arquivo recebido.</p>`;
    return;
  }

  try {
    const response = await fetch("/upload", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();

    if (data.error) {
      classification.innerHTML = `<p style="color:red;"><strong>Erro:</strong> ${data.error}</p>`;
    } else {
      localStorage.setItem("responseData", JSON.stringify(data));

      window.location.href = "/response";
    }
  } catch (err) {
    classification.innerHTML = `<p style="color:red;">Erro na requisição: ${err}</p>`;
  } finally {
    loading.style.display = "none";
    submitButton.disabled = false;
  }
});
