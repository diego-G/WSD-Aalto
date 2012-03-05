function validateForm()
{
var x=document.forms["myForm"]["id_name"];
if (x!=null || x!="")
  {
  return true;
  } else {
	  alert("Please, choose a layout");
	  return false;
  }
}