const uploadForm = document.getElementById("upload-form");
const fileUploaded = document.getElementById("file-upload");
const textInput = document.getElementById("text-input");
const classification = document.getElementById("classification");
const loading = document.getElementById("loading");
const submitButton = document.getElementById("submit-button");

const activateLoading = () => {
  loading.style.display = "flex";
  submitButton.disabled = true;
};

const deactivateLoading = () => {
  loading.style.display = "none";
  submitButton.disabled = false;
};

uploadForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  activateLoading();

  const formData = new FormData();
  const submitter = e.submitter;

  if (submitter.classList.contains("submit-text")) {
    if (textInput.value.trim()) {
      formData.append("text", textInput.value.trim());
    } else {
      alert("Digite o texto antes de enviar!");
      deactivateLoading();
      return;
    }
  } else if (submitter.classList.contains("submit-file")) {
    if (fileInput.files.length) {
      formData.append("file", fileInput.files[0]);
    } else {
      alert("Selecione um arquivo antes de enviar!");
      deactivateLoading();
      return;
    }
  }

  try {
    const response = await fetch("/upload", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();

    if (data.error) {
      alert(`Erro: ${data.error}`);
    } else {
      localStorage.setItem("responseData", JSON.stringify(data));
      window.location.href = "/response";
    }
  } catch (err) {
    alert(`Erro: ${err}`);
  } finally {
    deactivateLoading();
  }
});
