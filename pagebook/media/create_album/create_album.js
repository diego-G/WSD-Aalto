function validateForm()
{
var x=document.forms["myForm"]["id_name"].value;
if (x==null || x=="")
  {
  alert("Name of album must be filled out");
  return false;
  }
}