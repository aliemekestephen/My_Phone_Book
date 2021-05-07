function toggle2() {
    let a = document.getElementById("password2");
    let b = document.getElementById("hide11");
    let c = document.getElementById("hide22");

    if (a.type === "password"){
        a.type ="text";
        b.style.display = "block";
        c.style.display = "none";
    }
    else {
        a.type ="password";
        b.style.display = "none";
        c.style.display = "block";
    }
}