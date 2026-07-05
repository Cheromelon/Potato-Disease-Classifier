const imageInput = document.getElementById("imageInput");
const previewImage = document.getElementById("previewImage");

const predictBtn = document.getElementById("predictBtn");

const disease = document.getElementById("disease");
const confidence = document.getElementById("confidence");
const loading = document.getElementById("loading");


imageInput.addEventListener("change", () => {

    const file = imageInput.files[0];

    if(!file) return;

    previewImage.src = URL.createObjectURL(file);

    previewImage.style.display = "block";

});


predictBtn.addEventListener("click", async () => {

    const file = imageInput.files[0];

    if(!file){

        alert("Please select an image");

        return;

    }

    loading.innerText = "Predicting...";

    disease.innerText = "";
    confidence.innerText = "";

    const formData = new FormData();

    formData.append("file", file);

    try{

        const response = await fetch("http://127.0.0.1:8000/predict",{

            method:"POST",

            body:formData

        });

        const data = await response.json();

        loading.innerText="";

        disease.innerText=`Disease : ${data.class}`;

        confidence.innerText=`Confidence : ${data.confidence}%`;

    }

    catch(error){

        loading.innerText="";

        alert("Could not connect to backend.");

        console.log(error);

    }

});