function updateCounter(){
    const text=document.getElementById("messageInput").value;
    document.getElementById("charCount").textContent=text.length+" characters";
}

async function detectSpam() {
    const message=document.getElementById("messageInput").value.trim();
    const resultBox=document.getElementById("result");
    const button=document.getElementById("analyzeBtn");

    if(!message){
        resultBox.textContent="Please enter the text!";
        resultBox.style.color="#FFD700";
        return;
    }

    button.textContent="Analyzing text....";
    button.disabled=true;

    try{
        const response=await fetch("/predict",
            {
                method:"POST",
                headers:{"Content-Type":"application/json"},
                body:JSON.stringify({message})
            }
        );

        if(!response.ok){
            throw new Error("HTTP error "+response.status);
        }
        const data=await response.json();
        if (data.prediction===1){
            resultBox.textContent="Spam Detected!";
            resultBox.style.color="red";
        }
        else{
            resultBox.textContent="No Spam Detected!";
            resultBox.style.color="green";
        }
    }
    catch(error){
        resultBox.textContent="Sever Error!";
        resultBox.style.color="orange";
    }
     finally {
        button.textContent = "Analyze Message";
        button.disabled = false;
    }
}