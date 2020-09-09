
function SetAllowed(IdValue)
{
    var nameId = document.getElementById(IdValue);
    id = nameId.value;
    var req = new XMLHttpRequest();
    var url = "/saveContact?id=" + id;
    alert(url);
    req.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200){
            alert(req.responseText);
            if(Clear == "Yes")
            {
                nameId.innerHTML = "<span style='color: white'>Allowed</span></button>";
                nameId.style = "background-color: green; width: 80px; padding: 6px 0px;
            }
            else
            {
                nameId.innerHTML = "<span style='color: gray'>Not Allowed</span></button>";
                nameId.style = "background-color: yellow; width: 80px; padding: 6px 0px";
            }
        }
    };
    req.open("GET", url, true);
    req.send();
}
