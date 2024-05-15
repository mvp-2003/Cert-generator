function showFileName(event, outputElementId) {
    var input = event.srcElement;
    var fileName = input.files[0].name;
    document.getElementById(outputElementId).textContent = "File selected: " + fileName;
}