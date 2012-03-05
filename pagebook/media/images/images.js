function validateForm()
{
var x=document.forms["myForm"]["id_image"].value;
if (x==null || x=="")
  {
  alert("Choose an image before uploading... IDIOT!");
  return false;
  }
}