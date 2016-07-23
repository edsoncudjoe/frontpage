/**
 * Created by Bo55 on 10/07/2016.
 */

function setBorderColor(item, color) {

    item.style.border = "2px solid " + color.toString();
    console.log("changed color: " + item);
}
function vf() {
    var n,nbx, e,ebx, s,sbx, m,mbx, fe;
    function c(k){var l=/^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return l.test(k)}function a(k){var l=/(\W+)/ig;return l.test(k)
    }
    n = document.getElementById("name").value;
    nbx = document.getElementById("name");
    e = document.getElementById("email").value;
    ebx = document.getElementById("email");
    s = document.getElementById("subject").value;
    sbx = document.getElementById("subject");
    m = document.getElementById("message").value;
    mbx = document.getElementById("message");
    fe = document.getElementById("form-error");
    if (n==""||n==null) {
        setBorderColor(nbx, "red");
        fe.innerHTML = "What's your name?";
        return false
    } else {
        if (n.length<=2){
            setBorderColor(nbx, "red");
            fe.innerHTML = "The name entered is too short";
            return false
        } else {
            if(a(n)){
                setBorderColor(nbx, "red");
                fe.innerHTML = "Are you sure that's your name? It has a strange character";
                return false
            } else {
                setBorderColor(nbx, "green");
            }}
    }
    if (e==""||e==null||!(c(e))) {
        setBorderColor(ebx, "red");
        fe.innerHTML = "Somethings not quite right with your email address";
        return false
    } else {
        setBorderColor(ebx, "green");
    }
    if (a(s)) {
        setBorderColor(sbx, "red");
        fe.innerHTML = "What did you want to talk about?";
        return false
    } else {
        setBorderColor(sbx, "green");
    }
    if (m==""||m==null) {
        setBorderColor(mbx, "red");
        fe.innerHTML = "Don't be shy, leave a message"
        return false
    } else {
        if (a(m)) {
            setBorderColor(mbx, "red");
            fe.innerHTML = "What did you want to say?"
        } else {
            setBorderColor(mbx, "green");
        }
    }

    return true
}