function conjugateVerb() {
  const verb = document.getElementById("verb").value;
  const tense = document.getElementById("tense").value;
  const xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("conjugation").innerHTML = this.responseText;
    }
  };
  xhttp.open("GET", `conjugate?verb=${verb}&tense=${tense}`, true);
  xhttp.send();
}